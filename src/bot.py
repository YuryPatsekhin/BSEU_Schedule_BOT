import telebot
import constants
import getSchedule

#main variables
TOKEN = constants.TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hi!')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if (message.text == "расписание"):
        bot.send_message(message.chat.id, 'Загружаю, минуточку..')
        getSchedule.request(message.text)
        img = open('out.png', 'rb')
        bot.send_photo(message.chat.id, img)


bot.polling()
