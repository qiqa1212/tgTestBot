import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('7775230802:AAF-xnz7AGINcZh-0pDktmRXf0jl0tb4vgA')
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
   bot.send_message(message.chat.id, 'Hi, write your sum:')
   bot.register_next_step_handler(message, summa)
   

def summa(message):
   global amount
   try:
      amount = float(message.text.strip())
   except ValueError:
      bot.reply_to(message, f'Invalide sum!\nWrite sum:')
      bot.register_next_step_handler(message, summa)
      return

   if amount > 0:
      markup = types.InlineKeyboardMarkup(row_width=2)

      btn1 = types.InlineKeyboardButton('USD/EUR',callback_data='usd/eur')
      btn2 = types.InlineKeyboardButton('EUR/USD',callback_data='eur/usd')

      btn3 = types.InlineKeyboardButton('GBP/USD',callback_data='gbp/usd')
      btn4 = types.InlineKeyboardButton('Other',callback_data='else')

      markup.add(btn1,btn2,btn3,btn4)
      bot.send_message(message.chat.id, 'Choose your pair', reply_markup=markup)
   else:
      bot.reply_to(message, f'Sum must be more than 0\nWrite new sum:')
      bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
   global amount
   if call.data != 'else':
      values = call.data.upper().split('/')
      res = currency.convert(amount,values[0],values[1] )
      bot.send_message(call.message.chat.id, f'Your {amount} {values[0]} = {round(res,2)} {values[1]}\n Write new sum')
      bot.register_next_step_handler(call.message, summa)
   else:
      info = ''
      currencys = currency.currencies
      for cur in currencys:
         info += f'<b>{cur}</b> '
      bot.send_message(call.message.chat.id, f'Write your pair, like <b>USD\EUR</b> \nSupported currency:\n{info}', parse_mode='html')
      
      bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
   values = message.text.upper().split('/')
   try:
      res = currency.convert(amount,values[0],values[1] )
      bot.send_message(message.chat.id, f'Your {amount} {values[0]} = {round(res,2)} {values[1]}\n Write new sum')
      bot.register_next_step_handler(message, summa)
   except Exception:
      bot.send_message(message.chat.id, 'Something wrong. Try again!')
      bot.register_next_step_handler(message, my_currency)
   


@bot.message_handler(content_types=['text'])
def get_wether(message):
   pass

bot.polling(non_stop=True)