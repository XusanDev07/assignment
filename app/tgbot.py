# Javohir, [19.07.2023 19:21]
# 6121396810:AAErUp1PJPbH1rprIJhZuSUmdS_MCbfRQp4

# Avazbek aka fintech, [19.07.2023 20:07]
# import telebot
#
# bot = telebot.TeleBot()
import requests



# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, f"Salom Chat id: {message.chat.id}")


def send_messege(doktornik, xamshiranik, xona, bemorism):
    token = "6331128208:AAE7zj1VCI5lo1XWR7XwnisOlGE5q447ujU"
    chat_id = "-756061713"
    msg = f"{xona.id}ga {doktornik} bilan {xamshiranik} borsin. {bemorism}ni korishga"
    url = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&parse_mode=HTML&text="+msg
    requests.get(url)

    # bot.send_message(-756061713, f"{xona.id}ga {doktornik} bilan {xamshiranik} borsin. {bemorism}ni korishga")



# bot.polling()