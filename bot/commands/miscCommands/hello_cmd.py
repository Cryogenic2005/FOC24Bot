from bot.commands.utils.decorators import command

@command()
async def hello(update, context):
    '''Say hello to the user'''
    await context.bot.sendMessage(
        chat_id=update.effective_chat.id, 
        text=f"Hello, {update.message.from_user.username}"
    )