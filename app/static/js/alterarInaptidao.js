var dataInput = document.getElementById("data")
var lbData = document.getElementById("lbData")
var estado = document.getElementById("estadoAptidao")

bloquearData()

function verificarData(evento) {
    if (estado.value == "apto") return true;
    let dataAtual = new Date()

    let data = dataInput.value.split("/");
    
    let ano = data[2];
    let mes = data[1];
    let dia = data[0];
    
    var diasDoMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if ((!(ano % 4) && ano % 100) || !(ano % 400)) diasDoMes[1] = 29;
    
    if (mes <= 0 || mes > 12 || (dataAtual.getMonth() + 1) > mes || dataAtual.getFullYear() > ano) {
        evento.preventDefault()
        if (!dataInput.classList.contains('borda-alerta')) {
            dataInput.classList.add('borda-alerta')
            lbData.classList.add('txt-alerta')
        }
    };
    if (dia <= 0 || dia > diasDoMes[mes - 1]) {
        evento.preventDefault()
        if (!dataInput.classList.contains('borda-alerta')) {
            dataInput.classList.add('borda-alerta')
            lbData.classList.add('txt-alerta')
        }
    };
}

estado.addEventListener('focusout', bloquearData());

function removerClasse() {
    if (dataInput.classList.contains('borda-alerta')) {
        dataInput.classList.remove('borda-alerta')
        lbData.classList.remove('txt-alerta')
    }
}

function bloquearData(){
    if (estado.value == "apto") {
        dataInput.value = "";
        dataInput.readOnly = true;
    } else dataInput.readOnly = false;
}