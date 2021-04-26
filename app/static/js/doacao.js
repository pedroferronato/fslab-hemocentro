
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

function validarCampo(evento) {
    alerta = false

    if (!cpf.value == undefined || !cpf.value == null || !cpf.value == "" || !cpf.value == " ") {
        if (!validarCPF(cpf.value)){
            if (!cpf.classList.contains('borda-alerta')) {
                cpf.classList.add('borda-alerta')
            }
            alerta = true;   
        }
        
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
    
    if (data.value == undefined || data.value == null || data.value == "" || data.value == " "|| (data.value.length > 0 && data.value.length <= 9) || !validarData(data.value, true)) {
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

function validarCPF(cpfValidar) {
    var Soma;
    var Resto;
    Soma = 0;
    let strCPF = cpfValidar.replace(".", "").replace(".", "").replace("-", "")
    if (strCPF == "00000000000" || strCPF == "11111111111" || strCPF == "22222222222" || strCPF == "33333333333" || strCPF == "44444444444" || strCPF == "55555555555" || strCPF == "66666666666" || strCPF == "77777777777" || strCPF == "88888888888" || strCPF == "99999999999") return false;

    for (i = 1; i <= 9; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10))) return false;

    Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11))) return false;
    return true;
}

function validarData(vardata, nasc) {
    let data = vardata.split("/");
    let ano = data[2];
    let mes = data[1];
    let dia = data[0];

    var diasDoMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if ((!(ano % 4) && ano % 100) || !(ano % 400)) diasDoMes[1] = 29;
    
    if (mes <= 0 || mes > 12) return false
    if (dia <= 0 || dia > diasDoMes[mes - 1]) return false;
    if (nasc) if (ano > new Date().getFullYear()) return false;

    return true;
}