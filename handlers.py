from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_messsage(
        chat_id=update.effective_chat.id, text="Welcome to the Unifarm's staking bot!!"
    )
