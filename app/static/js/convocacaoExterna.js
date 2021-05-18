$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close')
})

var tipo = document.getElementById("tipagem")
var lbTipagem = document.getElementById("lbTipagem")
var municipio = document.getElementById("municipio")
var lbMunicipio = document.getElementById("lbMunicipio")


function validar(evento) {
    if (tipo.value == "null") {
        if (!tipo.classList.contains('borda-alerta')) {
            tipo.classList.add('borda-alerta')
            lbTipagem.classList.add('txt-alerta')
        }
        evento.preventDefault()
    }

    if (municipio.value == "null") {
        if (!municipio.classList.contains('borda-alerta')) {
            municipio.classList.add('borda-alerta')
            lbMunicipio.classList.add('txt-alerta')
        }
        evento.preventDefault()
    }

    if ( !estaContidoNoPadrao(estado, inputEstado) ) {
        if (!inputEstado.classList.contains('borda-alerta')) {
            inputEstado.classList.add('borda-alerta')
            lbEstado.classList.add('txt-alerta')
        }
        evento.preventDefault()
    }
    if ( !estaContidoNoPadrao(municipio, inputMunicipio) ) {
        if (!inputMunicipio.classList.contains('borda-alerta')) {
            inputMunicipio.classList.add('borda-alerta')
            lbMunicipio.classList.add('txt-alerta')
        }
        evento.preventDefault()
    }
}

function remover(elemento) {
    if (tipo.classList.contains('borda-alerta') && elemento == 'tipo') {
        tipo.classList.remove('borda-alerta')
        lbTipagem.classList.remove('txt-alerta')
    }

    if (municipio.classList.contains('borda-alerta') && elemento == 'municipio') {
        municipio.classList.remove('borda-alerta')
        lbMunicipio.classList.remove('txt-alerta')
    }
}

function adicionarPagina(valor) {
    document.getElementById("page").value = valor
}

function adicionarTelefonado(valor, evento) {
    let telefonados = document.getElementById("telefonados");
    if (!evento.target.classList.contains("azul")) {
        telefonados.value += valor + "&";
        evento.target.classList.add("azul");
    } else {
        telefonados.value = telefonados.value.replace(valor + "&", '');
        evento.target.classList.remove("azul");
    }
}