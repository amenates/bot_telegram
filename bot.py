import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime

logging.basicConfig(filename='bot.log', level=logging.INFO, encoding='utf-8')


def in_what_constellation(update, context):
    print('Вызвана комманда - /planet')

    user_text = update.message.text
    update.message.reply_text(f'Привет пользователь! Ты написал {user_text}')

    dt = datetime.datetime.today()
    user_dt = f'{dt.year}/{dt.month}/{dt.day}'

    # В переменную записывается планета указанная пользователем
    for planet in user_text.split():
        planet = planet.lower()
    print(f'Пользовательская планета: {planet}')

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
        print(constellation)
    except KeyError:
        print('Такой планеты нет')

    update.message.reply_text(
        f'Планета {planet} находится в созвездии {constellation}')


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
