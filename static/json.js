// add with ajax

$(function() {
    $("#submitBtn").click(function() {
         $("#visible").attr("id", "invisible");
         $("#button_gone").attr("id", "button");
         $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + "/echo/",
            contentType: "application/json; charset=utf-8",
            data: { echoValue: $('input[name="echoText"]').val() },
            success: function(data) {

                $('#echoResult').append('<li>');
                $('#echoResult').append(data.value);
                $('#echoResult').append('</li>');
                $('#echoResult').append('<span class="invisible"><input  /><button id="update">Update</button></span>');

            }
        });
    });
});


// show form  and hide button

$(document).on("click", "#button", (function() {
    $("#invisible").attr("id", "visible");
    $("#button").attr("id", "button_gone");
}));


// font and background color switches

$(document).on("click", "#yellowFont", (function() {
     $("body").css("color", "yellow");
}));

$(document).on("click", "#blackFont", (function() {
     $("body").css("color", "black");
}));

$(document).on("click", "#whiteFont", (function() {
     $("body").css("color", "white");
}));

$(document).on("click", "#redBg", (function() {
     $("body").css("background-color", "red");
}));

$(document).on("click", "#greenBg", (function() {
     $("body").css("background-color", "green");
}));

$(document).on("click", "#blueBg", (function() {
     $("body").css("background-color", "blue");
}));



// update

var checklist = document.getElementById("checklist");

var items = checklist.querySelectorAll("div");


for (var i = 0; i < items.length; i++) {
    items[i].addEventListener("click", editItem);
}

function editItem() {
    var li = this.querySelector("li");
    li.className = "invisible"
    var span = this.querySelector("span");
    span.className = "visible"

}

$(document).on("click", "#updateBtn", (function() {
     $(".visible").attr("class", "invisible");
     $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + "/echoup/",
        contentType: "application/json; charset=utf-8",
        data: { echoUp: $('input[name="updateText"]').val() },
        success: function(data) {


                $('#echoResult').append('<li>');
                $('#echoResult').append(data.value);
                $('#echoResult').append('</li>');

        }
     });
}));


