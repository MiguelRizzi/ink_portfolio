// Sliders
var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    loop: true,
    centerSlide: true,
    fade: true,
    grabCursor: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dinamicBullets: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        520: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 3,
        }

    }
});

var slider1 = new Swiper ('.slider1', {
    effect: 'fade',
    loop:true,
    autoplay: {
        delay: 3000, 
        disableOnInteraction: false,
    },
});
var slider2 = new Swiper ('.slider2', {
    effect: 'fade',
    loop:true,
    autoplay: {
        delay: 3000, 
        disableOnInteraction: false,
    },
});
// Controlar el cambio de diapositivas con setTimeout
function moveSlider1() {
slider1.slideNext();
setTimeout(moveSlider1, 3000);
}
function moveSlider2() {
slider2.slideNext();
setTimeout(moveSlider2, 3000);
}
// Iniciar el movimiento de los sliders
setTimeout(moveSlider1, 3000);
setTimeout(moveSlider2, 1500);

// Función para cambiar el texto de los sliders
squareTattos = document.getElementById('square-tattoos');
squareDesigns = document.getElementById('square-designs');
h3SliderTattoos = document.getElementById('h3-slider-tattoos');
h3SliderDesigns = document.getElementById('h3-slider-designs');
initialTextTatttos = "TATUAJES"
initialTextDesigns = "DISEÑOS"
hoverTextTatttos = "VER TATUAJES"
hoverTextDesigns = "VER DISEÑOS"

function changeTextOnHover(element1, element2, initialText, hoverText) {
  element1.addEventListener('mouseover', function() {
    element2.innerHTML = hoverText;
  });
  element1.addEventListener('mouseout', function() {
    element2.innerHTML = initialText;
  });
}

// Uso de la función para los elementos h3
changeTextOnHover(squareTattos, h3SliderTattoos, initialTextTatttos, hoverTextTatttos);
changeTextOnHover(squareDesigns, h3SliderDesigns, initialTextDesigns, hoverTextDesigns);