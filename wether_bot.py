import telebot
import requests
from telebot import types
import json


bot = telebot.TeleBot('7775230802:AAF-xnz7AGINcZh-0pDktmRXf0jl0tb4vgA')
API = '30ddaa74defe94608faa19cb322c038c'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Write your sity:')


@bot.message_handler(content_types=['text'])
def get_wether(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Situation: {data["weather"][0]['description']} \nTemp: {temp} \nFeels like: {data["main"]["feels_like"]} \n')
        
        image = 'sun.png' if temp > 10.0 else 'overcast_clouds.png'
        file = open('./other/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Incorect city')


bot.polling(non_stop=True)