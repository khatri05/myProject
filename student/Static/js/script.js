function showMessage(){
    alert("Welcome to Student Management System! This is a simple web application built using Django framework. You can manage student records, view details, and perform various operations related to student management. Enjoy exploring the features!");
}

document.addEventListener("DOMContentLoaded", function () {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');

    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
        new bootstrap.Tooltip(tooltipTriggerEl);
    });
});