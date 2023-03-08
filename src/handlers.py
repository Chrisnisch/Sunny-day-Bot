# добавить пиздюли за пустые команды set и edit, форматирование текста, решить проблему чат-террористов
from aiogram import types, Dispatcher
import re
import datetime

cur_day = ""
cur_time = ""
name = ""


def command_help(message: types.Message):
    f = open("help.txt", encoding="UTF-8")
    s = f.read()
    f.close()
    return message.reply(s)


def command_lunch(message: types.Message):
    # посмотреть текущий обэд
    global cur_day, name, cur_time
    f = open("lunch.txt", "r")
    cur_lunch = f.read()
    cur_lunch = cur_lunch[0].upper() + cur_lunch[1:]
    f.close()
    return message.reply(f'Сегодня {cur_day} на обед:\n{cur_lunch}'
                         f'\nИнформация предоставлена @{name} в {cur_time}'
                         f'\nЕсли что-то поменялось, напишите /edit_lunch и новый состав обеда')


def command_set_lunch(message: types.Message):
    # установить обэд
    global cur_day, name, cur_time
    cur_day = datetime.date.today().strftime('%d.%m')
    cur_time = datetime.datetime.now().time().strftime('%H:%M')
    name = message.from_user.username
    f = open("lunch.txt", "w")
    f.write(re.search("""([А-я\s,.])+""", message.text).group()[1:])
    f.close()
    return message.reply("Состав обеда на сегодня добавлен")


def command_edit_lunch(message: types.Message):
    # редактирование обэда (если в санни дей что-то закончилось и подают другое)
    global cur_day, name, cur_time
    cur_day = datetime.date.today().strftime('%d.%m')
    cur_time = datetime.datetime.now().time().strftime('%H:%M')
    name = message.from_user.username
    f = open("lunch.txt", "w")
    f.write(re.search("""([А-я\s,.])+""", message.text).group()[1:])
    f.close()
    return message.reply("Состав обеда обновлён")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_help, commands="help")
    dp.register_message_handler(command_lunch, commands="lunch")
    dp.register_message_handler(command_set_lunch, commands="set_lunch")
    dp.register_message_handler(command_edit_lunch, commands="edit_lunch")
