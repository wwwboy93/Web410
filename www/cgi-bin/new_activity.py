#!/usr/bin/python

import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string

def create_new_activity(username, activityname, activitycontent):
    return 0
    # conn = sqlite3.connect('users.db')
    # cursor = conn.cursor()
    # results = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    # if results is None:
    #     conn.close()
    #     return -1
    # conn.close()
    # if transid == results[5]:
    #     return 0
    # else:
    #     return -1

# For backend testing only:
# create_new_activity("asd", "asd")

cgitb.enable()

print "Content-type: application/json"
print 

activity_info = cgi.FieldStorage()
username = activity_info['username'].value
activityname = activity_info['activityname'].value
activitycontent = activity_info['activitycontent'].value
# transid = activity_info['transid'].value
response = {}

res = create_new_activity(username, activityname, activitycontent)
if res == -1:
    response['response'] = -1
else:
    response['response'] = 0
    
print json.dumps(response)






