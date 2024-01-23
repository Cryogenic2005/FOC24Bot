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
            
    def getDatabase(self):
        if DatabaseManager.instance is None:
            DatabaseManager.instance = DatabaseManager._DatabaseManager()
            
        return DatabaseManager.instance