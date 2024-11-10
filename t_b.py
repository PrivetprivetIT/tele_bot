import telebot

# Вставьте сюда ваш токен от BotFather
API_TOKEN = '7514413100:AAFu51FBMbRJII9DyZYkl44vPznwrvq_pPY'

# Создаем бота
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Привет! Я пока только учусь разговаривать. Буду рад если поможешь!")

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки сообщений
    bot.polling()