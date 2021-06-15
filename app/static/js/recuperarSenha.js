var enviar = document.getElementById('enviar')
var email = document.getElementById('email')

enviar.addEventListener('click', (event) => {
    if (email.value == null || email.value == "" || email.value == " ") {
        event.preventDefault();
        if (!email.classList.contains("borda-alerta")) {
            email.classList.add("borda-alerta")
        }
    }
});

email.addEventListener('focus', () => {
    if (email.classList.contains("borda-alerta")) {
        email.classList.remove("borda-alerta")
    }
});