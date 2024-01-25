import functools

from bot.botController import BotStatus
from .permissions import Permission, checkPermission

def command(permissionLevel = Permission.USER, checkBotStatus = True):
    '''
    Mandatory decorator for all bot commands
    
    :param Permission permissionLevel: Minimum permission level of user to execute the command, defaults to Permission.USER
    :param bool checkBotStatus: If True, bot must be active to execute the command, otherwise command can always be executed, defaults to True
    '''
    
    def commandDecorator(func):
        @functools.wraps(func)
        async def wrapper(update, context):
            
            # Checks if bot is active
            if checkBotStatus and not BotStatus.isBotActive():
                await context.bot.sendMessage(
                    chat_id=update.effective_chat.id,
                    text="The bot is not currently active"
                )
                return
            
            # Checks if user has permission to execute the command
            if not checkPermission(
                userID=update.message.from_user.id, 
                permissionLevel=permissionLevel
            ):
                await context.bot.sendMessage(
                    chat_id=update.effective_chat.id,
                    text="User {} is not allowed to execute the command".format(
                        update.message.from_user.username
                    )
                )
                return
            
            # Execute the command if passed all checks
            await func(update, context)
        return wrapper
    return commandDecorator