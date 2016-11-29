#!C:\Python27\python.exe



import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string

print "Content-type: application/json"
print 

def profile(username):
    conn1 = sqlite3.connect('hangout.db')
    cursor1 = conn1.cursor()
    results1 = cursor1.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    conn1.close()
    if results1 is None:
        return -1
    else:
        return results1[3]
         


cgitb.enable()



user_info = cgi.FieldStorage()

username = user_info['username'].value

response = {}

res = profile(username)
if res == -1:
    response['response'] = -1
else:
    response['response'] = res
    
print json.dumps(response)






