function signup() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let retype_password = document.getElementById("retype-password").value;
    let email = document.getElementById("email").value;

    if (username == "" || password == "" || retype_password == "" || email == "") {
        alert("Please fill every input field!")
    }
    else if (username == " " || password == " " || retype_password == " " || email == " ") {
        alert("Please enter a valid character! Not just spaces!")
    }}
