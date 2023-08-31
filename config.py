import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
API_TOKEN = os.getenv("API_TOKEN")