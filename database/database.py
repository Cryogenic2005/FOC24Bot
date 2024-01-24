import bot.commands.utils.permissions as perms

class DatabaseManager():
    '''Singleton class for interacting with database'''
    class _DatabaseManager():
        def getUserPermissions(self, userID):
            '''Get user permissions for the bot'''
            
            pass
    
    instance = None
    
    def __init__(self):
        if DatabaseManager.instance is None:
            DatabaseManager.instance = DatabaseManager._DatabaseManager()
        
    @staticmethod
    def getDatabase():
        if DatabaseManager.instance is None:
            DatabaseManager.instance = DatabaseManager._DatabaseManager()
            
        return DatabaseManager.instance