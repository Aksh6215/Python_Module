import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

# Create Table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER)
               ''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES ('ALice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
conn.commit()

# Query the data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)