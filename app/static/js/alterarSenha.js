var pass1 = document.getElementById("password1")
var pass2 = document.getElementById("password2")

var botao = document.getElementById("botao")

var alerta = document.getElementsByClassName("descricao")

botao.addEventListener('click', (event) => {
    if ( (pass1.value == null || pass1.value == '' || pass1.value == ' ') || (pass2.value == null || pass2.value == '' || pass2.value == ' ') ) {
        event.preventDefault()
        if (!pass1.classList.contains("borda-alerta")) {
            pass1.classList.add("borda-alerta")
        }
        if (!pass2.classList.contains("borda-alerta")) {
            pass2.classList.add("borda-alerta")
        }
    }
    if (pass1.value != pass2.value) {
        event.preventDefault()
        if (!pass1.classList.contains("borda-alerta")) {
            pass1.classList.add("borda-alerta")
        }
        if (!pass2.classList.contains("borda-alerta")) {
            pass2.classList.add("borda-alerta")
        }
        if (!alerta[0].classList.contains("txt-alerta")) {
            alerta[0].classList.add("txt-alerta")
        }
    } 
})

pass1.addEventListener('focus', () => {
    if (pass1.classList.contains("borda-alerta")) {
        pass1.classList.remove("borda-alerta")
    }
    if (alerta[0].classList.contains("txt-alerta")) {
        alerta[0].classList.remove("txt-alerta")
    }
});

pass2.addEventListener('focus', () => {
    if (pass2.classList.contains("borda-alerta")) {
        pass2.classList.remove("borda-alerta")
    }
    if (alerta[0].classList.contains("txt-alerta")) {
        alerta[0].classList.remove("txt-alerta")
    }
});