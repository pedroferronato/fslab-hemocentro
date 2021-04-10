from app import flaskApp
from flask import render_template


@flaskApp.route('/login')
def login():
    return render_template("login.html")


@flaskApp.route('/recuperar-senha')
def recuperar_senha():
    return render_template("recuperarSenha.html")


@flaskApp.route('/')
def inicial():
    return render_template("paginaInicial.html")

