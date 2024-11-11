import telebot


#Укажите ваш токен API, полученный от BotFather
Token = '7887933734:AAFBoqlBctdpAb2Fdwyls1oQAgKIM3vLreg'
#Создаем объект бота
bot = telebot.Telebot(Token)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message,'Привет!Попугай Джон звонит,Попугай Джон звонит,'
                         'Попугай Джон звонит!!!У него сегодня был хороший день,'
                         'попугай тебе желает того ')

if __name__ == '__main__':
#   Запускаем бесконечный цикл обработки сообщений
    bot.polling()