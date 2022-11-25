
import telebot
import json

API_TOKEN= '5741802861:AAHRwYh2FHtcxCiAxV6iDaP8RH6unhn3tAw'

bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,"Готов к работе!")

films=[]

def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека была успешно загружена")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Готов к работе!")
    try:
        load()
        bot.send_message(message.chat.id,"Фильмотека была успешно загружена!")

    except:
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властелин колец")
        films.append("Техасская резня бензопилой")
        films.append("Санта Барбара") 
        bot.send_message(message.chat.id,"Фильмотека была загружена по умолчанию!")

@bot.message_handler(commands=['show'])
def show_message(message):
    bot.send_message(message.chat.id,' '.join(films))

@bot.message_handler(commands=['calc'])
def calc_message(message):
    eq = message.text.split()[1:]
    print(eq)
    bot.send_message(message.chat.id,eval(eq[0]))


@bot.message_handler(content_types='text')
def message_reply(message):
    if 'привет' in message.text:
        bot.send_message(message.chat.id,'и тебе привет')
bot.polling()
