import telebot
from random import randint
'''Если захочется добавить стикеры'''
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = ''
    if message.text.lower() == "подели":
        # Просим 4 имени
        msg = bot.reply_to(message, "напиши 4 имени через пробелы")
        bot.register_next_step_handler(msg, pair_making)

def pair_making(message):
    l1 = message.text.split()
    n = len(l1)
    if n == 4:
        p1 = randint(0, 3)
        p2 = randint(0, 3)
        while p2 == p1:
            p2 = randint(0, 3)
        p3 = randint(0, 3)
        while p3 == p1 or p3 == p2:
            p3 = randint(0, 3)
        p4 = randint(0, 3)
        while p4 == p3 or p4 == p2 or p4 == p1:
            p4 = randint(0, 3)
        bot.send_message(message.chat.id, 'Первая пара игроков: {} и {}'.format(l1[p1], l1[p2]))
        bot.send_message(message.chat.id, 'Вторая пара игроков: {} и {}'.format(l1[p3], l1[p4]))


bot.polling(none_stop=True, interval=0)
