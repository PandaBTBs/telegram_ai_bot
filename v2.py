from openai import OpenAI
import telebot
import random
from telebot import types
import time
import webbrowser
import tkn
import os

TOKEN = tkn.TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("cmd")
    item3 = types.KeyboardButton("steam")
    item4 = types.KeyboardButton("sharex")
    item5 = types.KeyboardButton("rec. OBS")
    item6 = types.KeyboardButton("vs_studio")
    item7 = types.KeyboardButton("discord")
    item8 = types.KeyboardButton("weather_forecastа")
    item9 = types.KeyboardButton("music")
    item10 = types.KeyboardButton("news")
    item11 = types.KeyboardButton("video")
    
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
 
    bot.send_message(message.chat.id, "Приветствую, {0.first_name}!\n            Я - <b>{1.first_name}</b>\n      \
        исскуственный интелект, \nсозданный для помощи пользователям. \n \
        Команды - интрукции".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
            
            
        elif message.text == 'cmd':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("*list cmds*", callback_data='list')
 
            markup.add(item1)
 
            bot.send_message(message.chat.id, 'CMD list commands', reply_markup=markup)
            
            
        elif message.text == 'music':
            mc = 'Пока недоступно ❌'
            bot.send_message(message.chat.id, mc)
            pass
        
        elif message.text == 'news':
            nw = 'Пока недоступно ❌'
            bot.send_message(message.chat.id, nw)
            webbrowser.open("https://ria.ru/")
            pass
        
        elif message.text == 'video':
            vo = 'Пока недоступно ❌'
            bot.send_message(message.chat.id, vo)
            pass
        
        elif message.text == 'steam':
            os.startfile('D:\steamT1\steam.exe')
        
            bot.send_message(message.chat.id, 'Стим запущен✅')
            
        elif message.text == 'rec. OBS':
            webbrowser.open("steam://rungameid/1905180")
            bot.send_message(message.chat.id, 'OBS запущен✅')
            
        elif message.text == 'sharex':
            os.startfile(r'D:/steamT1/steamapps/common/ShareX/ShareX_Launcher')
            bot.send_message(message.chat.id, 'sharex запущен✅')
            
        elif message.text == 'vs_studio':
            webbrowser.open('steam://rungameid/1325860')
            bot.send_message(message.chat.id, 'vs_studio запущен✅')
            
        elif message.text == 'discord':

            webbrowser.open('https://discord.com/channels/@me')
            bot.send_message(message.chat.id, 'discord запущен✅')
            
        elif message.text == 'weather_forecastа':
            
            import requests
            import datetime
            from pprint import pprint
            from config import open_weather_token # your token https://home.openweathermap.org/ (api keys)


            def get_weather(city, open_weather_token):

                code_to_smile = {
                    "Clear": "Ясно \U00002600",
                    "Clouds": "Облачно \U00002601",
                    "Rain": "Дождь \U00002614",
                    "Drizzle": "Дождь \U00002614",
                    "Thunderstorm": "Гроза \U000026A1",
                    "Snow": "Снег \U0001F328",
                    "Mist": "Туман \U0001F32B"
                    }

                try:
                    r = requests.get(
                        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
                    )
                    data = r.json()
                    pprint(data)

                    city = data["name"]
                    cur_weather = data["main"]["temp"]

                    weather_description = data["weather"][0]["main"]
                    if weather_description in code_to_smile:
                        wd = code_to_smile[weather_description]
                    else:
                        wd = "Посмотри в окно, не пойму что там за погода!"

                    humidity = data["main"]["humidity"]
                    pressure = data["main"]["pressure"]
                    wind = data["wind"]["speed"]
                    sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
                    sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
                    length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                    data["sys"]["sunrise"])

                    rez =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                            f"Хорошего дня!"
                        )
                    bot.send_message(message.chat.id, rez)
                except Exception as ex:
                    bot.send_message(message.chat.id, ex)
                    print("Проверьте название города")


            def main():
                bot.send_message(message.chat.id, "Введите город: ")
                city = message.text
                get_weather(city, open_weather_token)


            if __name__ == '__main__':
                main()
      
        else:
            bot.send_message(message.chat.id, 'loading ... ')
            
            client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
            while __name__ == '__main__':
                    completion = client.chat.completions.create(
                    model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
                    messages=[
                    {"role": "system", "content": "Always answer briefly."},
                    {"role": "user", "content": message.text } 
                    ],
                    temperature=0.4,
                    )
                    l = str(completion.choices[0].message)
                    seconds = time.time()
                    seconds_last = time.ctime(seconds)
                    output = f'AI: {l[32:-57]}, \n{seconds_last} \n'
                    break

            bot.send_message(message.chat.id, output)
            
            
                
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'list':
                bot.send_message(call.message.chat.id, '1. /st steam \n\n 4. /st rec. OBS\n\n 5. /st sharex \n\n 6. /st vs_studio \n\n 7. /st discord \n\n 8. /st weather_forecastа')
                
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="list cmds:",
                reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="empty message")
 
    except Exception as e:
        print(repr(e))
        

bot.polling(none_stop=True)
