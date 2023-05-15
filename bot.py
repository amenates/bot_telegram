import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings as settings

logging.basicConfig(filename='bot.log', level=logging.INFO, encoding='utf-8')


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! Ты вызвал команду /start')
    print(update)


def talk_to_me(update, context):
    text = update.message.text
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
