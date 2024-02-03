from telegram.ext import CommandHandler, filters

from .commands import command_list

handlers = []

for command in command_list:
    handlers.append(CommandHandler(
        command=command.__name__,
        callback=command,
        filters=filters.COMMAND & ~filters.UpdateType.EDITED_MESSAGE
    ))
    
__all__ = ['handlers']