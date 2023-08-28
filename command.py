from telegram import Update
from telegram.ext import Updater, filters, ContextTypes

# Command handlers
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Im a temporary test bot. I can repeat any thing you send in chat.")

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi Nothing I can help you now :( ")

async def swear_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FucK You")