const SpinerLoader = document.querySelector('.spinner-loader')

window.addEventListener('load',() => {

    SpinerLoader.style.opacity = '0';

    setTimeout(() =>{
    
    SpinerLoader.style.display = 'none';

    }, 200);
});

