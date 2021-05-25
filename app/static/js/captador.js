$(".alert2").delay(5000).slideUp(200, function() {
    $(this).alert('close')
})

$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close')
})

function validarCampos(evento) {
    var nome = document.getElementById("nome")
    var lbNome = document.getElementById("lbNome")
    var celular = document.getElementById("celular")
    var lbCelular = document.getElementById("lbCelular")
    var hemocentro = document.getElementById("hemocentro")
    var lbHemocentro = document.getElementById("lbHemocentro")
    var mail = document.getElementById("mail")
    var lbMail = document.getElementById("lbMail")
    var login = document.getElementById("login")
    var lbLogin = document.getElementById("lbLogin")
    if (document.getElementById("senha")){
        var senha = document.getElementById("senha")
        var lbSenha = document.getElementById("lbSenha")
        var confirmarSenha = document.getElementById("confirmarSenha")
        var lbConfirmarSenha = document.getElementById("lbConfirmarSenha")
    }

    var alerta = false

    if (nome.value == undefined || nome.value == null || nome.value == "" || nome.value == " ") {
        if (!nome.classList.contains('borda-alerta')) {
            nome.classList.add('borda-alerta')
            lbNome.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (celular.value == undefined || celular.value == null || celular.value == "" || celular.value == " ") {
        if (!celular.classList.contains('borda-alerta')) {
            celular.classList.add('borda-alerta')
            lbCelular.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (hemocentro.value == "Selecione") {
        if (!hemocentro.classList.contains('borda-alerta')) {
            hemocentro.classList.add('borda-alerta')
            lbHemocentro.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (mail.value == undefined || mail.value == null || mail.value == "" || mail.value == " ") {
        if (!mail.classList.contains('borda-alerta')) {
            mail.classList.add('borda-alerta')
            lbMail.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (login.value == undefined || login.value == null || login.value == "" || login.value == " ") {
        if (!login.classList.contains('borda-alerta')) {
            login.classList.add('borda-alerta')
            lbLogin.classList.add('txt-alerta')
        }
        alerta = true
    }
    
    if (document.getElementById("senha")){

    if (senha.value == undefined || senha.value == null || senha.value == "" || senha.value == " ") {
        if (!senha.classList.contains('borda-alerta')) {
            senha.classList.add('borda-alerta')
            lbSenha.classList.add('txt-alerta')
        }
        alerta = true
    }
    
    if (confirmarSenha.value == undefined || confirmarSenha.value == null || confirmarSenha.value == "" || confirmarSenha.value == " ") {
        if (!confirmarSenha.classList.contains('borda-alerta')) {
            confirmarSenha.classList.add('borda-alerta')
            lbConfirmarSenha.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (senha.value != confirmarSenha.value) {
        if (!senha.classList.contains('borda-alerta')) {
            senha.classList.add('borda-alerta')
            lbSenha.classList.add('txt-alerta')
        }
        if (!confirmarSenha.classList.contains('borda-alerta')) {
            confirmarSenha.classList.add('borda-alerta')
            lbConfirmarSenha.classList.add('txt-alerta')
        }
        alerta = true
    }

    }

    if (alerta) evento.preventDefault()
}

function removerClasseAlerta(elemento){
    if (nome.classList.contains('borda-alerta') && elemento == 'nome') {
        nome.classList.remove('borda-alerta')
        lbNome.classList.remove('txt-alerta')
    }

    if (celular.classList.contains('borda-alerta') && elemento == 'celular') {
        celular.classList.remove('borda-alerta')
        lbCelular.classList.remove('txt-alerta')
    }

    if (hemocentro.classList.contains('borda-alerta') && elemento == 'hemocentro') {
        hemocentro.classList.remove('borda-alerta')
        lbHemocentro.classList.remove('txt-alerta')
    }

    if (mail.classList.contains('borda-alerta') && elemento == 'mail') {
        mail.classList.remove('borda-alerta')
        lbMail.classList.remove('txt-alerta')
    }

    if (login.classList.contains('borda-alerta') && elemento == 'login') {
        login.classList.remove('borda-alerta')
        lbLogin.classList.remove('txt-alerta')
    }

    if (senha.classList.contains('borda-alerta') && elemento == 'senha') {
        senha.classList.remove('borda-alerta')
        lbSenha.classList.remove('txt-alerta')
    }

    if (confirmarSenha.classList.contains('borda-alerta') && elemento == 'confirmarSenha') {
        confirmarSenha.classList.remove('borda-alerta')
        lbConfirmarSenha.classList.remove('txt-alerta')
    }
}

function limpar() {
    nome.value = ""
    celular.value = ""
    mail.value = ""
    login.value = ""
    senha.value = ""
    confirmarSenha.value = ""
    adm.value = "Captador"
}