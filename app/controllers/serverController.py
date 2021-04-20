from app import flaskApp, db
from app.models.utilidadeSistema import Utilidades
from flask import render_template, redirect, request, url_for


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


@flaskApp.route("/cidade/nova", methods=['POST'])
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
