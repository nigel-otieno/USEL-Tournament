// index.js

// Wait for the document to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Initialize all elements with the `data-bs-toggle="collapse"` attribute (Bootstrap accordion)
    var accordionElements = document.querySelectorAll('[data-bs-toggle="collapse"]');
    accordionElements.forEach(function (element) {
        element.addEventListener("click", function () {
            // Toggle the collapse state for each accordion item
            var target = document.querySelector(element.getAttribute("data-bs-target"));
            if (target) {
                target.classList.toggle("show");
            }
        });
    });
});
