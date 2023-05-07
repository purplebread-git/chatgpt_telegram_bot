import sqlite3
conn = sqlite3.connect('db.db')
cursor = conn.cursor()
cursor.execute("SELECT chat_id FROM user")
results = cursor.fetchall()

print(results[0][0])

