function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var eyeIcon = document.querySelector(".eye");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.src = "./PICS/open.png"; // Change to open eye image
    } else {
        passwordInput.type = "password";
        eyeIcon.src = "./PICS/close.png"; // Change to closed eye image
    }
}

