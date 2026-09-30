import sqlite3  
from database.db import get_db_connection  

class UserModel:
    
    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()  
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()  
        if user:
            return dict(user)
        return None  

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()  
        # Nunca seleciona a senha ou o hash da senha por segurança
        user = conn.execute('SELECT id, username FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()  
        if user:
            return dict(user)
        return None

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

    @staticmethod
    def update_user(user_id, username):
        conn = get_db_connection()  
        try:
            cursor = conn.execute('UPDATE users SET username = ? WHERE id = ?', (username, user_id))
            conn.commit()  
            return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()  
        try:
            # Exclui formulários associados ao usuário para manter integridade referencial
            conn.execute('DELETE FROM formularios WHERE user_id = ?', (user_id,))
            cursor = conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()  
            return cursor.rowcount > 0
        finally:
            conn.close()  
