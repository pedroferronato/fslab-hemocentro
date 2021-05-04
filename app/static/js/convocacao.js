$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close')
})

var tipo = document.getElementById("tipagem")
var lbTipagem = document.getElementById("lbTipagem")

function validar(evento) {
    if (tipo.value == "null") {
        if (!tipo.classList.contains('borda-alerta')) {
            tipo.classList.add('borda-alerta')
            lbTipagem.classList.add('txt-alerta')
        }
        evento.preventDefault()
    }
}

function remover() {
    if (tipo.classList.contains('borda-alerta')) {
        tipo.classList.remove('borda-alerta')
        lbTipagem.classList.remove('txt-alerta')
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