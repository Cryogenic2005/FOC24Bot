from bot.commands.utils.decorators import command
from bot.commands.utils.permissions import Permission
from database.databaseManager import DatabaseManager

@command()
async def start(update, context):
    '''Starts interaction with bot and register user in bot database'''
    
    db = DatabaseManager()
    db.registerUser(
        username=update.message.from_user.username,
        user_id=update.message.from_user.id,
        permission=Permission.USER.name
    )
    
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text="Hello @{}".format(update.message.from_user.username)
    )