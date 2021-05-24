var nome = document.getElementById("nome");
var municipio = document.getElementById('municipio')
var estado = document.getElementById('estado')

function validarCampos(evento) {
    if ((nome.value == "" || nome.value == " " || nome.value == null) && (!estaContidoNoPadrao(estado, inputEstado) || !estaContidoNoPadrao(municipio, inputMunicipio) )) {
        evento.preventDefault()
        $('#exampleModal').modal('show');
    }
}

function limpar() {
    inputMunicipio.value = ""
    inputEstado.value = ""
    nome.value = ""
}

function estaContidoNoPadrao(datalist, input) {
    let encontrado = false;
    Array.from(datalist.children).forEach(element => {
        if (input.value == element.value) {
            encontrado = true;   
        }
    });
    if (encontrado) return true;
    return false;
}