/**
 * Created by tmck on 3/2/17.
 */
$(document).ready(function() {
    // check where the detail box is
    var offset = $('#detail-box').offset();

    $(window).scroll(function () {
        var scrollTop = $(window).scrollTop(); // check the visible top of the browser

        if (offset.top<scrollTop) $('#detail-box').addClass('fixed');
        else $('#detail-box').removeClass('fixed');
    });
});
