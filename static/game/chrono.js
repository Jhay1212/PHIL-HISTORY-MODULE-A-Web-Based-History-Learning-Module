'use strict';

// console.log(__filename);
document.addEventListener('DOMContentLoaded', () => {
    const navD = document.getElementById('navSidebar');
    navD.style.display = 'none';
    const photo = document.getElementById('photo');
    const guessInput = document.getElementById('guess');
    const submitButton = document.getElementById('submit');
    const resultDiv = document.getElementById('result');

    const photos = [
        
        { src: 'static/game/photo/image1.png', year: 1990 },
        { src: 'static/game/photo/image1.png', year: 1980 },
        { src: 'static/game/photo/image1.png', year: 2000 }
    ];

    let currentPhotoIndex = 0;

    function loadPhoto(index) {
        
        photo.src = photos[index]['src'];
        guessInput.value = '';
        resultDiv.textContent = '';
    }

    submitButton.addEventListener('click', () => {
        const userGuess = parseInt(guessInput.value, 10);
        if (isNaN(userGuess)) {
            resultDiv.textContent = 'Please enter a valid year.';
            return;
        }

        const correctYear = photos[currentPhotoIndex].year;
        if (userGuess === correctYear) {
            resultDiv.textContent = 'Correct!';
        } else {
            resultDiv.textContent = `Incorrect! The correct year was ${correctYear}.`;
        }

        currentPhotoIndex = (currentPhotoIndex + 1) % photos.length;
        setTimeout(() => loadPhoto(currentPhotoIndex), 2000);
    });

    loadPhoto(currentPhotoIndex);
});

