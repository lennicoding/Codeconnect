function switchMode() {
    document.body.classList.toggle("dark_mode")
    const lightModeBox = document.querySelector(".wrapper");
    lightModeBox.classList.remove("show");
}

function showMessage() {
    const lightModeBox = document.querySelector(".wrapper");
    if (document.body.classList.contains("dark_mode")) {
        lightModeBox.classList.remove("show");
        document.body.classList.toggle("dark_mode")
    } else {
        lightModeBox.classList.add("show");   
    }
}