from bot.commands.utils.decorators import command

@command()
async def help(update, context):
    commandHelp = ''' \
    /hello - Say hello to user\n \
    /help - List of bot commands\n \
    /passOn - To be implemented\n \
    /guessingGame - To be implemented\n \
    '''
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=commandHelp
    )