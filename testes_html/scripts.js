const images = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg'];
let index = 0;

function changeBackground() {
    const container = document.getElementById('backgroundContainer');
    container.style.backgroundImage = `url(${images[index]})`;
    index = (index + 1) % images.length;
}

setInterval(changeBackground, 5000);
