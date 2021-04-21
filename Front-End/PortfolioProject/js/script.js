/*let images = document.querySelectorAll('.slider');
let start = 0;
images[start].style.display = 'block'

const moveSlider = () => {
    if (start == images.length - 1) {
        start = -1;
    };
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = 'none'
    }

}

setInterval(() => {
    moveSlider();

}, 2000)