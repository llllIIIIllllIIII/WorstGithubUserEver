from telegram import Update
from telegram.ext import Updater, filters, ContextTypes
from telegram.ext import MessageHandler, CommandHandler, Application
from config import BOT_TOKEN
from command import *
from handler import handle_message ,error



if __name__ == '__main__':
    print('Starting ...')

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('hello',swear_command))
    app.add_handler(CommandHandler('pic',pic_commnad))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=1)