"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import settings as settings
import random

logging.basicConfig(filename='bot.log', level=logging.INFO, encoding='utf-8')


def random_planet(planets):
    return random.choice(planets)


def in_what_constellation(update, context):

    user_text = update.message.text

    dt = datetime.datetime.today()
    user_dt = f'{dt.year}/{dt.month}/{dt.day}'

    for planet in user_text.split():
        planet = planet.lower()

    planets = {
        'mercury': ephem.Mercury(user_dt),
        'venus': ephem.Venus(user_dt),
        'mars': ephem.Mars(user_dt),
        'jupiter': ephem.Jupiter(user_dt),
        'saturn': ephem.Saturn(user_dt),
        'uranus': ephem.Uranus(user_dt),
        'neptune': ephem.Neptune(user_dt)
    }

    try:
        constellation = ephem.constellation(planets[planet])
        update.message.reply_text(
            f'Сегодня планета {planet} находится в созвездии {constellation}')
    except KeyError:
        update.message.reply_text(
            f"Такой планеты нет, попробуйте ввести /planet {random_planet(['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'])}"
        )


def greet_user(update, context):
    print('Вызвана комманда - /start')
    update.message.reply_text('Привет пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', in_what_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
