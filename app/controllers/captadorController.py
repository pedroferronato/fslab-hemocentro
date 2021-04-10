from app import flaskApp, login_manager
from flask import render_template

@login_manager.user_loader
def get_user(id):
    return Captador.query.filter_by(id=id).first()


@flaskApp.route('/novo-captador')
def novo_captador():
    return render_template("captador.html")
