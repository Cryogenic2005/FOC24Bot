import logging

from bot.commands.utils.decorators import command
from bot.commands.utils.permissions import Permission
from database.databaseManager import DatabaseManager

logger = logging.getLogger(__name__)

@command(permission_level=Permission.UNREGISTERED)
async def register(update, context):
    '''
    Registers user in bot database
    '''
    
    db = DatabaseManager()
    if db.getUserIdByUsername(update.message.from_user.username) is not None:
        logger.info(f"User {update.message.from_user.username} already registered with bot")
        
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id,
            text="User already registered with bot."
        )
        return
    
    logger.info(f"User {update.message.from_user.username} registered with bot")
    
    db.registerUser(
        username=update.message.from_user.username,
        user_id=update.message.from_user.id,
        permission=Permission.USER.name
    )
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text="@{} registered successfully".format(update.message.from_user.username)
    )