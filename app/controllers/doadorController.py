from app import flaskApp
from flask import render_template


@flaskApp.route('/novo-doador')
def novo_doador():
    return render_template("doadorNovo.html")


@flaskApp.route('/alterar-doador')
def alterar_doador():
    return render_template("doadorNovo.html", alterar=True)


@flaskApp.route('/alterar-inaptidao') # '/alterar_inatidao/<id>'
def alterar_inaptidao():
    return render_template("alterarInaptidao.html")


@flaskApp.route('/consultar-inaptidao') 
def consultar_inaptidao():
    return render_template("consultaDoadores.html")


@flaskApp.route('/consultar-inaptidao/resultado') 
def consultar_inaptidao_resultado():
    return render_template("consultaDoadores.html", resultado=True)


@flaskApp.route('/realatorio-doador') 
def relatorio_doador():
    return render_template("relatorioDoador.html")


@flaskApp.route('/realatorio-doador/id') # '/alterar_inatidao/<id>'
def detalhes_doador():
    return render_template("detalhesDoador.html")

