#!C:\Python27\python

# this code has been enhanced from the base demo given in class to include more complicated form submission types
# including drop-down lists, checkboxes, and a password field to hide the credit card number.
#
# note that this code is extraordinarily fragile.  things that will blow it up include:
#    a. not specifying a phone number
#    b. not specifying a credit card number
#    c. choosing 0 or 1 toppings
#    d. probably other things.
#  I will leave it as an exercise for the interested student to fix these errors.

import cgitb
import cgi
import MySQLdb
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
          font-size: 100px;
          font-family: monospace;
      }


    </style>

  </head>
  <body>
'''


def insert_user(username, password, email):
    conn = MySQLdb.connect('localhost', 'cc', '123123', 'web410')
    cursor = conn.cursor()
    results = conn.execute('SELECT id FROM user where id = 1')
    date = str(datetime.datetime.now())
    hasher = hashlib.md5()
    # if the id =1 user is not existing we create it
    if results.arraysize == 0:
        hasher.update('123123')
        hasher.update(date)
        encrypted = hasher.hexdigest()
        cursor.execute("INSERT INTO users(id, username, password, date) VALUES(?,?,?, ?);"
                       , ['1', 'admin', encrypted, date])
        conn.commit()
    results = conn.execute('SELECT id FROM user where user_name = ?', [username])
    if results.arraysize == 1:
        return -1
    hasher.update(password)
    hasher.update(date)
    encrypted = hasher.hexdigest()

    cursor.execute("INSERT INTO users(username, password, email, date)"
                   "VALUES(?,?,?,?);", [username, encrypted, email, date])
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





