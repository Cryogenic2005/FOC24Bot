import functools

from telegram.ext import CallbackContext

from bot.botController import BotStatus
from database.database import DatabaseManager
from .permissions import Permission, checkPermission

def command(permissionLevel = Permission.USER):
    def commandDecorator(func):
        @functools.wraps(func)
        async def wrapper(update, context: CallbackContext):
            
            # Checks if bot is active
            if not BotStatus.isBotActive():
                await context.bot.sendMessage("The bot is not currently active")
            
            # Checks if user has permission to execute the command
            if not checkPermission(
                userID=context.user_data.get("user_id", None), 
                permissionLevel=permissionLevel
            ):
                await context.bot.sendMessage("User {} is not allowed to execute the command".format(
                    context.user_data.get("username", '(Unable to find user)')
                ))
            
            await func(update, context)
        return wrapper
    return commandDecorator