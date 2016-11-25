/*
 * This script fetches  activities from database and list 
 * them both by categories and by post data (or by popularity)
 * */

$(document).ready(function() {
    console.log("list activities");
    list_all_activities();
    list_activities_by_category();
});

function list_activities_by_category() {
    /* to be done*/
}

/* list all activities by their created time */
function list_all_activities() {
    console.log("start to list activities");

    $.ajax({
        url: '../cgi-bin/get_activities.py',

        data: {
            type: "all"
        },

        type: "GET",

        dataType: "json",

        success: function(response) {
            console.log("get_activities.py executed");

            /* start to list all activities */
            if (response != null) {
                var activities = response.activity;
                var $all_activities = $('#all_activities');
                for (var i = 0; i < activities.length; i++) {
                    var activity = activities[i];
                    /* add a new table row in this table */
                    var tr = "<tr class=\"table_entry\">";
                    tr += "<td>" + activity.title + "</td>";
                    tr += "<td>" + activity.username + "</td>";
                    tr += "<td>" + activity.reply_times + "</td>";
                    tr += "<td>" + activity.create_time + "</td>";
                    tr += "</tr>";
                    $all_activities.append(tr);
                }
            }

        },

        error: function(response) {
            console.log("ERROR: fetch all activities failed");
            // error
            console.log(response);
        }
    }); 
};
