import telebot
import constants

#main variables
TOKEN = constants.TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hi! ')


bot.polling()
