/*let slideIndex = 0;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}



function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slider");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) { slideIndex = n - 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", " ");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";


}

setInterval(() => {
    showSlides(slideIndex += 1);

}, 2000)
*/


//

/*function myFunction() {
    let i;
    let index = document.getElementByClassName("index1");
    index[i].classList.add("show");

    alert();
}*/

/*function myFunction() {
    document.getElementsByClassName("index1").style.opacity = "0.7 !important";
}*/

/*let move = 0;
let sliderLine = document.querySelector('.slider');

console.log(sliderLine)

document.querySelector('.dot1').addEventListener('click', () => {
    sliderLine.style.transition = 'all 0.8s ease 0s';
    move += 291;
    if (move > 873) {
        sliderLine.style.transition = 'none';
        move = 0
    }
    sliderLine.style.left = -move + 'px';
})

document.querySelector('.dot2').addEventListener('click', () => {
    sliderLine.style.transition = 'all 0.8s ease 0s';
    move -= 291;
    if (move < 0) {
        sliderLine.style.transition = 'none';
        move = 873
    }
    sliderLine.style.left = -move + 'px';
})*/


let smooth = document.querySelectorAll('.smooth');
for (let i = 0; i < smooth.length; i++) {
    smooth[i].addEventListener('click', (e) => {
        e.preventDefault();
        const sectionId = e.target.getAttribute('href');
        document.querySelector(sectionId).scrollIntoView({
            behavior: 'smooth'
        })
    })

}