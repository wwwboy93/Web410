$(document).ready(function() {
    console.log("check_login!");
    var $cookie1 = $.cookie();
    console.log("fafa" + $.cookie());
    console.log($cookie1);
    var $username = Object.keys($cookie1)[0];
    var $transid = $cookie1[Object.keys($cookie1)[0]];
    
    if ($username != undefined) {
        console.log("user name: " + $username + $transid);


        $.ajax({
            url: '../cgi-bin/check_login.py',

            data: {
                username: $username,
                transid: $transid
            },

            type: "POST",

            dataType: "json",

            success: function(response) {
                console.log("check_login successfully");
                console.log(response);
                
                $('#error').empty();
                if (response.response == -1) {
                    $('#login_td').append('<font color=\"red\">Please login again</font>');
                }
                else {
                    $('.login').html("welcome, " + $username + "&nbsp&nbsp&nbsp<a href='profile.html'>profile</a>&nbsp&nbsp&nbsp");
                    $('.login').append("<button id='log_out' >logout</button>");
                }

            },

            error: function(request) {
                // do something
            }
        });
    } else {
        // ??? Can not hide the log out button and activity
        // ??? How to jump to log in page?
        console.log("log in check failed");
        $('.log_out').hide();
        $('.activity').hide();
        // ??? 如何只在 非主页 显示
        $('#check_login_res').html("<font color=\"red\">Please log in first</font>");
    }

});




    



