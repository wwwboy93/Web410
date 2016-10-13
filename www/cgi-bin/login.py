#!C:\Python27\python


import cgitb
import cgi
import sqlite3
import hashlib

cgitb.enable()

user_form = cgi.FieldStorage()

print 'Content-Type: text/html'
print

print '''<html>
  <head>
    <title>Welcome aboard</title>

    <style type="text/css">
      h1 {
          font-size: 30px;
          font-family: monospace;
      }


    </style>

  </head>
  <body>
'''


def user_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user where username = '%s';" % username)
    date = None
    if cursor.rowcount == 0:
        return -1
    results = cursor.fetchall()
    for row in results:
        password_f = row[2]
        date = row[4]

    conn.close()
    hasher = hashlib.md5()
    hasher.update(password)
    hasher.update(date)
    encrypted = hasher.hexdigest()
    if encrypted != password_f:
        return -1

    return 0


username = user_form['username'].value
password = user_form['password'].value

if user_login(username, password) == -1:
    print '<h1>Wrong username or password'
else:
    print '<h1>welcome, '+username

print '''
  </body>
</html>

'''





