$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close')
})

var lbNome = document.getElementById("lbNome")
var nome = document.getElementById("nome")

var lbCelular = document.getElementById("lbCelular")
var celular = document.getElementById("celular")

var lbEmail = document.getElementById("lbEmail")
var email = document.getElementById("email")

var lbLogin = document.getElementById("lbLogin")
var login = document.getElementById("login")

function validar(evento){

    let alerta = false;

    if (nome.value == "" || nome.value == " " || nome.value == undefined) {
        if (!nome.classList.contains("borda-alerta")) {
            lbNome.classList.add("txt-alerta")
            nome.classList.add("borda-alerta")
        }
        alerta = true;
    }

    if (celular.value == "" || celular.value == " " || celular.value == undefined) {
        if (!celular.classList.contains("borda-alerta")) {
            lbCelular.classList.add("txt-alerta")
            celular.classList.add("borda-alerta")
        }
        alerta = true;
    }

    if (email.value == "" || email.value == " " || email.value == undefined) {
        if (!email.classList.contains("borda-alerta")) {
            lbEmail.classList.add("txt-alerta")
            email.classList.add("borda-alerta")
        }
        alerta = true;
    }

    if (login.value == "" || login.value == " " || login.value == undefined) {
        if (!login.classList.contains("borda-alerta")) {
            lbLogin.classList.add("txt-alerta")
            login.classList.add("borda-alerta")
        }
        alerta = true;
    }

    if (alerta) evento.preventDefault()
}

nome.addEventListener('focusin', () => {
    if (nome.classList.contains('borda-alerta')) {
        nome.classList.remove('borda-alerta')
        lbNome.classList.remove('txt-alerta')
    }
})

celular.addEventListener('focusin', () => {
    if (celular.classList.contains('borda-alerta')) {
        celular.classList.remove('borda-alerta')
        lbCelular.classList.remove('txt-alerta')
    }
})

email.addEventListener('focusin', () => {
    if (email.classList.contains('borda-alerta')) {
        email.classList.remove('borda-alerta')
        lbEmail.classList.remove('txt-alerta')
    }
})

login.addEventListener('focusin', () => {
    if (login.classList.contains('borda-alerta')) {
        login.classList.remove('borda-alerta')
        lbLogin.classList.remove('txt-alerta')
    }
})
