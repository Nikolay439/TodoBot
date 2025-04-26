import telebot
from random import choice

token = "token telegramm bot"

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

HELP = '''
/help - напечатать справку по программе.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавлять случайную задачу на дату Сегодня'''

tasks={}

def add_todo(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты в словаре нет
        # Создаем запись с ключом date
        tasks[date] = []
        tasks[date].append(task)



@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command= message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2].lower()
    add_todo(date, task)
    text = " Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "cегодня"
    task = choice(RANDOM_TASKS)
    add_todo(date, task)
    text = " Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text =""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[]" + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
