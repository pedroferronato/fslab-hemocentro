var cpf = document.getElementById("cpf")
var lbCpf = document.getElementById("lbCpf")

function removerAlerta() {
    if (cpf.classList.contains('borda-alerta')) {
        cpf.classList.remove('borda-alerta')
        lbCpf.classList.remove('txt-alerta')
    }
}