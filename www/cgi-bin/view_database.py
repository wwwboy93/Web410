#!/usr/bin/python


import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
results = cursor.execute("SELECT * FROM user;")
print results.rowcount
for r in results:
    print r


results = cursor.execute("SELECT * FROM activity;")
print results.rowcount
for r in results:
    print r

results = cursor.execute("SELECT * FROM image;")
print results.rowcount
for r in results:
    print r

conn.close()