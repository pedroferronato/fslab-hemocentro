$(".alert").delay(2000).slideUp(200, function () {
    $(this).alert('close');
});

function validarCampos(evento) {
    var numRegistro = document.getElementById("numRegistro")
    var lbNumRegistro = document.getElementById("lbNumRegistro")
    var nome = document.getElementById("nome")
    var lbNome = document.getElementById("lbNome")
    var cpf = document.getElementById("cpf")
    var lbCpf = document.getElementById("lbCpf")
    var sexo = document.getElementById("sexo")
    var lbSexo = document.getElementById("lbSexo")
    var tipoSangue = document.getElementById("tipoSangue")
    var lbTipoSangue = document.getElementById("lbTipoSangue")
    var nascimento = document.getElementById("nascimento")
    var lbNascimento = document.getElementById("lbNascimento")
    var sus = document.getElementById("sus")
    var lbSus = document.getElementById("lbSus")
    var telefone = document.getElementById("telefone")
    var lbTelefone = document.getElementById("lbTelefone")
    var municipio = document.getElementById("municipio")
    var lbMunicipio = document.getElementById("lbMunicipio")


    var alerta = false;

    if (numRegistro.value == undefined || numRegistro.value == null || numRegistro.value == "" || numRegistro.value == " ") {
        if (!numRegistro.classList.contains('borda-alerta')) {
            numRegistro.classList.add('borda-alerta')
            lbNumRegistro.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (nome.value == undefined || nome.value == null || nome.value == "" || nome.value == " ") {
        if (!nome.classList.contains('borda-alerta')) {
            nome.classList.add('borda-alerta')
            lbNome.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (cpf.value == undefined || cpf.value == null || cpf.value == "" || cpf.value == " ") {
        if (!cpf.classList.contains('borda-alerta')) {
            cpf.classList.add('borda-alerta')
            lbCpf.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (sexo.value == 'selecione') {
        if (!sexo.classList.contains('borda-alerta')) {
            sexo.classList.add('borda-alerta')
            lbSexo.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (tipoSangue.value == 'selecione') {
        if (!tipoSangue.classList.contains('borda-alerta')) {
            tipoSangue.classList.add('borda-alerta')
            lbTipoSangue.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (nascimento.value == undefined || nascimento.value == null || nascimento.value == "" || nascimento.value == " ") {
        if (!nascimento.classList.contains('borda-alerta')) {
            nascimento.classList.add('borda-alerta')
            lbNascimento.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (sus.value == undefined || sus.value == null || sus.value == "" || sus.value == " ") {
        if (!sus.classList.contains('borda-alerta')) {
            sus.classList.add('borda-alerta')
            lbSus.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (telefone.value == undefined || telefone.value == null || telefone.value == "" || telefone.value == " ") {
        if (!telefone.classList.contains('borda-alerta')) {
            telefone.classList.add('borda-alerta')
            lbTelefone.classList.add('txt-alerta')
        }
        alerta = true;
    }
    if (municipio.value == 'selecione') {
        if (!municipio.classList.contains('borda-alerta')) {
            municipio.classList.add('borda-alerta')
            lbMunicipio.classList.add('txt-alerta')
        }
        alerta = true;
    }

    if (alerta) evento.preventDefault()
}

function removerClasseAlerta(elemento) {
    if (numRegistro.classList.contains('borda-alerta') && elemento == 'numRegistro') {
        numRegistro.classList.remove('borda-alerta')
        lbNumRegistro.classList.remove('txt-alerta')
    }
    if (nome.classList.contains('borda-alerta') && elemento == 'nome') {
        nome.classList.remove('borda-alerta')
        lbNome.classList.remove('txt-alerta')
    }
    if (cpf.classList.contains('borda-alerta') && elemento == 'cpf') {
        cpf.classList.remove('borda-alerta')
        lbCpf.classList.remove('txt-alerta')
    }
    if (sexo.classList.contains('borda-alerta') && elemento == 'sexo') {
        sexo.classList.remove('borda-alerta')
        lbSexo.classList.remove('txt-alerta')
    }
    if (tipoSangue.classList.contains('borda-alerta') && elemento == 'tipoSangue') {
        tipoSangue.classList.remove('borda-alerta')
        lbTipoSangue.classList.remove('txt-alerta')
    }
    if (nascimento.classList.contains('borda-alerta') && elemento == 'nascimento') {
        nascimento.classList.remove('borda-alerta')
        lbNascimento.classList.remove('txt-alerta')
    }
    if (sus.classList.contains('borda-alerta') && elemento == 'sus') {
        sus.classList.remove('borda-alerta')
        lbSus.classList.remove('txt-alerta')
    }
    if (telefone.classList.contains('borda-alerta') && elemento == 'telefone') {
        telefone.classList.remove('borda-alerta')
        lbTelefone.classList.remove('txt-alerta')
    }
    if (municipio.classList.contains('borda-alerta') && elemento == 'municipio') {
        municipio.classList.remove('borda-alerta')
        lbMunicipio.classList.remove('txt-alerta')
    }
}

function limpar() {
    numRegistro.value = ""
    nome.value = ""
    cpf.value = ""
    sexo.value = "selecione"
    tipoSangue.value = "selecione"
    nascimento.value = ""
    sus.value = ""
    estadoCivil.value = ""
    celular.value = ""
    telefone.value = ""
    mail.value = ""
    aviso.value = "selecione"
    municipio.value = "selecione"
    profissao.value = ""
    localTrabalho.value = ""
    estadoAptidao.value = "selecione"
    dataInaptidao.value = ""
    mae.value = ""
    pai.value = ""
}


function adicionarCidade() {
    let numRegistroSafe = document.getElementById("numRegistroSafe")
    let nomeSafe = document.getElementById("nomeSafe")
    let cpfSafe = document.getElementById("cpfSafe")
    let sexoSafe = document.getElementById("sexoSafe")
    let tipoSangueSafe = document.getElementById("tipoSangueSafe")
    let nascimentoSafe = document.getElementById("nascimentoSafe")
    let susSafe = document.getElementById("susSafe")
    let estadoCivilSafe = document.getElementById("estadoCivilSafe")
    let celularSafe = document.getElementById("celularSafe")
    let telefoneSafe = document.getElementById("telefoneSafe")
    let mailSafe = document.getElementById("mailSafe")
    let avisoSafe = document.getElementById("avisoSafe")
    let profissaoSafe = document.getElementById("profissaoSafe")
    let localTrabalhoSafe = document.getElementById("localTrabalhoSafe")
    let estadoAptidaoSafe = document.getElementById("estadoAptidaoSafe")
    let dataInaptidaoSafe = document.getElementById("dataInaptidaoSafe")
    let maeSafe = document.getElementById("maeSafe")
    let paiSafe = document.getElementById("paiSafe")

    numRegistroSafe.value = numRegistro.value
    nomeSafe.value = nome.value
    cpfSafe.value = cpf.value
    sexoSafe.value = sexo.value
    tipoSangueSafe.value = tipoSangueSafe.value
    nascimentoSafe.value = nascimento.value
    susSafe.value = sus.value
    estadoCivilSafe.value = estadoCivil.value
    celularSafe.value = celular.value
    telefoneSafe.value = telefone.value
    mailSafe.value = mail.value
    avisoSafe.value = aviso.value
    profissaoSafe.value = profissaoSafe.value
    localTrabalhoSafe.value = localTrabalho.value
    estadoAptidaoSafe.value = estadoAptidao.value
    dataInaptidaoSafe.value = dataInaptidao.value
    maeSafe.value = mae.value
    paiSafe.value = pai.value

    $(addCidade).modal('show');
}
