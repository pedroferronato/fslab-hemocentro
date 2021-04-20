from app import flaskApp, login_manager, db
from flask import render_template, redirect, request, url_for
from app.models.hemocentro import Hemocentro
from app.models.captador import Captador
from flask_login import login_required


@login_manager.user_loader
def get_user(captador_id):
    return Captador.query.filter_by(id=captador_id).first()


@flaskApp.route('/captador', methods=['GET', 'POST'])
@login_required
def novo_captador():
    sucesso = request.args.get('sucesso')
    senhasDiferentes = request.args.get('senhas')

    hemocentros = Hemocentro.query.all()
    if request.method == 'GET':
        return render_template("captador.html", sucesso=sucesso, hemocentros=hemocentros)
    elif request.method == 'POST':
        continuar = False
        if request.form['inserir'] == 'Inserir e continuar':
            continuar = True
        
        nome = request.form['nome']
        celular = request.form['celular']
        hemocentro = request.form['hemocentro']
        adm = request.form['adm']
        mail = request.form['mail']
        login = request.form['login']
        senha = request.form['senha']

        #TODO: CRIPTOGRAFAR SENHA

        try:
            if adm == 'Captador':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=False, servidor=False)
            elif adm == 'Administrador':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=True, servidor=False)
            elif adm == 'Servidor':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=True, servidor=True)
            else:
                pass
            db.session.add(cap)
            db.session.commit()
        except:
            print("An exception occurred")
            return render_template("paginaInicial.html", sucesso="") # TODO Gerar uma página de erro

        if continuar:
            return redirect(url_for("novo_captador", sucesso=True))
        else:
            return redirect(url_for('inicial', sucesso="sucesso"))
    

@flaskApp.route('/alterar-captador')
@login_required
def alterar_captador():
    return render_template("captador.html", alterar=True)


@flaskApp.route('/consultar/captador') 
@login_required
def consultar_captador():
    return render_template("consultaCaptador.html")


@flaskApp.route('/consultar-captadores/resultado')
@login_required 
def consultar_captador_resultado():
    return render_template("consultaCaptador.html", resultado=True)

