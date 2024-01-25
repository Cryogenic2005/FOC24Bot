import bot.commands
from bot.commands.utils.decorators import command

@command(checkBotStatus=False)
async def help(update, context):
    '''Descriptions of all bot commands'''
    
    commandHelp = ""
    for command in bot.commands.commandList:
        commandHelp += "/{} - {}\n".format(command.__name__, command.__doc__)
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=commandHelp
    )