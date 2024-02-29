from enum import Enum, auto

from database.databaseManager import DatabaseManager

class Permission(Enum):
    UNREGISTERED = 0 
    USER = 1
    MODERATOR = 2
    ADMIN = 3
    OWNER = 4
        
    
def checkPermission(user_id: int, permission_level: Permission, strict: bool = False) -> bool:
    """
    Check if a user is has permission level above the specified level 
    
    :param int userID: ID of the user to check permissions against
    :param Permission permissionLevel: The minimum permission level allowed, taken from the Permission enum
    :param bool strict: If True, equal permission level would still be considered invalid, defaults to False
    
    :return bool: True if the user has permission level above the specified level, False otherwise
    """
    
    if strict:
        return Permission[DatabaseManager().getUserPermissions(user_id)].value > \
            permission_level.value if user_id is not None else False
        
    return Permission[DatabaseManager().getUserPermissions(user_id)].value >= \
        permission_level.value if user_id is not None else False