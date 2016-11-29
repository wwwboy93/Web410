#!/usr/bin/python

print "Content type: text/html"
print

print '''
<!DOCTYPE html>
<html>
<head>
	<title>Hang OUT!</title>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script src="../js/widgEditor.js"></script>

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
				<table>
					<tr>
						<td>username:</td>
						<td><input type="text" id="username"></td>
						<td><a href="#">Sign up</a></td>
					</tr>
					<tr>
						<td>password:</td>
						<td><input type="password" id="password"></td>
						<td><a href="#">forget?</a></td>

					</tr>
					<tr>
						<td></td>
						<td colspan="2"><button type="button" id="login">login</button>	</td>
					</tr>
				</table>
			</div>
		</div>
		<div id="menu">

			<ul>
				<li><a href="./index.html">Home</a></li>
				<li class="dropdown"><a href="./activity.html">Activites</a>
				<div class="dropdown-content">
					<a href="#">Sports</a>
					<a href="#">Games</a>
					<a href="#">Events</a>
					<a href="#">Travel</a>
				</div>
				</li>

				<li><a href="#contact">Join Nearby</a></li>
				<li><a  class="active" href="#">Create New</a></li>

				<div id="search_bar">
					<input type="text" name="search_bar" id= "search"/>
					<input type="button" name="search_click" id="search_btn" value="GO!">
				</div>
			</ul>



		</div>
	</div>
'''