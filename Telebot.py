import telebot

TOKEN = "5786288318:AAHUlg3nmN5bdLSJRNhDBZ5JFG8pS1VDW8s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 1])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Количество параметров не совпадает с форматом ввода.\n')

        quote, base, amount = values
        total_base = convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e} Как надо?: /help')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e} \nКак правильно вводить данные: /help')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)



