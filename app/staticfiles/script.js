'use strict'

const hamburger = document.querySelector("#hamburger");
const menu = document.querySelector('nav');

hamburger.addEventListener('click', function () {
    menu.classList.toggle('hidden')
})


// document.addEventListener("DOMContentLoaded", function() {
//     const lightMode = document.getElementById("LightMode");
//     const darkMode = document.getElementById("DarkMode");
    
//     lightMode.addEventListener("click", function() {
//         lightMode.style.display = "none";
//         darkMode.style.display = "block";
//         document.documentElement.style.setProperty('--bg-color', '#1f1f1f');
//         document.documentElement.style.setProperty('--text', 'white');
//     });
    
//     darkMode.addEventListener("click", function() {
//         darkMode.style.display = "none";
//         lightMode.style.display = "block";
//         document.documentElement.style.setProperty('--bg-color', 'white');
//         document.documentElement.style.setProperty('--text', 'black');
//     });
// });

document.addEventListener("DOMContentLoaded", function() {
    const lightMode = document.getElementById("LightMode");
    const darkMode = document.getElementById("DarkMode");
    
    function enableDarkMode() {
        darkMode.style.display = "block";
        lightMode.style.display = "none";
        document.documentElement.style.setProperty('--bg-color', '#1f1f1f');
        document.documentElement.style.setProperty('--text', 'white');
        localStorage.setItem('theme', 'dark');
    }
    
    function enableLightMode() {
        lightMode.style.display = "block";
        darkMode.style.display = "none";
        document.documentElement.style.setProperty('--bg-color', 'white');
        document.documentElement.style.setProperty('--text', 'black');
        localStorage.setItem('theme', 'light');
    }
    
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        enableDarkMode();
    } else {
        enableLightMode();
    }
    
    lightMode.addEventListener("click", function() {
        enableDarkMode();
    });
    
    darkMode.addEventListener("click", function() {
        enableLightMode();
    });
});

