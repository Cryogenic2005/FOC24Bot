import os
import importlib

from typing import List, Callable, Coroutine

from telegram import Update
from telegram.ext import CallbackContext

def getFuncFromModule(
    funcName: str, 
    moduleName: str
) -> Callable[[Update, CallbackContext], Coroutine[None, None, None]]:
    
    """Returns a function with the given name from the given module"""
    
    try:
        module = importlib.import_module(name=moduleName)
        
        function = getattr(module, funcName)
        
        if callable(function):
            return function
        else:
            raise AttributeError(f"{funcName} in {moduleName} is not a function")
        
    except ImportError as e:
        raise ImportError(f"Module {moduleName} was not found") from e
    except AttributeError as e:
        raise AttributeError(f"Function {funcName} in {moduleName} was not found") from e
            
def getAllCommands() -> List[Callable[[Update, CallbackContext], Coroutine[None, None, None]]]:
    """Returns a list of all commands for the bot"""
    
    commands = [dir.name for dir in os.scandir("commands") if dir.is_dir() and dir.name != "__pycache__"]
    
    for command in commands:
        # Module and function name is the same as command name
        module = f"commands.{command}.{command}"
        function = command
        
        yield getFuncFromModule(moduleName=module, funcName=function)

if __name__ == "__main__":
    for command in getAllCommands():
        print("{}: {}".format(command.__name__, command))