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
    var username = $('#username').val();
    /*read a cookie that contains { username: transid } */
    var transid1 = $.cookie(username); // => transid
    if (transid1 == undefined) {
        transid1 = " ";
    }
    // var transid1 = "E9S3GmL0BoIRodVizgHOahG5UcOnS08j";
    var activityname = $('#activityname').val();
    var activitycontent = $('#activitycontent').val();
    console.log("transid: " + transid1);
    // alert( "error" );
    // console.log(typeof $(username).val());
    $.ajax({

        url: '../cgi-bin/new_activity.py',
        // contentType: "application/json; charset=utf-8",

        data: {
            username: username,
            transid: transid1,
            activityname: activityname,
            activitycontent: activitycontent
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("Created a new activity");
            console.log(response);
            
            $('#error').empty();

            if (response.response == -1) {
                $('#activity_res').html("<font color=\"red\">Wrong session ID, Please login again</font>");
                clear_info();
                
            }
            else {
                // $('.login').hide();
                $('#activity_res').html("New activity created!" + "<br>");
            }

        },

        error: function(request) {
            // do something
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
