// const dashboard =  fetch("http://127.0.0.1:5000/dashboard/carregamento")
// .then((response) => response.json()).then((data) => {
//     return data
// });

// const getData = async () => {
//     const informacao = await dashboard;
//     return informacao
// };

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