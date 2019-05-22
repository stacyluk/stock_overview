from flask_sslify import SSLify
import telebot
from flask import Flask, request
import os

TOKEN = "890044169:AAEyYetqi0ZLqFzFnDAkpHW6QNWdgzcgfe0"
APP_NAME = "stock-overviewbot"

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)
sslify = SSLify(server)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Я бот, помогающий совершать выгодные инвестиции."
                                           "Ты можешь управлять мной с помощью следующих команд:"
                                           "/stockinfo - информация по стоимости акций ведущих компаний"
                                           "/stockinfo<oтрасль> - информация по стоимости акций ведущих "
                                           "компаний конкретной области ()"
                                           "/profit - в какие отрасли выгоднее инвестировать сегодня"
                                           "/profitwhy - в какие отрасли выгоднее инвестировать и почему")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_text_messages(message):
    if message.text == "/stockinfo":
        bot.send_message(message.from_user.id, "Извените, неполадки в соединении с сервером.")
    elif message.text == "/profit":
        bot.send_message(message.from_user.id, "Извените, неполадки в соединении с сервером.")
    elif message.text == "/profitwhy":
        bot.send_message(message.from_user.id, "Извените, неполадки в соединении с сервером.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def echo_message(message):
#    bot.reply_to(message, message.text)


@server.route("/" + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


#bot.polling()

@server.route("/", methods=['GET'])
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))
    return "!", 200

if __name__ == "__main__":
    #server.run()
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
