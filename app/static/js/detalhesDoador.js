var mostrando = false
var infoIco = document.getElementById("infoIco")
var infoCloseIco = document.getElementById("infoCloseIco")
var linhaMedia = document.getElementById("linhaMedia")
var linhaBaixa = document.getElementById("linhaBaixa")

function toggleInfo() {
    if (mostrando) {
        infoCloseIco.classList.add("escondido")
        infoIco.classList.remove("escondido")
        linhaMedia.classList.add("linhaSolitaria")
        linhaBaixa.classList.add("escondido")
        linhaBaixa.classList.remove("linhaSolitaria")
        mostrando = false
    } else {
        infoCloseIco.classList.remove("escondido")
        infoIco.classList.add("escondido")
        linhaMedia.classList.remove("linhaSolitaria")
        linhaBaixa.classList.add("linhaSolitaria")
        linhaBaixa.classList.remove("escondido")
        mostrando = true
    }
}