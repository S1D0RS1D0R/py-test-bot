import sqlite3

class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def adduser(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall
            return bool(len(result))
    
    def setnickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'nickname' = ? WHERE 'user_id' = ?", (nickname, user_id,))
    
    def get_sign_up(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?",(user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
                return signup
        
    def setsignup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'signup' = ? WHERE 'user_id' = ?", (signup, user_id,))