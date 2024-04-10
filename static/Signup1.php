<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="signup1-css.css">
    <title>Sign Up - PH KASAYSAYAN</title>
</head>

<body>
    <div class="signup-container">
        <h2>Create an Account</h2>
        <form action="register.php" method="post" onsubmit="return validateForm()">
            <div class="form-group">
                <input type="text" name="username" placeholder="Username" required>
            </div>
            <div class="form-group">
                <div class="password-input">
                    <input type="password" name="password" id="password" placeholder="Password" required>
                    <img class="eye" src="close.png" onclick="togglePasswordVisibility('password')">
                </div>
            </div>
            <div class="form-group">
                <div class="password-input">
                    <input type="password" name="confirm_password" id="confirm_password" placeholder="Confirm Password" required onkeyup="validatePassword()">
                    <img class="eye" src="close.png" onclick="togglePasswordVisibility('confirm_password')">
                </div>
                <label id="password-match-label">Passwords do not match</label>
            </div>
            <div class="form-group">
                <input type="submit" value="Sign Up">
            </div>
        </form>
        <p>Already have an account? <a href="Login1.php">Login here</a>.</p>
    </div>

    <script>
        function togglePasswordVisibility(inputId) {
            var passwordInput = document.getElementById(inputId);
            var eyeIcon = passwordInput.nextElementSibling; // Get the next sibling, which is the eye icon

            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                eyeIcon.src = "open.png"; // Change to open eye image
            } else {
                passwordInput.type = "password";
                eyeIcon.src = "close.png"; // Change to closed eye image
            }
        }

        function validatePassword() {
            var password = document.getElementById("password").value;
            var confirm_password = document.getElementById("confirm_password").value;
            var passwordMatchLabel = document.getElementById("password-match-label");

            if (password !== confirm_password) {
                passwordMatchLabel.style.display = "block";
            } else {
                passwordMatchLabel.style.display = "none";
            }
        }

        function validateForm() {
            var password = document.getElementById("password").value;
            var confirm_password = document.getElementById("confirm_password").value;

            if (password !== confirm_password) {
                document.getElementById("password-match-label").style.display = "block";
                return false;
            }
            return true;
        }
    </script>
</body>
</html>
