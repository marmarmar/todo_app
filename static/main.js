// Submit post on submit
$('#post-form').on('submit', function(event){
    console.log("form submitted!")  // sanity check
    create_post();
});