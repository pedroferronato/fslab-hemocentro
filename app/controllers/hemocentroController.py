from app import flaskApp, login_manager
from flask import render_template

@login_manager.user_loader
def get_user(id):
    return Captador.query.filter_by(id=id).first()


@flaskApp.route('/novo-hemocentro')
def novo_hemocentro():
    return render_template("hemocentro.html")


@flaskApp.route('/consultar-hemocentros') 
def consultar_hemocentro():
    return render_template("consultaHemocentro.html")


@flaskApp.route('/consultar-hemocentros/resultado') 
def consultar_hemocentro_resultado():
    return render_template("consultaHemocentro.html", resultado=True)
