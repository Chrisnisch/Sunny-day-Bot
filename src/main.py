from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
import re


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


def clear_lunch():
    # функция будет очищать файл с обэдом каждый день в 21:00
    f = open("lunch.txt", "w")
    f.close()


def on_startup():
    print("Бот онлайн")


@dp.message_handler(commands=["lunch"])
def lunch(message: types.Message):
    # посмотреть текущий обэд
    f = open("lunch.txt", "r")
    cur_lunch = f.read()
    f.close()
    return message.reply(f'Сегодня у нас:\n{cur_lunch}'
                         f'\nЕсли что-то поменялось, напишите /edit_lunch и новый состав обеда')


@dp.message_handler(commands=["set_lunch"])
def set_lunch(message: types.Message):
    # установить обэд
    f = open("lunch.txt", "w")
    f.write(re.search("""([А-я\s,.])+""", message.text).group())
    f.close()
    return message.reply("Состав обеда на сегодня добавлен")


@dp.message_handler(commands=["edit_lunch"])
def edit_lunch(message: types.Message):
    # редактирование обэда (если в санни дей что-то закончилось и подают другое)
    f = open("lunch.txt", "w")
    f.write(re.search("""([А-я\s,.])+""", message.text).group())
    f.close()
    return message.reply("Состав обеда обновлён")


executor.start_polling(dp, skip_updates=True)
