from app import flaskApp
from flask import render_template, request


@flaskApp.route('/login')
def login():
    return render_template("login.html")


@flaskApp.route('/recuperar-senha')
def recuperar_senha():
    return render_template("recuperarSenha.html")


@flaskApp.route('/inicio')
def inicial():
    sucesso = request.args.get('sucesso')

    return render_template("paginaInicial.html", sucesso=sucesso)


@flaskApp.route('/perfil')
def perfil():
    return render_template("perfil.html")


@flaskApp.route('/alterar-senha') # TODO: USAR ALGUMA FORMA DE IDENTIFICAÇÃO
def alterar_senha():
    return render_template("alterarSenha.html")

