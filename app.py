from flask_sslify import SSLify
import telebot
from flask import Flask, request
import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from fbprophet import Prophet


TOKEN = "890044169:AAEyYetqi0ZLqFzFnDAkpHW6QNWdgzcgfe0"
APP_NAME = "stock-overviewbot"

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)
sslify = SSLify(server)


def str_to_date(x):
    return datetime.strptime(x, '%Y-%m-%d')


m = Prophet()


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет, ' + message.from_user.first_name + ' нажми /help для получения справки')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Я бот, помогающий совершать выгодные инвестиции.\n\n"
                                           "Ты можешь управлять мной с помощью следующей команды:\n\n"
                                           "/stockinfo - прогноз о стоимости акций\n"
                                           #"/stockinfooil - информация по стоимости акций ведущих "
                                           #"нефтяных компаний\n"
                                           #"/stockinfocorporation - информация по стоимости акций ведущих "
                                           #"транснациональных компаний\n"
                                           #"/profit - в какие отрасли выгоднее инвестировать сегодня\n"
                                           #"/profitwhy - в какие отрасли выгоднее инвестировать и почему\n")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_text_messages(message):
    if message.text == "/stockinfo":
        bot.send_message(message.from_user.id, "Выберите одну из трех компаний, для которой вы хотите посмотреть предсказания цены акций: /Microsoft, /Google или /Facebook.")
    elif message.text == "/Microsoft":
        bot.send_message(message.from_user.id, "Ведутся технические работы. Приносим свои извинения за неудобства.")
    elif message.text == "/Google":
        bot.send_message(message.from_user.id, "Ведутся технические работы. Приносим свои извинения за неудобства.")
    elif message.text == "/Facebook":
        bot.send_message(message.from_user.id, "Ведутся технические работы. Приносим свои извинения за неудобства.")
    elif message.text == "/profitwhy":
       bot.send_message(message.from_user.id, "Ведутся технические работы. Приносим свои извинения за неудобства.")
    else:
       bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@server.route("/" + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/", methods=['GET'])
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))
    return "!", 200


if __name__ == "__main__":
    #server.run()
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
