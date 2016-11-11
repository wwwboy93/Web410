/**
 * create a new activity with ajax
 * */


$(document).ready(function() {
    console.log("start to create a new activity");
    // var $username = $('#username').val();
    $('#activity').click(activity);
    // console.log("hehe "+typeof $(username).val());
});

/* activity function */
var activity = function() {
    var $username = $('#username').val();
    var $activityname = $('#activityname').val();
    var $activitycontent = $('#activitycontent').val();

    $.ajax({

        url: '../cgi-bin/new_activity.py',
        // contentType: "application/json; charset=utf-8",

        data: {
            username: $username,
            activityname: $activityname,
            activitycontent: $activitycontent
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("Created a new activity");
            console.log(response);
            
            $('#error').empty();

            if (response.response == -1) {
                $('#activity_res').html("Can not create an activity!");
                clear_info();
                
            }
            else {
                $('.activity').hide();
                $('#activity_res').html("New activity created!" + "<br>");
            }

        },

        error: function(request) {
            console.log("create activity failed");
        }

    });
    
};

/* clear username and password field */
function clear_info() {
    console.log("clear username, activityname, activitycontent");
    $('#username').val('');
    $('#activityname').val('');
    $('#activitycontent').val('');
}
