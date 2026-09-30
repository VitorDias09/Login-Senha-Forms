import sqlite3 
from database.db import get_db_connection  

class FormularioModel:
    
    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (int(user_id), nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except (sqlite3.IntegrityError, ValueError):
            return None  
        finally:
            conn.close()  

    @staticmethod
    def find_by_id(formulario_id):
        conn = get_db_connection()
        formulario = conn.execute(
            '''SELECT id, user_id, nome, email, data_nascimento, cpf, genero 
               FROM formularios 
               WHERE id = ?''',
            (formulario_id,)
        ).fetchone()
        conn.close()
        if formulario:
            return dict(formulario)
        return None

    @staticmethod
    def update_formulario(formulario_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            cursor = conn.execute(
                '''UPDATE formularios 
                   SET nome = ?, email = ?, data_nascimento = ?, cpf = ?, genero = ?
                   WHERE id = ?''',
                (nome, email, data_nascimento, cpf, genero, formulario_id)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception:
            return False
        finally:
            conn.close()

    @staticmethod
    def delete_formulario(formulario_id):
        conn = get_db_connection()
        try:
            cursor = conn.execute('DELETE FROM formularios WHERE id = ?', (formulario_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception:
            return False
        finally:
            conn.close()
