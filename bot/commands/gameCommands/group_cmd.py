import os

from database.databaseManager import DatabaseManager
from bot.commands.utils.decorators import command
from game.difficulty_enum import Difficulty

@command()
async def group(update, context):
    '''
    Usage: /group [group-id]
    Example: /group ABCDEF
    
    Returns a list of images for the group with that id
    '''
    
    group_name = context.args[0]
    
    db = DatabaseManager()
    
    imgList = db.getImagesByGroupId(group_name)
    
    if imgList is None:
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id, 
            text=f"No such group with the name {group_name}"
        )
        return
    
    for imgName, difficulty in imgList:
        imgPath = os.path.join("game", "images", imgName)
        
        if not os.path.exists(imgPath):
            await context.bot.sendMessage(
                update.effective_chat.id,
                text=f"Image {imgName} has not been added to the game yet"
            )
        else:
            await context.bot.sendPhoto(
                update.effective_chat.id, 
                photo=imgPath, 
                caption="Difficulty: {}".format(Difficulty(difficulty).name)
            )
    
    