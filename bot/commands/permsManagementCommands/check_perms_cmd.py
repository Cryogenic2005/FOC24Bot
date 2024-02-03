from bot.commands.utils.permissions import Permission, checkPermission
from bot.commands.utils.decorators import command
from database.databaseManager import DatabaseManager

@command(permission_level=Permission.MODERATOR, check_bot_status=False)
async def check_perms(update, context):
    '''
    Usage: /check_perms @[username]
    Example: /check_perms @ABCD123
    
    Checks the specified user's permission level
    
    Permission levels: User < Moderator < Admin < Owner
    '''
    
    username = context.args[0].strip('@')
    
    db = DatabaseManager()
    user_id = db.getUserIdByUsername(username)
    
    if user_id is None:
        await context.bot.sendMessage(
            chat_id = update.effective_chat.id,
            text = f"User @{username} has not registered with bot"
        )
        return
    
    user_perm = db.getUserPermissions(userID=user_id)
    await context.bot.sendMessage(
        chat_id = update.effective_chat.id,
        text = f"@{username} permission level: {user_perm}"
    )
    