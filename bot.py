from dotenv import load_dotenv
import logging
import os
from handlers import start
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
