#!/usr/bin/python


import sqlite3
import hashlib
import datetime
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# create user information table
cursor.execute('DROP TABLE IF EXISTS user')
cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', username varchar(100), password varchar(100), email varchar(100), date varchar(100)'
               ', transid varchar(100))')

# create activity table
cursor.execute('DROP TABLE IF EXISTS activity')
cursor.execute('CREATE TABLE IF NOT EXISTS activity(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', user_id INTEGER NOT NULL, title varchar(100), content varchar(1000), create_time varchar(100)'
               ', category varchar(30), area varchar(30))')

# create comment table
cursor.execute('DROP TABLE IF EXISTS comment')
cursor.execute('CREATE TABLE IF NOT EXISTS comment(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', user_id INTEGER, activity_id INTEGER, content varchar(1000), time varchar(100), replier_id INTEGER)')

# create participants table
cursor.execute('DROP TABLE IF EXISTS participants')
cursor.execute('CREATE TABLE IF NOT EXISTS participants(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', activity_id INTEGER, user_id INTEGER)')

# create image table
cursor.execute('DROP TABLE IF EXISTS image')
cursor.execute('CREATE TABLE IF NOT EXISTS image(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', path varchar(256), activity_id INTEGER, comment_id INTEGER)')

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


