from app import flaskApp, login_manager, db
from app.models.captador import Captador
from app.models.estado import Estado
from app.models.municipio import Municipio
from flask import render_template, redirect, request, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
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
            return redirect('/inicio')


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


@flaskApp.route('/inicio')
@login_required
def inicial():
    sucesso = request.args.get('sucesso')

    return render_template("paginaInicial.html", sucesso=sucesso)


@flaskApp.route('/perfil')
@login_required
def perfil():
    return render_template("perfil.html")


@flaskApp.route('/perfil', methods=['POST'])
@login_required
def alterar_perfil():
    nome = request.form['nome']
    celular = request.form['celular']
    email = request.form['email']
    login = request.form['login']

    captador = Captador.query.filter_by(id=current_user.id).first()
    
    if request.form['botao'] == "Atualizar cadastro":
        print("entrou")
        captador.nome = nome
        captador.celular = celular
        captador.email = email
        captador.login = login
        db.session.add(captador)
        db.session.commit()
        return render_template("perfil.html")
    if request.form['botao'] == "Excluir cadastro":
        db.session.delete(captador)
        db.session.commit()
        logout_user()
        return redirect('/login')



@flaskApp.route('/alterar-senha') # TODO: USAR ALGUMA FORMA DE IDENTIFICAÇÃO
def alterar_senha():
    return render_template("alterarSenha.html")

@flaskApp.route('/cidades/<estado>')
def get_cidade(estado):
    estado_id = Estado.query.filter_by(nome=estado).first().id
    cidades = Municipio.query.filter_by(uf=estado_id)
    cidades = [x.nome for x in cidades]
    return jsonify(cidades)
