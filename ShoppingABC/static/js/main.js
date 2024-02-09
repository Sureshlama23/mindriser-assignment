(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });
// Product Quantity
// $('.changeQuantity').click(function(e){
//     e.preventDefault();

//     var product_id = $(this).closest('product_data').find('.product_id').val();
//     var product_qty = $(this).closest('product_data').find('.qty-input').val();
//     var token = $('input[name=csrfmiddlewaretoken]').val();
//     $.ajax({
//         type: "POST",
//         url: "/cart-plus",
//         data: {
//             "product_id":product_id,
//             "product_qty":product_qty,
//             csrfmiddlewaretoken: token
//         },
//         success: function (response) {
//         }
//     });
// })
$('.btn-plus').click(function(){
    console.log('pickclicked')
    var id = $(this).attr("pid");
    console.log(id);
    $.ajax({
        type: "GET",
        url: "/cart-plus",
        data: {product_id:id},
        success: function (data) {
            console.log(data);
            console.log('success');
            
        }
    });
})

})(jQuery);



