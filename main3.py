import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('7775230802:AAF-xnz7AGINcZh-0pDktmRXf0jl0tb4vgA')

name = ''


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('qiqa1212.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "Hi, let's register you \nWrite your <b>Name:</b>", parse_mode='html')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Write your <b>pass:</b>", parse_mode='html')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()
    
    conn = sqlite3.connect('qiqa1212.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s' , '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton('List',callback_data='users'))
    bot.send_message(message.chat.id, "You're registered", reply_markup=markup)

    #bot.send_message(message.chat.id, "Write your <b>pass:</b>", parse_mode='html')
    

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    conn = sqlite3.connect('qiqa1212.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'<b>ID:</b> {el[0]}\n<b>Name:</b> {el[1]}\n<b>Pass:</b> {el[1]}\n\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info, parse_mode='html')










@bot.message_handler()
def info(message):
    bot.reply_to(message, message.text)


bot.polling(non_stop=True)