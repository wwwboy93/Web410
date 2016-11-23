#!C:\Python27\python.exe



import cgitb
import cgi
import sqlite3
import hashlib
import datetime

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


def insert_user(username, password, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    date = str(datetime.datetime.now())
    cursor.execute("SELECT * FROM user where username = '%s'" % (username))
    if cursor.fetchone() is not None:
        return -1
    hasher = hashlib.md5()
    hasher.update(password)
    hasher.update(date)
    encrypted = hasher.hexdigest()

    cursor.execute("INSERT INTO user(username, password, email, date)"
                   "VALUES('%s','%s','%s','%s');" % (username, encrypted, email, date))
    conn.commit()
    conn.close()
    return 0


username = user_form['username'].value
password = user_form['password'].value
email = user_form['email'].value

if insert_user(username, password, email) == -1:
    print '<h1>The username already exists'
else:
    print '<h1>You have create your account'
    print '<h2>Account username:' + username

print '''
  </body>
</html>

'''





