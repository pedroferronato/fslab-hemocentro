$(".alert").delay(2000).slideUp(200, function() {
    $(this).alert('close')
})

var nome = document.getElementById("nome");
var tipoSanguineo = document.getElementById("tipoSangue");
var numeroRegistro = document.getElementById("registro");
var municipio = document.getElementById("municipio");

function validarCampos(evento) {
    if ((nome.value == "" || nome.value == " " || nome.value == null) && municipio.value == "null" && tipoSanguineo.value == "null" && (numeroRegistro.value == "" || numeroRegistro.value == " " || numeroRegistro.value == null)) {
        $('#exampleModal').modal('show');
        evento.preventDefault()
    }
}
