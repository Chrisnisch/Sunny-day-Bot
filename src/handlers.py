# возможно стоит перенести тексты сообщений бота в отдельный файл
from aiogram import types, Dispatcher
import re
import datetime

cur_day = ""
cur_time = ""
name = ""
white_list = set(open("white-list.txt", "r", encoding="UTF-8").read().split())


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
    if cur_lunch == "":
        return message.reply("Нет информации")
    cur_lunch = cur_lunch[0].upper() + cur_lunch[1:]
    f.close()
    return message.reply(f'Сегодня <b>{cur_day}</b> на обед:\n<b>{cur_lunch}</b>'
                         f'\nИнформация предоставлена @{name} в {cur_time}', parse_mode="HTML")


def command_set_lunch(message: types.Message):
    # установить и редактировать обэд
    global cur_day, name, cur_time
    cur_day = datetime.date.today().strftime('%d.%m')
    cur_time = datetime.datetime.now().time().strftime('%H:%M')
    name = message.from_user.username
    s = re.search("""([А-я\s,.])+""", message.text)
    if s is not None:
        s = s.group()[1:]
        t = re.split("""[\s,.-]+""", s)
        print(t)
        for word in t:
            if word not in white_list:
                return message.reply("Я тебе не верю.")
            else:
                continue
    else:
        return message.reply("Пустое сообщение")
    f = open("lunch.txt", "w")
    f.write(s)
    f.close()
    return message.reply("Состав обеда на сегодня добавлен")


def command_edit_lunch(message: types.Message):
    # редактирование обэда (если в санни дей что-то закончилось и подают другое)
    global cur_day, name, cur_time
    cur_day = datetime.date.today().strftime('%d.%m')
    cur_time = datetime.datetime.now().time().strftime('%H:%M')
    name = message.from_user.username
    s = re.search("""([А-я\s,.])+""", message.text)
    if s is not None:
        s = s.group()[1:]
        t = re.split("""[\s,.-]+""", s)
        print(t)
        for word in t:
            if word not in white_list:
                return message.reply("Я тебе не верю.")
            else:
                continue
    else:
        return message.reply("Пустое сообщение")
    f = open("lunch.txt", "w")
    f.write(s)
    f.close()
    return message.reply("Состав обеда обновлён")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_help, commands=["help", "start"])
    dp.register_message_handler(command_lunch, commands="lunch")
    dp.register_message_handler(command_set_lunch, commands="set_lunch")
    dp.register_message_handler(command_edit_lunch, commands="edit_lunch")
