//_____________________ THEMES____________________
const body = document.querySelector("body");
const themeIcon = document.querySelector("#icon-theme");
const themeButton = document.querySelector("#button-theme");
const elementsForChange = document.querySelectorAll(".fondo");
const bodyForChange = document.querySelector("body");
const fondoMainForChange = document.querySelector(".fondo-main");
const textForChange = document.querySelectorAll(".text");
const cardsForChange = document.querySelectorAll(".card");
const iconsForChange = document.querySelectorAll(".feature-icon");
const iconsSocialForChange = document.querySelectorAll(".icon-social");
const navbarForChange = document.querySelector(".navbar");
const activeForChange = document.querySelectorAll(".active");
const navIconforChange = document.querySelector(".navbar-icon")
 
const darkTheme = () => {
    body.setAttribute("data-bs-theme", "dark");
    themeIcon.classList.remove("bi-moon-fill");
    themeIcon.classList.add("bi-sun-fill");
    elementsForChange.forEach((elemento) => {
        elemento.classList.remove("fondo-light");
        elemento.classList.add("fondo-dark");
    });
    textForChange.forEach((text) => {
        text.classList.remove("text-black");
        text.classList.add("text-white");
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
    activeForChange.forEach((active) => {
        active.classList.remove("active-dark");
        active.classList.add("active-light");
    })
    bodyForChange.classList.remove("image-light");
    bodyForChange.classList.add("image-dark");
    fondoMainForChange.classList.remove("main-light");
    fondoMainForChange.classList.add("main-dark");
    navbarForChange.classList.remove("navbar-light");
    navbarForChange.classList.add("navbar-dark");
    navIconforChange.classList.remove("navbar-icon-light");
    
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
    textForChange.forEach((text) => {
        text.classList.remove("text-white");
        text.classList.add("text-black");
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
        icon.classList.add("text-black");
    });
    activeForChange.forEach((active) => {
        active.classList.remove("active-light");
        active.classList.add("active-dark");
    })
    bodyForChange.classList.remove("image-dark");
    bodyForChange.classList.add("image-light");
    fondoMainForChange.classList.remove("main-dark");
    fondoMainForChange.classList.add("main-light");
    navbarForChange.classList.remove("navbar-dark");
    navbarForChange.classList.add("navbar-light");
    navIconforChange.classList.add("navbar-icon-light");
   
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



