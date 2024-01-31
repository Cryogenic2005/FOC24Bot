import os
import sqlite3

class DatabaseManager():
    '''Singleton class for interacting with database'''
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if DatabaseManager._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if DatabaseManager._initialized:
            return
        
        self.connection = sqlite3.connect(os.path.join("database","database.db"))
        self.cursor = self.connection.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(username, user_id, permission)")
    
    def registerUser(
            self,
            username: str,
            user_id: int,
            permission = "USER"
        ) -> None:
        
        self.cursor.execute("SELECT user_id FROM users")
        if (user_id,) in self.cursor.fetchall():
            return
        
        self.cursor.execute("INSERT INTO users VALUES (?, ?, ?)",
            (username, user_id, permission)
        )
        
        self.connection.commit()
        
    def printDB(self):
        self.cursor.execute("SELECT * FROM users")
        print(self.cursor.fetchall())
    
    def getUserPermissions(self, userID):
        '''Get user permissions for the bot'''
        
        self.cursor.execute("SELECT permission FROM users WHERE user_id=?", (userID, ))
        permLevel = self.cursor.fetchall()[0][0]
        print(permLevel)
        return permLevel
        