from app import flaskApp
from flask import render_template


@flaskApp.route('/novo-doador')
@login_required
def novo_doador():
    return render_template("doador.html")


@flaskApp.route('/alterar-doador')
@login_required
def alterar_doador():
    return render_template("doador.html", alterar=True)


@flaskApp.route('/alterar-inaptidao') # '/alterar_inatidao/<id>'
@login_required
def alterar_inaptidao():
    return render_template("alterarInaptidao.html")


@flaskApp.route('/consultar-inaptidao') 
@login_required
def consultar_inaptidao():
    return render_template("consultaDoadores.html")


@flaskApp.route('/consultar-inaptidao/resultado') 
@login_required
def consultar_inaptidao_resultado():
    return render_template("consultaDoadores.html", resultado=True)


@flaskApp.route('/realatorio-doador') 
@login_required
def relatorio_doador():
    return render_template("relatorioDoador.html")


@flaskApp.route('/realatorio-doador/id') # '/alterar_inatidao/<id>'
@login_required
def detalhes_doador():
    return render_template("detalhesDoador.html")

