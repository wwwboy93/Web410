#!C:\Python27\python.exe

import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string

def user_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    results = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    if results is None:
        conn.close()
        return -1
    date = None
    password_f = results[2]
    date = results[4]

    
    hasher = hashlib.md5()
    hasher.update(password)
    hasher.update(date)
    encrypted = hasher.hexdigest()
    if encrypted != password_f:
        conn.close()
        return -1

    transID = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    cursor.execute("UPDATE user SET transID = '%s' WHERE username = '%s';" % (transID, username))
    # results2 = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    # print results2
    conn.commit()
    conn.close()
    return transID

# For backend testing only:
# user_login("asd", "asd")

cgitb.enable()


print "Content-type: application/json"
print 

user_info = cgi.FieldStorage()

username = user_info['username'].value
password = user_info['password'].value

response = {}

res = user_login(username, password)
if res == -1:
    # print '<h1>Wrong username or password'
    response['response'] = -1
else:
    response['response'] = res
    
print json.dumps(response)






