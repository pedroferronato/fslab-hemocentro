from app import flaskApp, login_manager
from flask import render_template


@flaskApp.route('/novo-hemocentro')
def novo_hemocentro():
    return render_template("hemocentro.html")


@flaskApp.route('/alterar-hemocentro')
def alterar_hemocentro():
    return render_template("hemocentro.html", alterar=True)


@flaskApp.route('/consultar-hemocentros') 
def consultar_hemocentro():
    return render_template("consultaHemocentro.html")


@flaskApp.route('/consultar-hemocentros/resultado') 
def consultar_hemocentro_resultado():
    return render_template("consultaHemocentro.html", resultado=True)

