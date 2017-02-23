// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken')

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$(document).ready(function(){
    $('form').submit(function(e){
        var id = '#' + $(this).attr('id'); // for use when selecting the form.
        if (id != '#search-form'){
            e.preventDefault();
            add_to_cart(id);
        };
    });
});

function add_to_cart(id){
        form = $(id);
        // ajax posting
        $.ajax({
            url: "" , // this shouldn't matter as its being received by middleware not an endpoint.
            type: "POST",
            data: form.serialize(),
            success: function(json){
                    console.log(json.cart);
                    $('span#cart-total').html('Ksh'+json.cart_total);
                    alert = "<div class='alert alert-dismissable alert-info' data-alert='alert'>"+
                    "<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button>"+
                    "<h4>"+json.msg+"</h4>"+
                    "<hr style='border-color: transparent;'/>"+
                    "<button type='button' class='btn btn-default btn-sm' data-dismiss='alert'><i class='fa fa-shopping-cart'></i> Continue Shopping</button> "+
                    " <a href='#' class='btn btn-action btn-sm'>Go to Checkout <i class='fa fa-angle-double-right'></i></a>"+
                "</div>";
                    $('#alert').html(alert);
                    //var cart = [{"index":1},{"index":2},{"index":3},{"index":4},{"index":5}];
                    //var cart = JSON.parse(json.cart);
                    //cart.forEach(function(item){console.log(item.fields.description + 'Hello World!!')});
                    // the cart dropdown
                    
                    cart_items = JSON.parse(json.cart);
                    cart_items.forEach(function(item){
                        item_template ="<li>"+
                        "<div class='row'>"+
                        "<div class='col-sm-2'>"+
                            "<div class='image_container'>"+
                                "<a href=''><img class='thumbnail' src="+"/static/"+item.fields.image+"/onion-40x40.jpeg"+" alt="+item.fields.description+"></a>"+
                            "</div>"+
                        "</div>"+
                        "<div class='col-sm-4'>"+
                        "<p>"+item.fields.description+"</p>"+
                        "</div>"+
                        "<div class='col-sm-3 align-center'><strong>Qty </strong>"+item.fields.quantity+"</div>"+
                        "<div class='col-sm-3 price_color align-right'>"+
                        "Ksh"+item.fields.total_price+
                        "</div>"+
                        "</div>"+
                        "</li>"
                    
                        $('.basket-mini-item').append(item_template);
                    });
            },
            error: function(xhr, errmsg, err){
                    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                        " <a href='#' class='close'>&times;</a></div>");
                    console.log(xhr.status + ": " + xhr.responseText);
            }

        });
};