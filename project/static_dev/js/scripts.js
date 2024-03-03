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
const sectionsForChange = document.querySelectorAll("section");



const darkTheme = () => {
    body.setAttribute("data-bs-theme", "dark");
    themeIcon.classList.remove("bi-moon-fill");
    themeIcon.classList.add("bi-sun-fill");
    elementsForChange.forEach((elemento) => {
        elemento.classList.remove("fondo-light");
        elemento.classList.add("fondo-dark");
    });
    sectionsForChange.forEach((section) => {
        section.classList.remove("section-light");
        section.classList.add("section-dark");
    });
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
    sectionsForChange.forEach((section) => {
        section.classList.remove("section-dark");
        section.classList.add("section-light");
    });
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



