var app = new Vue({
    el: '#sobrepor',
    data: {
        opcoes: {
            'doacoes' : false,
            'doadores' : false,
            'chamadas' : false,
            'hemocentros' : false,
            'captadores' : false,
        }
    },
    methods: {
        toggle: function (chaveCategoria) {
            this.opcoes[chaveCategoria] = !this.opcoes[chaveCategoria];
            for (var op in this.opcoes) if (chaveCategoria != op) this.opcoes[op] = false;
        }
    }
})
