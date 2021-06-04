
function getData() {
    let valores = document.getElementsByClassName("valor")
    let valoresLimpos = []
    Array.from(valores).forEach(element => {
        valoresLimpos.push(parseInt(element.innerHTML))
    });
    return valoresLimpos
}

var ctx = document.getElementsByClassName("grafico");

var chartGraph = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
        datasets: [
            {
                label: "DOAÇÕES 2021",
                data: getData(),
                backgroundColor: 'rgba(172,0,17,0.85)',
            },
        ]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: "RELATÓRIO DE DOAÇÃO ANUAL",
                font: {
                    size: 36,
                }
            },
            legend: {
                display: false,
            }
        }
    },
});

var pizza = document.getElementById("pizza");

var chartPizza = new Chart(pizza, {
    type: 'doughnut',
    data: {
        labels: ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
        datasets: [
            {
                label: "DOAÇÕES 2021",
                data: getData(),
                backgroundColor: [
                 '#71F77F',
                 '#13751D',
                 '#9195F7',
                 '#222575',
                 '#F77D76',
                 '#751A15',
                 '#F7EA7B',
                 '#756C17',
                ]
            },
        ]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: "Doações por tipo",
                font: {
                    size: 24,
                }
            },
            legend: {
                display: true,
            }
        }
    },
});

