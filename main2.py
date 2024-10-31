import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7775230802:AAF-xnz7AGINcZh-0pDktmRXf0jl0tb4vgA')


@bot.message_handler(commands=['start'])
def start(message):   
    markup = types.ReplyKeyboardMarkup()

    btn1 = types.KeyboardButton('Chek ✅')
    btn2 = types.KeyboardButton('Video 📹')
    btn3 = types.KeyboardButton('Audio 🎵')
    btn4 = types.KeyboardButton('Photo 🖼')

    markup.row(btn1)
    markup.row(btn2,btn3,btn4)
    #bot.send_message(message.chat.id, 'Hi',reply_markup=markup)

    bot.send_message(message.chat.id, 'Menu',reply_markup=markup )
    
    
    
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Chek ✅': 
        bot.send_message(message.chat.id, 'chek')
    elif message.text == 'Video 📹': 
        video  = open('./other/raper.mp4', 'rb')
        bot.send_video(message.chat.id, video)
    elif message.text == 'Audio 🎵': 
        audio  = open('./other/rap.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    elif message.text == 'Photo 🖼': 
        cat  = open('./other/cat.JPG', 'rb')
        bot.send_photo(message.chat.id, cat, 'Nice cat!!!')



@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Start',callback_data='start')
    
    btn2 = types.InlineKeyboardButton('Edit',callback_data='edit')
    btn3 = types.InlineKeyboardButton('Delete',callback_data='delete')
    btn4 = types.InlineKeyboardButton('Site',url='https://steamcommunity.com/id/Lalka228_navi/')
    
    markup.row(btn1,btn2,btn3)
    markup.row(btn4)
    
    bot.reply_to(message, "Nice photo",reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
        

























bot.polling(non_stop=True)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Privet {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')