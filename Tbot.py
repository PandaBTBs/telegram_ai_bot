from openai import OpenAI
import telebot
import random
from telebot import types
import time
import webbrowser
import tkn #your token

TOKEN = tkn.TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Приветствую, {0.first_name}!\n            Я - <b>{1.first_name}</b>\n      исскуственный интелект, \nсозданный для помощи пользователям. \n <Команды> - интрукции".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
            
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
                bot.send_message(call.message.chat.id, '1. 🎲Рандомное число🎲 \n\n 2. ♦Команды♦ \n\n 3. /st стим \n\n 4. /st obs\n\n 5. /st скриншот \n\n 6. /st vs studio \n\n 7. /st дискорд \n\n 8. /st погода')
                
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<__Список_команд__>",
                reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="empty message")
 
    except Exception as e:
        print(repr(e))
        

bot.polling(none_stop=True)
