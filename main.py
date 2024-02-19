import sqlite3
import csv

db = sqlite3.connect('twitch.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE stream (
        'time', 'device_id', 'login', 'channel', 'country', 'player', 'game', 'stream_format', 'subscriber');
        ''')
with open('stream.csv','r') as data:
    dr = csv.DictReader(data)
    to_db = [(i['time'],
              i['device_id'],
              i['login'],
              i['channel'],
              i['country'],
              i['player'],
              i['game'],
              i['stream_format'],
              i['subscriber']) for i in dr]

cursor.executemany('''
    INSERT INTO stream ('time', 'device_id', 'login', 'channel', 'country', 'player', 'game', 'stream_format',
     'subscriber')
    VALUES (?,?,?,?,?,?,?,?,?);''', to_db)

db.commit()
db.close()



