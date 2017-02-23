// search.js

$('#search-form').submit(function(e){
    $.post('/search/', $(this).serialize(), function(data){
        $('.vegies').html(data);
        console.log(data);
    });
    e.preventDefault(
});
