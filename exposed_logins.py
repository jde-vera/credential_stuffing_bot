import sqlite3

connection = sqlite3.connect('logins.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT UNIQUE NOT NULL
    )
''')
connection.commit()

cursor.execute('SELECT * FROM users;')
if len(cursor.fetchall()) == 0:
    logins = [('alice','Password123!'),
            ('bob.smith','qwertyuiop'),
            ('charlie1985','12345678'),
            ('david','letmein'),
            ('eve_admin','admin1234'),
            ('frank.jones','Welcome1'),
            ('grace1990','summer2020'),
            ('harry','Passw0rd!'),
            ('irene99','iloveyou'),
            ('jane','janedoe')]

    cursor.executemany('''
        INSERT INTO users (username,password) VALUES (?,?)

    ''',logins)

    connection.commit()

def get_login():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()