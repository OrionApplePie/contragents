$(document).ready(function() {
    function getRandomInt(min, max)
    {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
    //
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
    //
    $("#search").submit(function( event ) {
            event.preventDefault();
            var $form = $(this);
            term = $form.find("input[name='search']").val();
            var csrftoken = getCookie('csrftoken');

            /*
            var $form = $(this),
                term = $form.find("input[name='search']").val(),
                url = $form.attr("action");

            var posting = $.post( url, { search: term } );
            */
            $.ajax({
                url:"/",
                type: "post",
                data:  term,
                //csrfmiddlewaretoken: csrftoken,
                headers: { "X-CSRFToken": getCookie("csrftoken") },

                success: function( data ) {
                //var content = $(data).find("#content");
                $("#result").html(JSON.stringify( data ) );


            }})

            });

    $(window).scroll(function() {
        var windowScroll = $(window).scrollTop();
        var windowHeight = $(window).height();
        var documentHeight = $(document).height();
        if ((windowScroll + windowHeight) == documentHeight) {
            var randName = getRandomInt(1, 100);
            $("#wrapper").append('<div class="block ' + randName + '">' + randName + '</div>');

         }
        console.log(windowScroll + " " + windowHeight + " " + documentHeight);
        })

})