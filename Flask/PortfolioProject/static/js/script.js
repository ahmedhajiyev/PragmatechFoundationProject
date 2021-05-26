//For Slider

let images = document.querySelectorAll('.slider');
let start = 0;
images[start].style.display = 'block';

document.querySelector('.dot1').addEventListener('click', () => {
    if (start == images.length - 1) {
        start = -1;
    };
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = 'none';
    }
    images[++start].style.display = 'block';
})


document.querySelector('.dot2').addEventListener('click', () => {
    start -= 1;
    if (start < 0) {
        start = images.length - 1;
    }
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = 'none';
    }
    images[start].style.display = 'block';
})



const moveSlider = () => {
    if (start == images.length - 1) {
        start = -1;
    };
    for (let i = 0; i < images.length; i++) {
        images[i].style.display = 'none';
    }
    images[++start].style.display = 'block';
}


/* Sonsuz */
let move = setInterval(() => {
    moveSlider();
}, 10000);

//


const animationItems = document.querySelectorAll('._anim');
const animationOnScroll = () => {
    if (animationItems.length > 0) {
        for (let i = 0; i < animationItems.length; i++) {
            // Animasiya ne zaman baslasin
            const animationStart = 4;
            // ekranin olcusu elementin olsunun 1/4 oldugda animasi aktivlessin
            let animationItemPoint = window.innerHeight - animationItems[i].offsetHeight / animationStart;
            // Eger scroll deyeri > sehifenin en basindan elemente geder olan mesafe - elementin 1/4 geder
            if ((pageYOffset > (animationItems[i].offsetTop - animationItemPoint)) && (pageYOffset < (animationItems[i].offsetTop + animationItems[i].offsetHeight))) {
                animationItems[i].classList.add('_active');
            } else {
                // Animasiyani  tekrarlanmamasi ucun sert
                if (!animationItems[i].classList.contains('_noRepeat')) {
                    animationItems[i].classList.remove('_active');
                }
            }
        }
    }
}
window.addEventListener('scroll', animationOnScroll);
// Sehife acilanda il section animasiyanin aktivlesmesi
animationOnScroll();