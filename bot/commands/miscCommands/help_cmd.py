import bot.commands
from bot.commands.utils.decorators import command
from bot.commands.utils.permissions import Permission

@command(permission_level=Permission.UNREGISTERED, check_bot_status=False)
async def help(update, context):
    '''
    Descriptions of all bot commands
    '''
    
    help_text = ""
    for command in bot.commands.command_list:
        help_text += "/{}: {}\n\n".format(command.__name__, command.__doc__.rstrip())
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=help_text
    )