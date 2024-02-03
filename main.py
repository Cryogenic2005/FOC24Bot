import os

from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv

from bot import handlers

if __name__ == "__main__":
    load_dotenv()
    
    app = ApplicationBuilder().token(os.getenv("BOT_API_TOKEN")).build()
    
    for handler in handlers:
        app.add_handler(handler)
    
    print("Bot is running")
    app.run_polling()
