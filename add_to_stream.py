import sqlite3
import csv

db = sqlite3.connect('twitch.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE chat ('time', 'device_id', 'login', 'channel', 'country', 'player', 'game');
    ''')
with open('chat.csv','r') as data1:
    dr = csv.DictReader(data1)
    to_db = [(i['time'],
              i['device_id'],
              i['login'],
              i['channel'],
              i['country'],
              i['player'],
              i['game']) for i in dr]
cursor.executemany('''
        INSERT INTO chat ('time', 'device_id', 'login', 'channel', 'country', 'player', 'game')
        VALUES (?,?,?,?,?,?,?);''', to_db)

db.commit()
db.close()
