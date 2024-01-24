import bot.commands.utils.permissions as perms

class DatabaseManager():
    '''Singleton class for interacting with database'''
    
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance
    
    def getUserPermissions(self, userID):
        '''Get user permissions for the bot'''
        
        return perms.Permission.OWNER