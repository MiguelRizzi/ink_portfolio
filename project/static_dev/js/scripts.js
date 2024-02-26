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
  
