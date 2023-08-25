from telegram import Update
from telegram.ext import Updater, filters, ContextTypes
from telegram.ext import MessageHandler, CommandHandler, Application


# 替換為你的機器人令牌
TOKEN = "6538289312:AAHLHWTIlwqJ8CpeyX8XFW4rIZge9tgbem4"

# Commands
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Im a temporary test bot. I can repeat any thing you send in chat.")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Nothing I can help you now :( ")

async def swear_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FucK You")

#Response
def handle_response(text:str) -> str:
    return text   

async def handle_message(update:Update ,context:ContextTypes.DEFAULT_TYPE):
    
    message_type : str  = update.message.chat.type
    text : str = update.message.text
    
    response:str = handle_response(text)

    await update.message.reply_text(response)

#Error
async def error(update:Update ,context:ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting ...')

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('hello',swear_command))

    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=1)