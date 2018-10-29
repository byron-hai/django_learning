function login() {
    var mask = document.getElementsByClassName('page_mask')[0];
    var login = document.getElementsByClassName('login')[0];
    //main.style.display = 'none';
    mask.style.display = 'block';
    login.style.display = 'block';
}

function loginSwitch(idName) {
    var login = document.getElementById('login_box');
    var signup = document.getElementById('signup_box');

    if ( idName == 'signup' ) {
        login.style.display = 'none';
        signup.style.display = 'block';
    } else if (idName == 'login') {
        login.style.display = 'block';
        signup.style.display = 'none';
    }
}

function loginQuit() {
    document.getElementsByClassName('login')[0].style.display = 'none';
    document.getElementsByClassName('page_mask')[0].style.display = 'none';
}

function addNew(idName) {
    var div = document.getElementById(idName);
    if (div.style.display == 'block') {
        div.style.display = 'none';
    } else {
        div.style.display = 'block';
    }
}