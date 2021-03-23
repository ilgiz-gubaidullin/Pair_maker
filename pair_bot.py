import telebot
import random

bot = telebot.TeleBot('1682187129:AAF7sN4HXtrOwz1oKSiuXQjv2hwNtksxD80')

players_list = []
stickers_list =[]


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    if message.sticker.file_unique_id == 'AgADMgADN8pHFg':
        players_list.append(message.from_user.first_name)
        stickers_list.append(message.sticker.file_unique_id)
        if len(stickers_list) > 1:
            players_list.clear()
            players_list.append(message.from_user.first_name)
            stickers_list.clear()
            stickers_list.append(message.sticker.file_unique_id)


@bot.message_handler(content_types=['text'])
def user_adding(message):
    l2 = message.text.split()
    if ('+' in l2) and (message.from_user.first_name not in players_list):
        players_list.append(message.from_user.first_name)
    elif len(l2) == 2:
        players_list.append(l2[1])

    if len(players_list) == 4:
        random.shuffle(players_list)
        bot.send_message(message.chat.id, 'Первая пара игроков: {} и {}'.format(players_list[0], players_list[1]))
        bot.send_message(message.chat.id, 'Вторая пара игроков: {} и {}'.format(players_list[2], players_list[3]))
        players_list.clear()


bot.polling()
