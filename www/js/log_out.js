$(document).ready(function() {
    console.log("log out!");

    $('#log_out').click(log_out);
});

/* login function */
var log_out = function() {
    var $cookie1 = $.cookie();
    console.log($cookie1);
    var $username = Object.keys($cookie1)[0];
    console.log("user name: " + $username);

    $.ajax({
        url: '../cgi-bin/log_out.py',

        data: {
            username: $username,
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("log_out successfully");
            console.log(response);
            
            $('#error').empty();
            if (response.response == -1) {
                $('#log_out_res').html("<font color=\"red\">Sorry, log out failed!</font>");
            }
            else {
                $('.login').hide();
                $('.log_out').hide();
                $.removeCookie($username);
                $('#log_out_res').html("User: " + $username + " logs out successfully!");
            }

        },

        error: function(request) {
            // do something
        }
    });
    
};


