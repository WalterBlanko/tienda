'use strict'

window.addEventListener('load', () => {
    var registro = document.querySelector('#registro');
    document.querySelector('#error').style.display = 'none';

    registro.addEventListener('submit', () => {
        var username = document.querySelector('#InputUsername').value;
        var email = document.querySelector('#inputRegEmail').value;
        var region = document.querySelector('#regiones').value;
        var provincia = document.querySelector('#provincia').value;
        var comuna = document.querySelector('#comunas').value;
        var pass1 = document.querySelector('#InputRegPassword').value;
        var pass2 = docucment.querySelector('#InputRegPassword2').value;

        if(username.length == 0) {
            document.querySelector('.emptyUser').innerHTML = '¡Ingrese nombre de usuario!'
            return false;
        } else {
            document.querySelector('.emptyUser').style.display = 'none';
        }

        console.log(username);

        if(email.length == 0) {
            document.querySelector('.emptyEmail').innerHTML = '¡Ingrese correo electronico!'
            return false;
        } else {
            document.querySelector('.emptyEmail').style.display = 'none';
        }

        if(region.length == 0) {
            document.querySelector('.emptyRegion').innerHTML = '¡Seleccione region!'
            return false;
        } else {
            document.querySelector('.emptyRegion').style.display = 'none';
        }

        if(provincia.length == 0) {
            document.querySelector('.emptyProvincia').innerHTML = '¡Seleccione provincia!'
            return false;
        } else {
            document.querySelector('.emptyProvincia').style.display = 'none';
        }

        if(comuna.length == 0) {
            document.querySelector('.emptyComuna').innerHTML = '¡Seleccione comuna!'
            return false;
        } else {
            document.querySelector('.emptyComuna').style.display = 'none';
        }

        if(pass1.length == 0) {
            document.querySelector('.emptyPass').innerHTML = '¡Ingrese contraseña!'
            return false;
        } else {
            document.querySelector('.emptyPass').style.display = 'none';
        }

        if(pass2.length == 0) {
            document.querySelector('.emptyPass2').innerHTML = '¡Ingrese confirmación de contraseña!!'
            return false;
        } else {
            document.querySelector('.emptyPass2').style.display = 'none';
        }

        if(pass1 != pass2 || pass2 != pass1) {
            document.querySelector('.errorPass').innerHTML = '¡Contraseñas no coinciden!';
            return false;
        } else {
            document.querySelector('.errorPass').style.display = 'none';
        }
    });
});