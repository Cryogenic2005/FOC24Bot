from bot.commands.utils.permissions import Permission, checkPermission
from bot.commands.utils.decorators import command
from database.databaseManager import DatabaseManager

@command(permission_level=Permission.ADMIN, check_bot_status=False)
async def grant(update, context):
    '''
    Usage: /grant @[username] [permission-level]
    Example: /grant @ABCD123 moderator
    
    Grants the specified user the specified permission level
    Command executor must have permission level greater than the specified permission level
    
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
            text = "User has not registered with bot"
        )
        return
    
    if not checkPermission(userID=update.message.from_user.id, permission_level=Permission[permission]):
        await context.bot.sendMessage(
            chat_id = update.effective_chat.id,
            text = "You cannot grant users a permission level higher than or equal to your own permission levels."
        )
        return
    
    if checkPermission(userID=user_id, permission_level=Permission[permission]):
        await context.bot.sendMessage(
            chat_id = update.effective_chat.id,
            text = "User already has permission level higher than or equal to the specified permission level."
        )
        return
    
    db.updateUserPermissions(userID=user_id, permission=permission)
    await context.bot.sendMessage(
        chat_id = update.effective_chat.id,
        text = "User permission level has been updated successfully."
    )
    