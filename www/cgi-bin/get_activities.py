#!/usr/bin/python

import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string

cgitb.enable()

# get all activities from activity table
def get_all_activities():
    activities_json = []
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    activities = cursor.execute("SELECT title, username, reply_times, activity.create_time FROM activity, user "
                                "where activity.user_id = user.user_id");
    if activities is None:
        conn.close()
        return -1

    for activity in activities:
        activity_json = { }
        # print activity
        activity_json["title"] = str(activity[0])
        activity_json["username"] = str(activity[1])
        activity_json["reply_times"] = str(activity[2])
        activity_json["create_time"] = str(activity[3])[0:-7]
        # print activity_json
        activities_json += [activity_json]

    conn.close()
    return activities_json




print "Content-type: application/json"
print

activities_json = {}
fetch_type = cgi.FieldStorage()['type'].value
if fetch_type == "all":
    activities_json['activity'] = get_all_activities()

print json.dumps(activities_json)






    




