$(function() {
    $("#submitBtn").click(function() {
         $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + "/echo/",
            contentType: "application/json; charset=utf-8",
            data: { echoValue: $('input[name="echoText"]').val() },
            success: function(data) {
                $('#echoResult').text(data.value);
            }
        });
    });
});
