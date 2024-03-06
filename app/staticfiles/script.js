'use strict'

const hamburger = document.querySelector("#hamburger");
const menu = document.querySelector('nav');

hamburger.addEventListener('click', function () {
    menu.classList.toggle('hidden')
})