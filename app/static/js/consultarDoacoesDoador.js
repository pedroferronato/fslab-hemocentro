var nome = document.getElementById("nome")
var cpf = document.getElementById("cpf")
var numeroRegistro = document.getElementById("numeroRegistro")

function validar(evento) {
    if ( (nome.value == "" || nome.value == " " || nome.value == undefined) 
    && (cpf.value == "" || cpf.value == " " || cpf.value == undefined) 
    && (numeroRegistro.value == "" || numeroRegistro.value == " " || numeroRegistro.value == undefined)) {
        evento.preventDefault();
        $('#modal').modal('show');
    }
    if (!validarCPF() && (cpf.value != "" && cpf.value != undefined && cpf.value != " ")) {
        evento.preventDefault()
        if (!cpf.classList.contains('borda-alerta')) {
            cpf.classList.add('borda-alerta')
            lbCpf.classList.add('txt-alerta')
        }
    }
}

function validarCPF() {
    var Soma;
    var Resto;
    Soma = 0;
    let strCPF = cpf.value.replace(".", "").replace(".", "").replace("-", "")
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

function removerAlerta() {
    if (cpf.classList.contains('borda-alerta')) {
        cpf.classList.remove('borda-alerta')
        lbCpf.classList.remove('txt-alerta')
    }
}

function adicionarPagina(valor) {
    document.getElementById("page").value = valor
}