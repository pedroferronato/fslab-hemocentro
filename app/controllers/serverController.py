from app import flaskApp, db, login_manager
from app.models.utilidadeSistema import Utilidades
from app.models.captador import Captador
from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required
import bcrypt


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
            login_user(captador)
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


@flaskApp.route('/alterar-senha') # TODO: USAR ALGUMA FORMA DE IDENTIFICAÇÃO
def alterar_senha():
    return render_template("alterarSenha.html")


@flaskApp.route("/cidade/nova", methods=['POST'])
@login_required
def nova_cidade():
    nome_cidade = request.form['novaCidade']
    registradas = Utilidades.query.filter_by(cidade_registrada=nome_cidade)
    nome = request.form['nomeSafe']
    telefone = request.form['telefoneSafe']
    img = request.form['imgSafe']
    if registradas.count() == 0:
        cidade_nova = Utilidades(cidade_registrada=nome_cidade)
        db.session.add(cidade_nova)
        db.session.commit()
        return redirect(url_for('novo_hemocentro', reload=True, nomeBKP=nome, telefoneBKP=telefone, imgBKP=img, cidade_adicionada=nome_cidade))
    else:
        return redirect(url_for('novo_hemocentro', nomeBKP=nome, telefoneBKP=telefone, imgBKP=img))


# @flaskApp.route("/cidades/nova", methods=['POST'])
# def nova_cidade():
#     nome_cidade = request.form['novaCidade']
#     registradas = Utilidades.query.filter_by(cidade_registrada=nome_cidade)
#     nome = request.form['nomeSafe']
#     telefone = request.form['telefoneSafe']
#     img = request.form['imgSafe']
#     if registradas.count() == 0:
#         cidade_nova = Utilidades(cidade_registrada=nome_cidade)
#         db.session.add(cidade_nova)
#         db.session.commit()
#         return redirect(url_for('novo_hemocentro', reload=True, nomeBKP=nome, telefoneBKP=telefone, imgBKP=img, cidade_adicionada=nome_cidade))
#     else:
#         return redirect(url_for('novo_hemocentro', nomeBKP=nome, telefoneBKP=telefone, imgBKP=img))
