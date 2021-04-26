
$(".alert2").delay(5000).slideUp(200, function() {
    $(this).alert('close')
})

$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close')
})


var alerta = false

function validarCampoPesquisa(evento){
    var pesquisa = document.getElementById("pesquisa")
    alerta = false

    if (pesquisa.value == undefined || pesquisa.value == null || pesquisa.value == "" || pesquisa.value == " ") {
        if (!pesquisa.classList.contains('borda-alerta')) {
            pesquisa.classList.add('borda-alerta')
        }
        alerta = true
    }
    
    if (alerta) evento.preventDefault()
}


function validarCampos(evento) {
    alerta = false
    
    var numRegistro = document.getElementById("numRegistro")
    var lbRegistro = document.getElementById("lbRegistro")
    var nome = document.getElementById("nome")
    var lbNome = document.getElementById("lbNome")
    var tipoSangue = document.getElementById("tipoSangue")
    var lbTipo = document.getElementById("lbTipo")
    var data = document.getElementById("data")
    var lbData = document.getElementById("lbData")
    var fidelidade = document.getElementById("fidelidade")
    var lbFidelidade = document.getElementById("lbFidelidade")
    var convocacao = document.getElementById("convocacao")
    var lbConvocacao = document.getElementById("lbConvocacao")

    if (numRegistro.value == undefined || numRegistro.value == null || numRegistro.value == "" || numRegistro.value == " ") {
        if (!numRegistro.classList.contains('borda-alerta')) {
            numRegistro.classList.add('borda-alerta')
            lbRegistro.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (nome.value == undefined || nome.value == null || nome.value == "" || nome.value == " ") {
        if (!nome.classList.contains('borda-alerta')) {
            nome.classList.add('borda-alerta')
            lbNome.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (tipoSangue.value == undefined || tipoSangue.value == null || tipoSangue.value == "" || tipoSangue.value == " ") {
        if (!tipoSangue.classList.contains('borda-alerta')) {
            tipoSangue.classList.add('borda-alerta')
            lbTipo.classList.add('txt-alerta')
        }
        alerta = true
    }
    
    if (data.value == undefined || data.value == null || data.value == "" || data.value == " ") {
        if (!data.classList.contains('borda-alerta')) {
            data.classList.add('borda-alerta')
            lbData.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (fidelidade.value == "Selecione") {
        if (!fidelidade.classList.contains('borda-alerta')) {
            fidelidade.classList.add('borda-alerta')
            lbFidelidade.classList.add('txt-alerta')
        }
        alerta = true
    }

    if (convocacao.value == "Selecione") {
        if (!convocacao.classList.contains('borda-alerta')) {
            convocacao.classList.add('borda-alerta')
            lbConvocacao.classList.add('txt-alerta')
        }
        alerta = true
    }
    
    if (alerta) evento.preventDefault()
}

function removerClasseAlerta(elemento){
    if (numRegistro.classList.contains('borda-alerta') && elemento == 'numRegistro') {
        numRegistro.classList.remove('borda-alerta')
        lbRegistro.classList.remove('txt-alerta')
    }

    if (nome.classList.contains('borda-alerta') && elemento == 'nome') {
        nome.classList.remove('borda-alerta')
        lbNome.classList.remove('txt-alerta')
    }

    if (tipoSangue.classList.contains('borda-alerta') && elemento == 'tipoSangue') {
        tipoSangue.classList.remove('borda-alerta')
        lbTipo.classList.remove('txt-alerta')
    }

    if (data.classList.contains('borda-alerta') && elemento == 'data') {
        data.classList.remove('borda-alerta')
        lbData.classList.remove('txt-alerta')
    }

    if (fidelidade.classList.contains('borda-alerta') && elemento == 'fidelidade') {
        fidelidade.classList.remove('borda-alerta')
        lbFidelidade.classList.remove('txt-alerta')
    }

    if (convocacao.classList.contains('borda-alerta') && elemento == 'convocacao') {
        convocacao.classList.remove('borda-alerta')
        lbConvocacao.classList.remove('txt-alerta')
    }

    if (pesquisa.classList.contains('borda-alerta') && elemento == 'pesquisa') {
        pesquisa.classList.remove('borda-alerta')
    }

}

function limpar() {
    numRegistro.value = ""
    nome.value = ""
    tipoSangue.value = ""
    data.value = ""
    fidelidade.value = "Selecione"
    convocacao.value = "Selecione"
    observacoes.value = ""
}