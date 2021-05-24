from app import flaskApp, db, login_manager
from app.models.captador import Captador
from flask import render_template, redirect, request, url_for, session
from flask_login import login_user, logout_user, login_required
from datetime import timedelta
import bcrypt

@flaskApp.before_request
def make_session_permanent():
    session.permanent = True
    flaskApp.permanent_session_lifetime = timedelta(minutes=30)
    session.modified = True

@flaskApp.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        mensagem = request.args.get('mensagem')
        return render_template("login.html", mensagem=mensagem)

    elif request.method == 'POST':

        login = request.form['login']
        senha = request.form['senha']

        captador = Captador.query.filter_by(login=login).first()

        autorizado = False
        if captador:
            autorizado = bcrypt.checkpw(senha.encode('UTF-8'), captador.senha.encode('UTF-8'))
        
        if not captador or not autorizado:
            mensagem = "Login não autorizado"
            return render_template("login.html", mensagem=mensagem)
        else:
            login_user(captador, remember=False)
            return redirect('/')


@flaskApp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@login_manager.unauthorized_handler
def nao_autorizado():
    return redirect('/login')


@flaskApp.route('/recuperar-senha')
def recuperar_senha():
    return render_template("recuperarSenha.html")


@flaskApp.route('/')
@login_required
def inicial():
    sucesso = request.args.get('sucesso')

    return render_template("paginaInicial.html", sucesso=sucesso)


@flaskApp.route('/dashboard')
@login_required
def dashboard():

    return render_template("dashboard.html")


@flaskApp.route('/perfil')
@login_required
def perfil():
    return render_template("perfil.html")


@flaskApp.route('/alterar-senha') # TODO: USAR ALGUMA FORMA DE IDENTIFICAÇÃO
def alterar_senha():
    return render_template("alterarSenha.html")

