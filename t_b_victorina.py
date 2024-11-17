import telebot
from random import choice

# Токен вашего бота
API_TOKEN = '7514413100:AAFu51FBMbRJII9DyZYkl44vPznwrvq_pPY'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

# Вопросы по истории разной сложности
questions = {
    1: [
        ("Когда произошло Крещение Руси?", "988 год"),
        ("Кто был первым царем всея Руси?", "Иван Грозный")
    ],
    2: [
        ("Какое событие произошло в 1812 году?", "Отечественная война против Наполеона"),
        ("Что такое Ледовое побоище?", "Битва новгородцев с рыцарями Ливонского ордена в 1242 году")
    ],
    3: [
        ("В каком веке было создано Московское княжество?", "XIV век"),
        ("Какой договор положил конец Смутному времени?", "Деулинское перемирие")
    ],
    4: [
        ("Какая битва произошла между русскими войсками и шведами в 1709 году?", "Полтавская битва"),
        ("Кому принадлежит фраза «Петербургский период» моей жизни кончился'?", "Александр Пушкин")
    ],
    5: [
        ("Как назывался первый русский печатный учебник?", "Азбука Ивана Федорова"),
        ("Кто такой протопоп Аввакум?", "Один из лидеров старообрядчества, автор Жития протопопа Аввакума")
    ]
}

current_user_question = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это викторина по истории. Выбери уровень сложности от 1 до 5.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global current_user_question

    chat_id = message.chat.id

    try:
        user_input = int(message.text.strip())

        if user_input in questions.keys():
            if chat_id not in current_user_question:
                question, answer = choice(questions[user_input])
                current_user_question[chat_id] = (question, answer)
                bot.send_message(chat_id, f"Вопрос: {question}")
            else:
                bot.send_message(chat_id, "Сначала ответьте на текущий вопрос.")
        elif chat_id in current_user_question:
            given_answer = message.text.strip().lower()
            correct_answer = current_user_question[chat_id][1].lower()

            if given_answer == correct_answer:
                bot.send_message(chat_id, "Правильно!")
            else:
                bot.send_message(chat_id, f"Неправильно. Правильный ответ: {correct_answer}.")

            del current_user_question[chat_id]
            bot.send_message(chat_id, "Выберите новый уровень сложности от 1 до 5.")
        else:
            bot.reply_to(message, "Уровень сложности должен быть числом от 1 до 5.")

    except ValueError:
        if chat_id in current_user_question:
            given_answer = message.text.strip().lower()
            correct_answer = current_user_question[chat_id][1].lower()

            if given_answer == correct_answer:
                bot.send_message(chat_id, "Правильно!")
            else:
                bot.send_message(chat_id, f"Неправильно. Правильный ответ: {correct_answer}.")

            del current_user_question[chat_id]
            bot.send_message(chat_id, "Выберите новый уровень сложности от 1 до 5.")
        else:
            bot.reply_to(message, "Уровень сложности должен быть числом от 1 до 5.")


if __name__ == '__main__':
    bot.polling(none_stop=True)