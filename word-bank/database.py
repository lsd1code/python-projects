import sqlite3
from dataclasses import dataclass
import re

@dataclass
class Auth:
    database = 'word_bank.db'
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    def register(self) -> bool:
        while True:
            username = input('username: ')
            
            if len(username) < 3:
                print('Length of username must be more than 2 characters') 
                continue
            
            email = input('email address: ')
            
            if not re.match(self.pattern, email):
                print('enter a valid email address')
                continue
            
            pwd = input('password: ')
            
            if len(pwd) < 5:
                print('Length of password must be more than 5 characters') 
                continue
        
            break
        
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
                
        cursor.execute(
            'INSERT INTO users VALUES (?, ?, ?)', (username, email, pwd)
        )
        
        connection.commit()
        connection.close()
        
        return True
        
        
    def login(self) -> bool:
        while True:
            email = input('email address: ')
            
            if not re.match(self.pattern, email):
                print('enter a valid email address')
                continue
            
            pwd = input('password: ')
            
            if len(pwd) < 5:
                print('Length of password must be more than 5 characters') 
                continue
            
            break
        
        conn = sqlite3.connect('word_bank.db')
        cursor = conn.cursor()
        
        q = cursor.execute(f'SELECT password FROM users WHERE email LIKE "{email}"')
        
        if not q:
            return
        
        password = q.fetchone()[0]
        
        return password == pwd