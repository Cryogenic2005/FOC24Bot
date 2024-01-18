from telegram import Update
from telegram.ext import ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=f"Hello, {update.message.from_user.username}"
    )