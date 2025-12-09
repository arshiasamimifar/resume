$(window).on("load", function () {
    setTimeout(function () {
        $(".preloader").addClass("loaded");
    }, 1000);

    if ($(".portfolio-items").length) {
        $(".portfolio-items").isotope();

        $(".portfolio-filter ul li").on("click", function () {
            $(".portfolio-filter ul li").removeClass("sel-item");
            $(this).addClass("sel-item");

            var filter = $(this).attr("data-filter");

            $(".portfolio-items").isotope({
                filter: filter,
                animationOptions: {
                    duration: 750,
                    easing: "linear",
                    queue: false
                }
            });
        });
    }
});

$(function () {
    "use strict";

    var win = $(window);

    function homeHeight() {
        $("#home").css({height: win.height() + "px"});
    }

    homeHeight();
    win.resize(homeHeight);

    $.scrollIt({
        upKey: 38,
        downKey: 40,
        easing: "swing",
        scrollTime: 600,
        activeClass: "active",
        onPageChange: null,
        topOffset: -15
    });

    win.on("scroll", function () {
        var scrollTop = win.scrollTop(),
            navbar = $(".navbar");

        if (scrollTop > 300) navbar.addClass("fixed-top");
        else navbar.removeClass("fixed-top");
    });

    // Stats counter
    (function () {
        if ($("section.stats").length > 0) {
            var started = 0;

            win.on("scroll", function () {
                var trigger = $("section.stats").offset().top - window.innerHeight;

                if (started === 0 && win.scrollTop() > trigger) {
                    $("section.stats .single-stat .counter").each(function () {
                        var $this = $(this),
                            countTo = $this.attr("data-count");

                        $({countNum: $this.text()}).animate(
                            {countNum: countTo},
                            {
                                duration: 2000,
                                easing: "swing",
                                step: function () {
                                    $this.text(Math.floor(this.countNum));
                                },
                                complete: function () {
                                    $this.text(this.countNum);
                                }
                            }
                        );
                    });

                    started = 1;
                }
            });
        }
    })();

    $(".nav-item .nav-link").on("click", function () {
        $(".navbar-collapse").removeClass("show");
    });

    win.stellar({horizontalScrolling: false});

    $(".portfolio .link").magnificPopup({
        delegate: "a",
        type: "image",
        gallery: {enabled: true}
    });

    $(".blogs .owl-carousel").owlCarousel({
        loop: true,
        margin: 30,
        autoplay: true,
        smartSpeed: 500,
        responsiveClass: true,
        dots: false,
        responsive: {
            0: {items: 1},
            700: {items: 2},
            1000: {items: 3}
        }
    });

    $(".testimonials .owl-carousel").owlCarousel({
        items: 1,
        loop: true,
        autoplay: true,
        smartSpeed: 500
    });

    // Contact form
    // $("#contact-form").on("submit", function (e) {
    //     e.preventDefault();
    //
    //     $("#form-submit").val("Wait...");
    //
    //     var name = $("#contact-name").val(),
    //         email = $("#contact-email").val(),
    //         message = $("#contact-message").val(),
    //         errorCount = 0;
    //
    //     $(".con-validate", this).each(function () {
    //         if ($(this).val() === "") {
    //             $(this).addClass("con-error");
    //             errorCount++;
    //         } else if ($(this).hasClass("con-error")) {
    //             $(this).removeClass("con-error");
    //             if (errorCount > 0) errorCount--;
    //         }
    //     });
    //
    //     if (errorCount === 0) {
    //         $.ajax({
    //             type: "POST",
    //             url: "mail.php",
    //             data: {
    //                 con_name: name,
    //                 con_email: email,
    //                 con_message: message
    //             },
    //             success: function (result) {
    //                 $("#contact-form input, #contact-form textarea").val("");
    //                 $("#contact-submit.primary-button span").html("Done!");
    //                 $("#contact-submit.primary-button").addClass("ok");
    //                 console.log(result);
    //             },
    //             error: function () {
    //                 $("#contact-submit.primary-button span").html("Failed!");
    //             }
    //         });
    //     } else {
    //         console.log("Validation Error");
    //     }
    // });

    $(".con-validate").keyup(function () {
        $(this).removeClass("con-error");
    });
});
