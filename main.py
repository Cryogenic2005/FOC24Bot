import os

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv

import bot.commands

if __name__ == "__main__":
    load_dotenv()
    
    app = ApplicationBuilder().token(os.getenv("BOT_API_TOKEN")).build()
    
    for command in bot.commands.getAllCommands():
        command_handler = CommandHandler(command.__name__, command)
        app.add_handler(command_handler)
    
    print("Bot is running")
    app.run_polling()    