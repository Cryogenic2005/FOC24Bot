from enum import Enum, auto

from database.database import DatabaseManager

class Permission(Enum):
    USER = 1
    MODERATOR = 2
    ADMIN = 3
    OWNER = 4
    
def checkPermission(userID, permissionLevel):
    """
    Check if a user is allowed to execute a given command
    
    :param userID: ID of the user to check permissions against
    :param permissionLevel: The minimum permission level allowed, taken from the Permission enum
    
    :return: True if the user is allowed to execute the command, False otherwise
    """
    return DatabaseManager.getUserPermissions(userID) >= permissionLevel if userID is not None else False