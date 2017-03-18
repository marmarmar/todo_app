$(document).ready(function() {
            $("#add").focus();
            $("#add").keypress(function(event) {
                var key = (event.keyCode ? event.keyCode : event.which);
                if (key == 13) {
                    var add = $("#add").val();
                    $.ajax({
                        method: "POST",
                        url: "action.php",
                        data: {task: add},
                        success: function(status) {
							        $('#result').append(status);
							        $('#add').val('');
							        alert("added");
					    }
					});
				};
            });
        });