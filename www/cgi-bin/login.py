#!/usr/bin/python


import cgitb
import cgi
import sqlite3
import hashlib
import json


def user_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    results = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    if results is None:
        return -1
    date = None
    password_f = results[2]
    date = results[4]

    conn.close()
    hasher = hashlib.md5()
    hasher.update(password)
    hasher.update(date)
    encrypted = hasher.hexdigest()
    if encrypted != password_f:
        return -1

    return 0

cgitb.enable()


print "Content-type: application/json"
print 

user_info = cgi.FieldStorage()

username = user_info['username'].value
password = user_info['password'].value

response = {}

if user_login(username, password) == -1:
    # print '<h1>Wrong username or password'
    response['response'] = -1
else:
    response['response'] = 0
    
print json.dumps(response)






