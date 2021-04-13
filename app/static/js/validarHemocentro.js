$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close');
});

function validarCampos(evento) {
    var nome = document.getElementById("nome")
    var lbNome = document.getElementById("lbNome")
    var telefone = document.getElementById("telefone")
    var lbTelefone = document.getElementById("lbTelefone")
    var municipio = document.getElementById("municipio")
    var lbMunicipio = document.getElementById("lbMunicipio")

    var alerta = false;

    if (nome.value == undefined || nome.value == null || nome.value == "" || nome.value == " ") {
        if (!nome.classList.contains('borda-alerta')) {
            nome.classList.add('borda-alerta')
            lbNome.classList.add('txt-alerta')
        }
        alerta = true;
    };
    if (telefone.value == undefined || telefone.value == null || telefone.value == "" || telefone.value == " ") {
        if (!telefone.classList.contains('borda-alerta')) {
            telefone.classList.add('borda-alerta')
            lbTelefone.classList.add('txt-alerta')
        }
        alerta = true;
    };
    if (municipio.value == 'selecione') {
        if (!municipio.classList.contains('borda-alerta')) {
            municipio.classList.add('borda-alerta')
            lbMunicipio.classList.add('txt-alerta')
        }
        alerta = true;
    };

    if (alerta) evento.preventDefault();
}

function removerClasseAlerta(elemento){
    if (nome.classList.contains('borda-alerta') && elemento == 'nome') {
        nome.classList.remove('borda-alerta')
        lbNome.classList.remove('txt-alerta')
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
    nome.value = ""
    telefone.value = ""
    document.getElementById("img").value = ""
    municipio.value = "selecione"
}