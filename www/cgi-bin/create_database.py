#!C:\Python27\python.exe


import sqlite3
import hashlib
import datetime
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS user')
cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', username varchar(100), password varchar(100), email varchar(100), date varchar(100))')
conn.commit()

date = str(datetime.datetime.now())
hasher = hashlib.md5()
hasher.update('123123')
hasher.update(date)
encrypted = hasher.hexdigest()
cursor.execute("INSERT INTO user(id, username, password, date) VALUES('1','admin','%s','%s');"
               % (encrypted, date))
cursor.execute("INSERT INTO user(id, username, password, date) VALUES('2','fucksqlite','%s','%s');"
               % (encrypted, date))
# cursor.execute("DROP TABLE user")
conn.commit()
conn.close()


