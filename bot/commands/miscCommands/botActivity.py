import logging

from bot.botController import BotStatus
from bot.commands.utils.decorators import command
from bot.commands.utils.permissions import Permission

logger = logging.getLogger(__name__)

@command(permission_level=Permission.ADMIN, check_bot_status=False)
async def enable(update, context):
    '''
    Set the bot status to be active
    '''
    
    logger.info(f"User {update.message.from_user.username} has enabled the bot")
    
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
    
@command(permission_level=Permission.ADMIN, check_bot_status=False)
async def disable(update, context):
    '''
    Set the bot status to be inactive
    '''
    
    logger.info(f"User {update.message.from_user.username} has disabled the bot")
    
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