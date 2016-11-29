$(document).ready(function() {
    console.log("profile.js begins");
    var $cookie1 = $.cookie();
    console.log("Cookie is " + $.cookie());
    var $username = Object.keys($cookie1)[0];

    if ($username != undefined) {
        console.log("user name: " + $username);

        $.ajax({
            url: '../cgi-bin/profile.py',

            data: {
                username: $username
            },

            type: "POST",

            dataType: "json",

            success: function(response) {
                console.log("get profile successfully");
                console.log(response);
                
                $('#error').empty();
                if (response.response == -1) {
                    $('#profile_res1').html("Can not get username!");
                    $('#profile_res2').html("Can not get user email!");
                }
                else {
                    $('#profile_res1').html($username);
                    $('#profile_res2').html(response.response);
                    
                }

            },

            error: function(request) {
                // do something
            }
        });
    } else {
        console.log("Cannot get username!");
        $('.log_out').hide();
    }

});




    



