//_____________________ NAVBAR____________________

// Bootstrap ScrollSpy
document.addEventListener('DOMContentLoaded', function() {
    new bootstrap.ScrollSpy(document.body, {
        target: '#main-nav',
    });
});

window.addEventListener('scroll', function() {
    var navbar = document.querySelector('.navbar');
    var scrolled = window.scrollY || document.documentElement.scrollTop;
  
    if (scrolled > 0) {
        navbar.classList.add('navbar-scroll');
    } else {
        navbar.classList.remove('navbar-scroll');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    new bootstrap.ScrollSpy(document.body, {
        target: '#main-nav',
    });
});
  
//_____________________ THEMES____________________
const body = document.querySelector("body");
const themeIcon = document.querySelector("#icon-theme");
const themeButton = document.querySelector("#button-theme");
const elementsForChange = document.querySelectorAll(".fondo");
const bodyForChange = document.querySelector("body");
const fondoMainForChange = document.querySelector(".fondo-main");
const aContactForChange = document.querySelectorAll(".a-contact");
const cardsForChange = document.querySelectorAll(".card");
const iconsForChange = document.querySelectorAll(".feature-icon");
const iconsSocialForChange = document.querySelectorAll(".icon-social");

const darkTheme = () => {
    body.setAttribute("data-bs-theme", "dark");
    themeIcon.classList.remove("bi-moon-fill");
    themeIcon.classList.add("bi-sun-fill");
    elementsForChange.forEach((elemento) => {
        elemento.classList.remove("fondo-light");
        elemento.classList.add("fondo-dark");
    });
    aContactForChange.forEach((a) => {
        a.classList.remove("text-black");
        a.classList.add("text-white");
    });
    cardsForChange.forEach((card) => {
        card.classList.remove("card-light");
        card.classList.add("card-dark");
    });
    iconsForChange.forEach((icon) => {
        icon.classList.remove("feature-icon-light")
    })
    iconsSocialForChange.forEach((icon) => {
        icon.classList.remove("text-black");
        icon.classList.add("text-white");
    });
    bodyForChange.classList.remove("image-light");
    bodyForChange.classList.add("image-dark");
    fondoMainForChange.classList.remove("main-light");
    fondoMainForChange.classList.add("main-dark");
    localStorage.setItem("theme", "dark");
}

const lightTheme = () => {
    body.setAttribute("data-bs-theme", "light");
    themeIcon.classList.remove("bi-sun-fill");
    themeIcon.classList.add("bi-moon-fill");
    elementsForChange.forEach((elemento) => {
        elemento.classList.remove("fondo-dark");
        elemento.classList.add("fondo-light");
    }); 
    aContactForChange.forEach((a) => {
        a.classList.add("text-white");
        a.classList.remove("text-secondary");
    });
    cardsForChange.forEach((card) => {
        card.classList.remove("card-dark");
        card.classList.add("card-light");
    });
    iconsForChange.forEach((icon) => {
        icon.classList.add("feature-icon-light")
    })
    iconsSocialForChange.forEach((icon) => {
        icon.classList.remove("text-white");
        icon.classList.add("text-secondary");
    });
    bodyForChange.classList.remove("image-dark");
    bodyForChange.classList.add("image-light");
    fondoMainForChange.classList.remove("main-dark");
    fondoMainForChange.classList.add("main-light");
    localStorage.setItem("theme", "light");
}
const loadTheme = () => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        darkTheme();
    } else if (savedTheme === "light") {
        lightTheme();
    } else {
        darkTheme();
    }
}

const changeTheme = () => {
    if (body.getAttribute("data-bs-theme") === "light") {
        darkTheme();
        localStorage.setItem("theme", "dark");
    } else {
        lightTheme();
        localStorage.setItem("theme", "light");
    }
}

themeButton.addEventListener("click", changeTheme);

loadTheme();



