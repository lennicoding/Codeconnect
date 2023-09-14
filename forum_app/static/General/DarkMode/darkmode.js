function switchMode() {
    if(sessionStorage.getItem("mode") == "1"){
        sessionStorage.setItem("mode", "0")
        document.body.classList.remove("dark_mode")
        return;
    }
    else if(sessionStorage.getItem("mode") == "0"){
        sessionStorage.setItem("mode", "1")
        document.body.classList.add("dark_mode")
        return;
    }

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
