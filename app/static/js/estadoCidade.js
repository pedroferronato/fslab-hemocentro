var municipio = document.getElementById('municipio')
var estado = document.getElementById('estado')

var inputEstado = document.getElementById("inputEstado")
var lbEstado = document.getElementById("lbEstado")

var inputMunicipio = document.getElementById("inputMunicipio")
var lbMunicipio = document.getElementById("lbMunicipio")

$('#inputEstado').focusout(function () {
    if ( estaContidoNoPadrao(estado, inputEstado) ) {
        municipio.innerHTML = ""
        getCidades().then(resposta => {
            resposta.forEach(element => {
                var option = document.createElement('option');
                option.value = element;
                municipio.appendChild(option);
            });
        });
    } else {
        inputEstado.classList.add('borda-alerta')
        lbEstado.classList.add('txt-alerta')
    }
});

$('#inputMunicipio').focusout(function () {
    if ( !estaContidoNoPadrao(municipio, inputMunicipio) ) {
        inputMunicipio.classList.add('borda-alerta')
        lbMunicipio.classList.add('txt-alerta')
    }
});

inputEstado.addEventListener('focusin', () => {
    if (inputEstado.classList.contains('borda-alerta')) {
        inputEstado.classList.remove('borda-alerta')
        lbEstado.classList.remove('txt-alerta')
    }
})

inputMunicipio.addEventListener('focusin', () => {
    if (inputMunicipio.classList.contains('borda-alerta')) {
        inputMunicipio.classList.remove('borda-alerta')
        lbMunicipio.classList.remove('txt-alerta')
    }
})

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

async function getCidades() {
    var urlCidades = "http://127.0.0.1:5000/cidades/" + inputEstado.value;
    let response = await fetch(urlCidades);
    let data = await response.json();
    return data;
}