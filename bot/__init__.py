from telegram.ext import CommandHandler, filters

from .commands import commandList

handlers = []

for command in commandList:
    handlers.append(CommandHandler(
        command=command.__name__,
        callback=command,
        filters=filters.COMMAND & ~filters.UpdateType.EDITED_MESSAGE
    ))
    
__all__ = ['handlers']