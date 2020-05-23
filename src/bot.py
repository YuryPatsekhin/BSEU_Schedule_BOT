import telebot

#main variables
TOKEN = "1175307787:AAF4iOHtNeDRhYzZ1edvBooCqTCgSX_crno"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Hi! ')


bot.polling()
