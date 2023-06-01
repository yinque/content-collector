
const app = document.querySelector('#app');
console.log(app)
function md(){
    return new MobileDetect(window.navigator.userAgent);
}
function checkMobile(){
    if(md().mobile()){
        app.classList.add('mobile');
    }else{
        app.classList.remove('mobile');
    }
}
window.addEventListener('load',checkMobile)
window.addEventListener('resize',checkMobile)

