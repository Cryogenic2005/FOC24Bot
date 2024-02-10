import functools
import logging

from bot.botController import BotStatus
from .permissions import Permission, checkPermission

logger = logging.getLogger(__name__)

def command(permission_level = Permission.USER, check_bot_status = True):
    '''
    Mandatory decorator for all bot commands
    
    :param Permission permissionLevel: Minimum permission level of user to execute the command, defaults to Permission.USER
    :param bool checkBotStatus: If True, bot must be active to execute the command, otherwise command can always be executed, defaults to True
    '''
    
    def commandDecorator(func):
        @functools.wraps(func)
        async def wrapper(update, context):
            logger.info(f"User {update.message.from_user.username} executed command /{func.__name__}")
            
            # Checks if bot is active
            if check_bot_status and not BotStatus.isBotActive():
                await context.bot.sendMessage(
                    chat_id=update.effective_chat.id,
                    text="The bot is not currently active"
                )
                return
            
            # Checks if user has permission to execute the command
            if not checkPermission(
                userID=update.message.from_user.id, 
                permission_level=permission_level
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