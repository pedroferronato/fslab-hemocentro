from app import flaskApp
from flask import render_template
from flask_login import login_required


@flaskApp.route('/nova-doacao')
@login_required
def nova_doacao():
    return render_template("doacao.html")


@flaskApp.route('/alterar-doacao') # '/alterar_doacao/<id>'
@login_required
def alterar_doacao():
    return render_template("doacao.html", alterar=True)


@flaskApp.route('/detalhes-doacao/id')
@login_required
def detalhes_doacao():
    return render_template("detalhesDoacao.html")


@flaskApp.route('/consultar-doacao') 
@login_required
def consultar_doacao():
    return render_template("consultarDoacoes.html")


@flaskApp.route('/consultar-doacao/resultado') 
@login_required
def consultar_doacao_resultado():
    return render_template("consultarDoacoes.html", resultado=True)

