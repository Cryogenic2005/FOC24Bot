import os
import sqlite3

from game.group_id_enum import GroupName

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
        
        self._table_names = ["users", "images"]
        self._cursor.execute("CREATE TABLE IF NOT EXISTS users(username, user_id, permission)")
        self._cursor.execute("CREATE TABLE IF NOT EXISTS images(name, group_id, difficulty, img_name)")
    
    # ---------------------- Miscellaneous Methods ----------------------------
    
    def printDB(self):
        self._cursor.execute("SELECT * FROM users")
        print(self._cursor.fetchall())
        
    def countTable(self, table_name):
        if table_name not in self._table_names:
            return 0
        
        self._cursor.execute("SELECT COUNT(*)")
        return self._cursor.fetchall()
        
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
    
    def getUserIdByUsername(self, username: str):
        '''
        Gets user id by username
        
        :param str username: User's username
        :return: Returns user id if in database, otherwise returns None 
        '''
        
        self._cursor.execute("SELECT user_id FROM users WHERE username=?", (username, ))
        query_result = self._cursor.fetchall()
        
        if query_result == []:
            return None
        
        return query_result[0][0]
    
    def getUserPermissions(self, userID):
        '''Get user permissions for the bot'''
        
        self._cursor.execute("SELECT permission FROM users WHERE user_id=?", (userID, ))
        query_result = self._cursor.fetchall()
        
        if query_result == []:
            return "UNREGISTERED"
        
        return query_result[0][0]
    
    def updateUserPermissions(self, userID: int, permission: str) -> bool:
        '''
        Update user permissions for the bot
        
        :param int userID: User Id
        :param str permission: Permission level to update user to
        :return bool: False user is not in database, True if update was successful 
        '''
        
        self._cursor.execute("SELECT permission FROM users WHERE user_id=?", (userID,))
        
        query_result = self._cursor.fetchall()
        if query_result == []:
            return False
        
        self._cursor.execute("UPDATE users SET permission=? WHERE user_id=?", (permission, userID))
        return True
    
    # ---------------------- Game Management Methods -----------------------------------
    
    def insertImage(self, name: str, group_id: int, difficulty: int):
        self._cursor.execute("INSERT INTO images VALUES (?, ?, ?, ?)",
            (name, group_id, difficulty, f"{name}.png")
        )
        
        self._connection.commit()
        
    def getImagesByGroupId(self, group_name: str):
        if not hasattr(GroupName, group_name):
            return None
        
        group_id = GroupName[group_name].value
        
        self._cursor.execute("SELECT img_name, difficulty FROM images WHERE group_id=?", (group_id, ))
        
        return self._cursor.fetchall()
        