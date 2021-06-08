$(".alert2").delay(5000).slideUp(200, function() {
    $(this).alert('close')
})

$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close')
})

function predefinicaoPersonalizado() {
    $('#predefinicoes').val("personalizado");
}

function setarData(dataSelect) {
    let data = new Date();
    let dataHoje = new Date();

    if (dataSelect.value == "ontem") {
        data.setDate(data.getDate() - 1);
        let diaData = data.getDate()
        let mesData = data.getMonth() + 1
        if (diaData < 10) {
            diaData = "0"+diaData
        }
        if (mesData < 10) {
            mesData = "0"+mesData
        }

        let dataFormatada = diaData + "/" + mesData + "/" + data.getFullYear();
        $('.data').val(dataFormatada);
        return
    }
    
    if (dataSelect.value == "anteontem") {
        data.setDate(data.getDate() - 2);
        let diaData = data.getDate()
        let mesData = data.getMonth() + 1
        if (diaData < 10) {
            diaData = "0"+diaData
        }
        if (mesData < 10) {
            mesData = "0"+mesData
        }

        let dataFormatada = diaData + "/" + mesData + "/" + data.getFullYear();
        $('.data').val(dataFormatada);
        return
    }

    if (dataSelect.value == "dois" || dataSelect.value == "sete" || dataSelect.value == "dez") {
        if (dataSelect.value == "dois") {
            data.setDate(data.getDate() - 1);
            let diaData = data.getDate()
            let mesData = data.getMonth() + 1
            if (diaData < 10) {
                diaData = "0"+diaData
            }
            if (mesData < 10) {
                mesData = "0"+mesData
            }

            let dataFormatada = diaData + "/" + mesData + "/" + data.getFullYear();
            $('#data').val(dataFormatada);
        }

        if (dataSelect.value == "sete") {
            data.setDate(data.getDate() - 6);
            let diaData = data.getDate()
            let mesData = data.getMonth() + 1
            if (diaData < 10) {
                diaData = "0"+diaData
            }
            if (mesData < 10) {
                mesData = "0"+mesData
            }

            let dataFormatada = diaData + "/" + mesData + "/" + data.getFullYear();
            $('#data').val(dataFormatada);
        }

        if (dataSelect.value == "dez") {
            data.setDate(data.getDate() - 9);
            let diaData = data.getDate()
            let mesData = data.getMonth() + 1
            if (diaData < 10) {
                diaData = "0"+diaData
            }
            if (mesData < 10) {
                mesData = "0"+mesData
            }

            let dataFormatada = diaData + "/" + mesData + "/" + data.getFullYear();
            $('#data').val(dataFormatada);
        }

        dataHoje.setDate(dataHoje.getDate());
        let diaDataHoje = dataHoje.getDate();
        let mesDataHoje = dataHoje.getMonth() + 1;
        if (diaDataHoje < 10) {
            diaDataHoje = "0"+diaDataHoje;
        }
        if (mesDataHoje < 10) {
            mesDataHoje = "0"+mesDataHoje;
        }

        let dataFormatadaHoje = diaDataHoje + "/" + mesDataHoje + "/" + dataHoje.getFullYear();
        $('#dataFinal').val(dataFormatadaHoje);
        return
    }

}

var alerta = false

function validarData(vardata) {
    let data = vardata.split("/");

    let ano = data[2];
    let mes = data[1];
    let dia = data[0];

    var diasDoMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if ((!(ano % 4) && ano % 100) || !(ano % 400)) diasDoMes[1] = 29;
    
    if (mes <= 0 || mes > 12) return false
    if (dia <= 0 || dia > diasDoMes[mes - 1]) return false;

    return true;
}

function validarConsultaDoacao(evento){
    var predefinicoes = document.getElementById("predefinicoes")
    var data = document.getElementById("data")
    var lbData = document.getElementById("lbData")
    var dataFinal = document.getElementById("dataFinal")
    var lbDataFinal = document.getElementById("lbDataFinal")
    let vPredefinicao = true
    let vDataInicial = true
    let vDataFinal = true
    alerta = false

    if (predefinicoes.value == "null") {
        vPredefinicao = false
    } else {
        if (!validarData(data.value) || data.value.length < 10){
            data.classList.add('borda-alerta')
            lbData.classList.add('txt-alerta')
            alerta = true
        }
        
        if (!validarData(dataFinal.value) || dataFinal.value.length < 10){
            dataFinal.classList.add('borda-alerta')
            lbDataFinal.classList.add('txt-alerta')
            alerta = true
        }
        if (alerta) return evento.preventDefault()
    }

    if (data.value == undefined || data.value == null || data.value == "" || data.value == " ") vDataInicial = false
    if (dataFinal.value == undefined || dataFinal.value == null || dataFinal.value == "" || dataFinal.value == " ") vDataFinal = false
    
    if (!vPredefinicao && !vDataInicial || !vDataFinal){
        $(erroUm).modal('show');
        return evento.preventDefault()
    }

    let dataInicialSplit = data.value.split('/');
    let dataFinalSplit = dataFinal.value.split('/');
    let dataInicialFormato = ''+dataInicialSplit[2]+'-'+dataInicialSplit[1]+'-'+dataInicialSplit[0]+''
    let dataFinalFormato = ''+dataFinalSplit[2]+'-'+dataFinalSplit[1]+'-'+dataFinalSplit[0]+''
    let dataInicialFormatoDate = new Date(dataInicialFormato)
    let dataFinalFormatoDate = new Date(dataFinalFormato)

    if (dataInicialFormatoDate.getTime() > dataFinalFormatoDate.getTime()){
        $(erroDois).modal('show');
        return evento.preventDefault()
    }
    
    if ((dataFinalFormatoDate - dataInicialFormatoDate) > 31622400000) {
        $(erroTres).modal('show');
        return evento.preventDefault()
    }

}

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

    var lbCpf = document.getElementById("lbCpf")

    if (!cpf.value == undefined || !cpf.value == null || !cpf.value == "" || !cpf.value == " ") {
        if (!validarCPF(cpf.value)){
            if (!cpf.classList.contains('borda-alerta')) {
                cpf.classList.add('borda-alerta')
                lbCpf.classList.add('txt-alerta')
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
    let hoje = new Date()
    let dataSuperiorAAtual = hoje.getDate() < data.value.split('/')[0] || hoje.getMonth() + 1 < data.value.split('/')[1] || hoje.getFullYear() < data.value.split('/')[2];
    
    if (data.value == undefined || data.value == null || data.value == "" || data.value == " "|| (data.value.length > 0 && data.value.length <= 9) || !validarData(data.value, true) || dataSuperiorAAtual) {
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

}

function removerClasseAlertaDoacoes(elemento){
    if (data.classList.contains('borda-alerta') && elemento == 'data') {
        data.classList.remove('borda-alerta')
        lbData.classList.remove('txt-alerta')
    }

    if (dataFinal.classList.contains('borda-alerta') && elemento == 'dataFinal') {
        dataFinal.classList.remove('borda-alerta')
        lbDataFinal.classList.remove('txt-alerta')
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

function adicionarPagina(valor) {
    document.getElementById("page").value = valor
}