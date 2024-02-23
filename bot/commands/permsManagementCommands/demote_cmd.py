import logging

from bot.commands.utils.permissions import Permission, checkPermission
from bot.commands.utils.decorators import command
from database.databaseManager import DatabaseManager

logger = logging.getLogger(__name__)

@command(permission_level=Permission.ADMIN, check_bot_status=False)
async def demote(update, context):
    '''
    Usage: /demote @[username] [permission-level]
    Example: /demote @ABCD123 user
    
    Demotes the specified user to the specified permission level
    Command executor must have permission level greater than the specified user's permission level
    
    Permission levels: User < Moderator < Admin < Owner
    '''
    
    username = context.args[0].strip('@')
    permission = context.args[1].upper()
    
    db = DatabaseManager()
    user_id = db.getUserIdByUsername(username)
    
    if not hasattr(Permission, permission) or permission == "UNREGISTERED":
        await context.bot.sendMessage(
            chat_id = update.effective_chat.id,
            text = "Invalid permission level specified"
        )
        return
    
    if user_id is None:
        await context.bot.sendMessage(
            chat_id = update.effective_chat.id,
            text = f"User @{username} has not registered with bot"
        )
        return
    
    user_perm = db.getUserPermissions(userID=user_id)
    
    if not checkPermission(
        userID=update.message.from_user.id, 
        permission_level=Permission[user_perm],
        strict=True
    ):
        await context.bot.sendMessage(
            chat_id = update.effective_chat.id,
            text = "You cannot demote users with permission levels higher than or equal to your own permission levels."
        )
        return
    
    if not checkPermission(userID=user_id, permission_level=Permission[permission]):
        await context.bot.sendMessage(
            chat_id = update.effective_chat.id,
            text = "You cannot demote users to permission levels higher than or equal their current permission levels."
        )
        return
    
    logger.info("Demoted user {} to {}".format(user_id, permission))
    
    db.updateUserPermissions(userID=user_id, permission=permission)
    await context.bot.sendMessage(
        chat_id = update.effective_chat.id,
        text = "User permission level has been updated successfully."
    )
    