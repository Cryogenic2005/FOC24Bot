from bot.botController import BotStatus
from bot.commands.utils.decorators import command
from bot.commands.utils.permissions import Permission

@command(permissionLevel=Permission.ADMIN, checkBotStatus=False)
async def start(update, context):
    if BotStatus.isBotActive():
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id,
            text="Bot is already active!"
        )
    else:
        BotStatus.setBotStatus(BotStatus.ACTIVE)
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id,
            text="Bot is now active"
        )
    
@command(permissionLevel=Permission.ADMIN, checkBotStatus=False)
async def stop(update, context):
    if not BotStatus.isBotActive():
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id,
            text="Bot is already inactive!"
        )
    else:
        BotStatus.setBotStatus(BotStatus.INACTIVE)
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id,
            text="Bot is now inactive"
        )