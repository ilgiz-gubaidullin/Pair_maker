import telebot
import random

bot = telebot.TeleBot('')

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
    print(players_list)


@bot.message_handler(content_types=['text'])
def user_adding(message):
    addition_list = message.text.split()
    if '+' == addition_list[0]:
        if message.from_user.first_name not in players_list:
            players_list.append(message.from_user.first_name)
        else:
            players_list.append(addition_list[1])

    if len(players_list) == 4:
        random.shuffle(players_list)
        bot.send_message(message.chat.id, 'Первая пара игроков: {} и {}'.format(players_list[0], players_list[1]))
        bot.send_message(message.chat.id, 'Вторая пара игроков: {} и {}'.format(players_list[2], players_list[3]))
        players_list.clear()


bot.polling()
