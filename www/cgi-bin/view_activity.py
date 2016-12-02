#!C:\Python27\python.exe


import cgi
import cgitb
import sqlite3

cgitb.enable()

# fetch the activity id
act_id = cgi.FieldStorage()['id'].value

activity = {}
comments = []

def get_activity():
    global activity
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    _activity = cursor.execute("SELECT * FROM activity WHERE act_id = " + act_id)

    if _activity is None:
        conn.close()
        return
    for __activity in _activity:
        activity['act_id'] = str(__activity[0])
        activity['user_id'] = str(__activity[1])
        activity['title'] = str(__activity[2])
        activity['content'] = str(__activity[3])
        activity['create_time'] = str(__activity[4])
        activity['category'] = str(__activity[5])
        activity['area'] = str(__activity[6])
        activity['reply_times'] = str(__activity[7])
        img_path = cursor.execute("select path from image where activity_id = " + act_id)
        for _img_path in img_path:
            activity['img_path'] = "../pics/memberphotos/" + str(_img_path[0])

    conn.close()


def get_comments():
    global comments
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    _comments = cursor.execute("select * from comment where activity_id = " + act_id)

    if _comments is None:
        conn.close()
        return

    for _comment in _comments:
        comment = { }
        comment['com_id'] = str(_comment[0])
        comment['activity_id'] = str(_comment[1])
        comment['content'] = str(_comment[2])
        comment['create_time'] = str(_comment[3])[0 : -7];
        comment['replier_id'] = str(_comment[4])
        comment['replier_name'] = str(_comment[5])
        comments += [comment]
    conn.close()

get_activity()
get_comments()

print "Content type: text/html"
print

print '''
<!DOCTYPE html>
<html>
<head>
	<title>Hang OUT!</title>
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script src="../js/widgEditor.js"></script>
	<script src="../js/jquery.cookie.js"></script>
	<script type="text/javascript" src="../js/login.js"></script>
	<script src="../js/log_out.js"></script>
	<script src="../js/check_login.js"></script>
	
	<style type="text/css" media="all">
		@import "../css/main.css";
		@import "../css/widgEditor.css";
	</style>
	<link rel="stylesheet" type="text/css" href="../css/style.css">
	<link rel="stylesheet" type="text/css" href="../css/slide.css">
	
</head>

<body>
	<div id="header">
		<div id="top_area">
			<div id="logo_bar">Hang OUT</div>
			<div id="login_bar">
				<div id="check_login_res"></div>
				<div class="login">
					<table>
						<tr>
							<td>username:</td>
							<td><input type="text" id="username"></td>
							<td><a href="#">
					        <form action="../register.html">
					            <input type="submit" value="register">
					        </form>
					        </a></td>
						</tr>
						<tr>
							<td>password:</td>
							<td><input type="password" id="password"></td>
							<td colspan="2"><button type="button" id="login">login</button>	</td>
							<td><a href="#">forget?</a></td>
							
						</tr>
					</table>
				</div>
		        <div id="login_res"></div>
		        <div id="error"></div>  
		        <div id="log_out_res"></div>
			</div>
		</div>
		<div id="menu">

			<ul>
				<li><a href="../index.html">Home</a></li>
				<li class="dropdown"><a href="../activity.html">Activites</a>
				<div class="dropdown-content">
					<a href="#">Sports</a>
					<a href="#">Games</a>
					<a href="#">Events</a>
					<a href="#">Travel</a>
				</div>
				</li>

				<li><a href="../join_nearby.html">Join Nearby</a></li>
				<li><a href="../new_activity.html">Create New</a></li>


				<div id="search_bar">
					<input type="text" name="search_bar" id= "search"/>
					<input type="button" name="search_click" id="search_btn" value="GO!">
				</div>
			</ul>

	
			
		</div>
	</div>
	<div id="body_main">
		<div id="body_head">
			<div id="thread_title">
'''

print activity['title'] + "</div>"

# print the content of the activity
print "<div class=\"comment\">"
print "<p>" + activity['content'] + "</p>"
print "</br>"
print "<img style=\"height:200px; width:auto\" src=\"" + activity['img_path'] + "\">"
print "</div>"


# print comments
for comment in comments:
    print "<div class=\"comment\">"
    print "<div class=\"left_comment\">"
    print "<p>username: " + comment['replier_name'] + "</p>"
    print "<p>time: " + comment['create_time'] + "</p>";
    print "</div>"
    print "<div class=\"right_comment\">"
    print "<p>" + comment['content'] + "</p>";
    print "</div></div>"

print "</div></div>"
print "</body></html>"

