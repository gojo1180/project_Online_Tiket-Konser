
$(document).ready(function() {
    $('.concert').hover(
        function() {
            $(this).css('background-color', '#e0ffe0');
        },
        function() {
            $(this).css('background-color', 'white');
        }
    );

    // Smooth scrolling for nav links
    $('nav a').click(function() {
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top
        }, 500);
        return false;
    });
});

