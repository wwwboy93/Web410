
function check_all(){
	if(check_username()&&check_email())
		return true;
	else
		return false;
}

function check_email(){

	var mail=$("#email").val();

    var $mailMsg=$("#email_check");

    var pattern="^[_/.a-z0-9]+@[a-z0-9]+[/.][a-z0-9]{2,}$";
    var check=new RegExp(pattern);
	if(!check.test(mail)){
		$mailMsg.html("<font color='red'>not valid email</font>");
		return false;
	}else{
		$mailMsg.html("<font color='green'>OK</font>");
		return true;

	}
}
function check_username(){
    var $username = $('#username').val();
    console.log("user name: " + $username);

    var pattern="^[0-9a-zA-Z_.-]+$";
	var check=new RegExp(pattern);

	if(!check.test($username)){
		$('#username_check').html("<font color='red'>user name not valid</font>");
                return false;
	}
    $.ajax({
        url: '../cgi-bin/isexist.py',

        data: {
            username: $username
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("login successfully");
            console.log(response);

            $('#error').empty();
            if (response.response == -1) {
               $('#username_check').html("<font color='red'>user name already exists</font>");
                return false;
            }
            else {
                $('#username_check').html("<font color='green'>username OK</font>");
                return true;
            }

        },

        error: function(request) {
            // do something
            $('#username_check').html("<font color='red'>Cannot access database!</font>");
        }
    });
}