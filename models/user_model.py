import sqlite3  
from database.db import get_db_connection  

class UserModel:
    
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()  
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()  
        return user  

    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()  
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  

