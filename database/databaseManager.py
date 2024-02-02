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
        
        self._connection = sqlite3.connect(os.path.join("database","database.db"))
        self._cursor = self._connection.cursor()
        
        self._cursor.execute("CREATE TABLE IF NOT EXISTS users(username, user_id, permission)")
    
    # ---------------------- Miscellaneous Methods ----------------------------
    
    def printDB(self):
        self._cursor.execute("SELECT * FROM users")
        print(self._cursor.fetchall())
        
        
    # ---------------------- User Management Methods --------------------------
    
    def registerUser(
            self,
            username: str,
            user_id: int,
            permission = "USER"
        ) -> None:
        
        self._cursor.execute("SELECT user_id FROM users")
        if (user_id,) in self._cursor.fetchall():
            return
        
        self._cursor.execute("INSERT INTO users VALUES (?, ?, ?)",
            (username, user_id, permission)
        )
        
        self._connection.commit()
    
    def getUserPermissions(self, userID):
        '''Get user permissions for the bot'''
        
        self._cursor.execute("SELECT permission FROM users WHERE user_id=?", (userID, ))
        query_result = self._cursor.fetchall()
        
        if query_result == []:
            return "UNREGISTERED"
        
        return query_result[0][0]