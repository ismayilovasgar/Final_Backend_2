var swiper = new Swiper(".swiper", {
  // slidesPerView: 2,
  spaceBetween: 32,
  // loopAdditionalSlides: 2,

  sliderPerGroup: 3,
  loop: true,
  // centerSlide: "true",
  fade: "true",
  // grabCursor: "true",
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    // dynamicBullets: true,
  },
  navigation: {
    nextEl: ".slickNext",
    prevEl: ".slickPrev",
  },

  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    700: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 24,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 32,
    },
  },
});
