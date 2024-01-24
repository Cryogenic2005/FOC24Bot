from telegram.ext import CommandHandler

from .commands import commandList

handlers = []

for command in commandList:
    handlers.append(CommandHandler(command=command.__name__, callback=command))
    
__all__ = ['handlers']