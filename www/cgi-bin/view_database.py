#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('web410.db')
cursor = conn.cursor()
results = cursor.execute("SELECT * FROM user;")
print results.rowcount
for r in results:
    print r
conn.close()