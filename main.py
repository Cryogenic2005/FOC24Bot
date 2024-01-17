import os

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=f"Hello, {update.message.from_user.username}"
    )

if __name__ == "__main__":
    load_dotenv()
    
    app = ApplicationBuilder().token(os.getenv("BOT_API_TOKEN")).build()
    
    hello_handler = CommandHandler("hello", hello)
    app.add_handler(hello_handler)
    
    app.run_polling()    