import random
import string
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('Tokens.db', check_same_thread=False)
cursor = conn.cursor()

# Create the table to store the tokens (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tokens (
    token_text text
)
''')
conn.commit()


class ApiToken:
    
    def generate_token():
        # Generate random alpha-numeric string with length 50
        token = ''.join(random.choices(string.ascii_letters+string.digits, k=40))
        result = cursor.execute("SELECT * FROM Tokens WHERE token_text=?", (token,)).fetchone()
        
        # Check whether the token already exist or not
        while result:
            token = ''.join(random.choices(string.ascii_letters+string.digits, k=50))
            result = cursor.execute("SELECT * FROM Tokens WHERE token_text=?", (token,)).fetchone()
        
        cursor.execute("INSERT INTO Tokens (token_text) VALUES (?)", (token,))
        conn.commit()

        return token
    
    
    def is_valid_token(token_to_check):
        cursor.execute("SELECT * FROM Tokens WHERE token_text=?", (token_to_check,))
        result = cursor.fetchone()

        return True if result else False    

