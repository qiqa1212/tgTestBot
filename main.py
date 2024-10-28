import telebot
import time

bot = telebot.TeleBot('7775230802:AAF-xnz7AGINcZh-0pDktmRXf0jl0tb4vgA')

def remove_none(d):
    if isinstance(d, dict):
        # Рекурсивно обрабатываем словарь
        return {k: remove_none(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        # Если значение — список, обрабатываем каждый элемент
        return [remove_none(i) for i in d if i is not None]
    else:
        # Если значение не словарь и не список, возвращаем его как есть
        return d

@bot.message_handler(commands=['info'])
def first(message):
    print(type(message))
    cleaned_message = remove_none(message)
    message_dict = message.__dict__
    cleaned_dict = remove_none(message_dict)
    bot.send_message(message.chat.id, message_dict)

# Функция для ручной обработки обновлений в течение 10 секунд
def run_bot_for_10_seconds():
    start_time = time.time()
    while time.time() - start_time < 10:
        # Получаем новые обновления
        updates = bot.get_updates(timeout=2)
        
        if updates:
            # Обрабатываем каждое обновление
            bot.process_new_updates(updates)
        time.sleep(1)  # Задержка между запросами

    print("Бот остановлен после 10 секунд.")

# Запуск бота на 10 секунд
run_bot_for_10_seconds()
