import logging

from bot.commands.utils.decorators import command
from bot.commands.utils.permissions import Permission
from database.databaseManager import DatabaseManager

logger = logging.getLogger(__name__)

@command(permission_level=Permission.UNREGISTERED)
async def start(update, context):
    '''
    Starts interaction with bot
    Registers user in bot database for verifying permission levels
    '''
    
    db = DatabaseManager()
    
    if db.getUserPermissions(userID=update.message.from_user.id) != "UNREGISTERED":
        logger.info(f"User {update.message.from_user.username} is already registered.") 
    else:
        logger.info(f"User {update.message.from_user.username} registered with bot.") 
        
        db.registerUser(
            username=update.message.from_user.username,
            user_id=update.message.from_user.id,
            permission=Permission.USER.name
        )
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text="Hello @{}".format(update.message.from_user.username)
    )