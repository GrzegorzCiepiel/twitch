import sqlite3

db = sqlite3.connect('twitch.db')
cursor = db.cursor()
cursor.execute('''
    SELECT DISTINCT game
    FROM stream;
    ''')

result = cursor.fetchall()
db.commit()
db.close()

print(result)
