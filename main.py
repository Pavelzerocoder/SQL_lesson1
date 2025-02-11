import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)""")

conn.commit()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Алексей', 30))  # (?, ?)
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Игорь', 25))  # (?, ?)

conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())


conn.close()