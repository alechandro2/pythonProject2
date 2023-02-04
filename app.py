import telebot

TOKEN = "6050657135:AAGQRkSrvQsvI7-NEi-fuDW5JBKVcB-J4Po"

bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин':'BTC',
    'эфириум': 'ETC',
    'доллар' : 'USD',

}

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду в следующем формате:\n<имя валюты> \
 <в какую валюту перевести> \
 <количество переводимой валюты>'
    bot.reply_to(message, text)


    bot.polling()

