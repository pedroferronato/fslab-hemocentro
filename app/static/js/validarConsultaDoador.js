var nome = document.getElementById("nome");
var tipo_sanguineo = document.getElementById("tipoSangue");
var numero_registro = document.getElementById("registro");
var municipio = document.getElementById("municipio");

function validarCampos(evento) {
    if ((nome.value == "" || nome.value == " " || nome.value == null)  && municipio.value == "null") {
        evento.preventDefault()
        $('#exampleModal').modal('show');
    }
}
