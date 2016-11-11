/**
 * login with ajax
 * */

$(document).ready(function() {
    console.log("start to log in");

    $('#login').click(login);
});

/* login function */
var login = function() {
    var $username = $('#username').val();
    var $password = $('#password').val();
    console.log("user name: " + $username);

    $.ajax({
        url: '../cgi-bin/login.py',

        data: {
            username: $username,
            password: $password
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("login successfully");
            console.log(response);
            
            $('#error').empty();
            if (response.response == -1) {
                $('#login_res').html("<font color=\"red\">wrong username or password! please try again</font>");
                clear_login_info();
                
            }
            else {
                $('.login').hide();
                // Set a cookie at Client with the returned transID (transaction ID) expires within 60 days
                $.cookie($username, response.response, { expires: 60 });
                $('#login_res').html("welcome, " + $username + "<br>");
                $('#check_login_res').html("<font color=\"red\">You have logged in!</font>");
            }

        },

        error: function(request) {
            // do something
        }
    });
    
};

/* clear username and password field */
function clear_login_info() {
    console.log("clear user name and password");
    $('#username').val('');
    $('#password').val('');
}
