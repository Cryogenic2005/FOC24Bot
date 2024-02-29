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
    
    try:
        group_name = context.args[0]
    except IndexError:
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id, 
            text=f"Missing arguments. Please check the correct usage of the command below."
        )
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id, 
            text=group.__doc__
        )
        return
    
    db = DatabaseManager()
    
    img_list = db.getImagesByGroupId(group_name)
    
    if img_list is None:
        await context.bot.sendMessage(
            chat_id=update.effective_chat.id, 
            text=f"No such group with the name {group_name}"
        )
        return
    
    for img_name, difficulty in img_list:
        img_path = os.path.join("game", "images", img_name)
        
        if not os.path.exists(img_path):
            await context.bot.sendMessage(
                update.effective_chat.id,
                text=f"Image {img_name} has not been added to the game yet"
            )
        else:
            await context.bot.sendPhoto(
                update.effective_chat.id, 
                photo=img_path, 
                caption="Difficulty: {}".format(Difficulty(difficulty).name)
            )
    
    