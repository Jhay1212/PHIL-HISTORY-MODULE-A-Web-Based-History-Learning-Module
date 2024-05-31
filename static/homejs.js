
document.addEventListener("DOMContentLoaded", function() {


const sidebarToggle = document.getElementById('sidebarToggle');
const sidebar = document.getElementById('sidebar');
const closeSidebar = document.getElementById('closeSidebar');

sidebarToggle.addEventListener('click', () => {
    const sidebarLeft = parseInt(window.getComputedStyle(sidebar).getPropertyValue('left'));
    if (sidebarLeft < 0) {
        sidebar.style.left = '0';
        // sidebarToggle.querySelector('img').src = './PICS/logo1.png';
    } else {
        sidebar.style.left = '-250px';
        // sidebarToggle.querySelector('img').src = './PICS/sidenav1.1.png';
    }
});

closeSidebar.addEventListener('click', () => {
    sidebar.style.left = '-250px';
    // sidebarToggle.querySelector('img').src = './PICS/sidenav1.1.png';
});

window.addEventListener('scroll', function() {
    var header = document.getElementById('header');
    if (window.scrollY > 0) {
        header.classList.add('fixed');
    } else {
        header.classList.remove('fixed');
    }
});

// Function to set the default user icon when the page is loaded
function setDefaultUserIcon() {
    const defaultIcon = "./PICS/haerin.jpg"; // Default user icon path
    const storedIcon = localStorage.getItem('userIcon');

    // Check if there's a stored user icon
    if (storedIcon) {
        document.getElementById('userIcon').src = storedIcon;
    } else {
        document.getElementById('userIcon').src = defaultIcon;
    }
}

// Function to handle changing the user icon
function changeUserIcon(event) {
    // Get the selected file
    const file = event.target.files[0];
    
    // Check if a file is selected
    if (file) {
        // Create a FileReader object to read the file
        const reader = new FileReader();
        
        // Define a function to execute when the file is read
        reader.onload = function(e) {
            // Update the user icon with the selected image
            document.getElementById('userIcon').src = e.target.result;
            
            // Store the selected image in local storage
            localStorage.setItem('userIcon', e.target.result);
        }
        
        // Read the selected file as a data URL
        reader.readAsDataURL(file);
    }
}

// Add event listener to the edit user icon input
document.getElementById('editUserIconInput').addEventListener('change', changeUserIcon);

// Call the function to set the default user icon when the page is loaded
window.addEventListener('load', setDefaultUserIcon);

// JavaScript to toggle the visibility of the dropdown buttons
document.querySelectorAll('#navSidebar li').forEach(item => {
    item.addEventListener('click', () => {
        // Toggle the visibility of the buttons inside the clicked item
        const topicButtons = item.querySelector('.topic-buttons');
        if (topicButtons.style.display === 'block') {
            topicButtons.style.display = 'none';
        } else {
            // Hide all other dropdowns before showing this one
            document.querySelectorAll('.topic-buttons').forEach(buttons => {
                if (buttons !== topicButtons) {
                    buttons.style.display = 'none';
                }
            });
            topicButtons.style.display = 'block';
        }
    });
});


document.querySelectorAll('.rectangle').forEach(rectangle => {
    const dropdown = rectangle.querySelector('.dropdown');
    
    // Show dropdown on hover
    rectangle.addEventListener('mouseenter', () => {
        dropdown.style.display = 'block';
    });
    
    // Hide dropdown when mouse leaves the rectangle
    rectangle.addEventListener('mouseleave', () => {
        dropdown.style.display = 'none';
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Get references to all lesson images
    var lessonImages = document.querySelectorAll(".content-item img");

    // Add click event listener to each lesson image
    lessonImages.forEach(function(image) {
        image.addEventListener("click", function() {
            // Get the id of the clicked image
            var lessonId = image.parentNode.querySelector("p").id;
            
            // Redirect to a new page based on the lesson id
            switch (lessonId) {
                case "TOPIC 1":
                    window.location.href = "../HOME1/unit1.php";
                    break;
                case "TOPIC 2":
                    window.location.href = "lesson2.html";
                    break;
				 case "TOPIC 3":
                    window.location.href = "lesson2.html";
                    break;
				case "TOPIC 4":
                    window.location.href = "lesson1.html";
                    break;
                case "TOPIC 5":
                    window.location.href = "lesson2.html";
                    break;
				 case "TOPIC 6":
                    window.location.href = "lesson2.html";
                    break;
				case "TOPIC 7":
                    window.location.href = "lesson1.html";
                    break;
                case "TOPIC 8":
                    window.location.href = "lesson2.html";
                    break;
				 case "TOPIC 9":
                    window.location.href = "lesson2.html";
                    break;
				case "TOPIC 10":
                    window.location.href = "lesson1.html";
                    break;
                case "TOPIC 11":
                    window.location.href = "lesson2.html";
                    break;
				 case "TOPIC 12":
                    window.location.href = "lesson2.html";
                    break;
				case "TOPIC 13":
                    window.location.href = "lesson1.html";
                    break;
                case "TOPIC 14":
                    window.location.href = "lesson2.html";
                    break;
				 case "TOPIC 15":
                    window.location.href = "lesson2.html";
                    break;
                // Add more cases for other lessons as needed
                default:
                    // Redirect to a default page if the lesson id is not recognized
                    window.location.href = "default.html";
                    break;
            }
        });
    });
});

// JavaScript to toggle the visibility of the note container
// Add this JavaScript code at the bottom of your existing script
const noteOptionBtn = document.getElementById('noteOptionBtn');
const noteContainer = document.getElementById('noteContainer');
const noteTextarea = document.getElementById('noteTextarea');
const saveNoteBtn = document.getElementById('submit');
const cancelNoteBtn = document.getElementById('cancelNoteBtn');

// Show note container when note option button is clicked
noteOptionBtn.addEventListener('click', () => {
    noteContainer.style.display = 'block';
});

// Hide note container and clear textarea when cancel button is clicked
cancelNoteBtn.addEventListener('click', () => {
    noteContainer.style.display = 'none';
    noteTextarea.value = '';
});

// Save note when save button is clicked (You can customize this function to save the note wherever you want)
saveNoteBtn.addEventListener('click', () => {
    const noteText = noteTextarea.value;
    // You can perform saving logic here
    console.log('Note saved:', noteText);
    // Clear textarea and hide note container after saving
    noteTextarea.value = '';
    noteContainer.style.display = 'none';
});

});