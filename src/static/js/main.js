$('.gallery-slider').slick({
    dots: true,
    arrows: false,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 500,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
        {
        breakpoint: 1025,
        settings: {
            slidesToShow: 2
        }
        },
        {
        breakpoint: 768,
        settings: {
            slidesToShow: 1
        }
        }
    ]
});