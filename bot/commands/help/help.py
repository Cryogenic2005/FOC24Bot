from telegram import Update
from telegram.ext import ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commandHelp = '''
    /hello - Say hello to user
    /help - List of bot commands
    /passOn - To be implemented
    /guessingGame - To be implemented
    '''
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=commandHelp
    )