#!C:\Python27\python.exe





print 'Content-Type: text/html'
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
	<script src="../js/log_out_py.js"></script>
	<script src="../js/check_login_py.js"></script>
    <script src="../js/search.js"></script>
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


				<div class="login">
					<table>
						<tr>
							<td>username:</td>
							<td><input type="text" id="username"></td>
							<td><a href="../register.html">Sign up</a></td>
						</tr>
						<tr>
							<td>password:</td>
							<td><input type="password" id="password"></td>
							<td><a href="../forget.html">forget?</a></td>

						</tr>
						<tr>
							<td></td>
							<td colspan="2" id="login_td"><button type="button" id="login">login</button><span id="login_td_span"></span>	</td>
						</tr>
					</table>
				</div>

			</div>
		</div>
		<div id="menu">

			<ul>
				<li><a  href="../index.html">Home</a></li>
				<li class="dropdown"><a class="active" href="../activity.html">Activites</a>
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
					<button id="search_btn">GO!</button>
				</div>
			</ul>

	
			
		</div>
	</div>
	<div id="body_main">
		<div id="body_head">
			<div id="thread_title"> the Title of the the activities</div>
			<div class="comment">
				<div class="left_comment">
					<p>username:asdasd</p>
					<p>email:asdasd</p>
					<p>create date:2017-10-1</p>
				</div>	
				<div class="right_comment">
					<p>the content of the asd</p>
				</div>	
			</div>	
			<div class="comment">
				<div class="left_comment">
					<p>username:12313</p>
					<p>email:asd5414123asd</p>
					<p>create date:2017-10-1</p>
				</div>	
				<div class="right_comment">
					<p>the content of the asd</p>
				</div>	
			</div>	

			<div class="comment">
				<div class="left_comment">
					<p>username:12313</p>
					<p>email:asd5414123asd</p>
					<p>create date:2017-10-1</p>
				</div>	
				<div class="right_comment">
					<p>the content of the asd</p>
				</div>	
			</div>	
		</div>
	
		<div id="re_editor">
			<form action="./cgi-bin/create_comment.py" method="POST" enctype="multipart/form-data">
			<fieldset>
					<label for="noise">
						Reply:
					</label>
					<textarea id="noise" name="noise" class="widgEditor nothing"></textarea>
				</fieldset>
				<fieldset class="submit">
					<input type="submit" value="Reply"/>
				</fieldset>
			</form>
		</div>
		
	</div>
	
	
</body>
</html>

print '''