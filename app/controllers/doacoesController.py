from app import flaskApp
from flask import render_template


@flaskApp.route('/nova-doacao')
def nova_doacao():
    return render_template("doacao.html")


@flaskApp.route('/alterar-doacao') # '/alterar_doacao/<id>'
def alterar_doacao():
    return render_template("doacao.html", alterar=True)


@flaskApp.route('/detalhes-doacao/id')
def detalhes_doacao():
    return render_template("detalhesDoacao.html")


@flaskApp.route('/consultar-doacao') 
def consultar_doacao():
    return render_template("consultarDoacoes.html")


@flaskApp.route('/consultar-doacao/resultado') 
def consultar_doacao_resultado():
    return render_template("consultarDoacoes.html", resultado=True)

