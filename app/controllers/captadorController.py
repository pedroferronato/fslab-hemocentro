from app import flaskApp, login_manager, db
from flask import render_template, redirect, request, url_for
from app.models.hemocentro import Hemocentro
from app.models.utilidadeSistema import Utilidades
from app.models.captador import Captador
from collections import Counter
from sqlalchemy import exc
import bcrypt
from flask_login import login_required


@login_manager.user_loader
def get_user(captador_id):
    return Captador.query.filter_by(id=captador_id).first()


@flaskApp.route('/captador', methods=['GET', 'POST'])
@login_required
def novo_captador():
    mensagem = request.args.get('mensagem')
    senhasDiferentes = request.args.get('senhas')

    hemocentros = Hemocentro.query.all()
    if request.method == 'GET':
        return render_template("captador.html", mensagem=mensagem, hemocentros=hemocentros)
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
        senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        try:
            if adm == 'Captador':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=False, servidor=False)
            elif adm == 'Administrador':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=True, servidor=False)
            elif adm == 'Servidor':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=True, servidor=True)
            db.session.add(cap)
            db.session.commit()
        except:
            return redirect(url_for("novo_captador", mensagem="ErroBD"))
            # TODO: PAGINA 500 - OU MANTER OS DADOS

        if continuar:
            return redirect(url_for("novo_captador", mensagem="Inserido"))
        else:
            return redirect(url_for('inicial', sucesso="sucesso"))

@flaskApp.route('/captador/alterar/<captador_id>', methods = ['GET', 'POST'])
@login_required
def alterar_captador(captador_id):
    hemocentros = Hemocentro.query.all()
    mensagem = request.args.get('mensagem')
    if request.method == 'GET':
        captador = Captador.query.filter_by(id=captador_id).first()
        return render_template("captador.html", alterar=True, captador=captador, hemocentros=hemocentros, mensagem=mensagem)

    elif request.method == 'POST':
        nome = request.form['nome']
        celular = request.form['celular']
        hemocentro = request.form['hemocentro']
        adm = request.form['adm']
        mail = request.form['mail']
        login = request.form['login']
        try:
            cap = Captador.query.filter_by(id=captador_id).first()
            cap.nome = nome
            cap.celular = celular
            cap.hemocentro_id = int(hemocentro)
            cap.email = mail
            cap.login = login
            if adm == 'Captador':
                cap.administrador = False
                cap.servidor = False
            elif adm == 'Administrador':
                cap.administrador = True
                cap.servidor = False
            elif adm == 'Servidor':
                cap.administrador = True
                cap.servidor = True
            else:
                pass
            db.session.add(cap)
            db.session.commit()
        except:
            return redirect(url_for("alterar_captador", mensagem="ErroBD", captador_id=captador_id))
            # TODO ERRO: 500 - PÁGINA BANCO DE DADOS

        return redirect(url_for("consultar_captador", mensagem="sucesso", nome=cap.nome))

@flaskApp.route('/captador/consulta')
@login_required
def consulta_captador():
    hemocentro_registrados = Hemocentro.query.all()
    mensagem = request.args.get('mensagem')
    return render_template("consultaCaptador.html", resultado=False, hemocentros=hemocentro_registrados, mensagem = mensagem)


@flaskApp.route('/captador/consultar')
@login_required
def consultar_captador():
    hemocentro_registrados = Hemocentro.query.all()

    mensagem = request.args.get('mensagem')

    hemocentro_id = request.args.get('hemocentro')
    nome = request.args.get('nome')
    itens = request.args.get('itens')
    lista_captador= []

    nome_pesquisado = nome

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if itens:
        itens_pesquisado = int(itens)
    else:
        itens_pesquisado = 5
    if hemocentro_id:
        hemocentro_pesquisado = int(hemocentro_id)
    else:
        hemocentro_pesquisado = ""

    if nome and hemocentro_id:
        nome = '%' + nome + '%'
        paginacao = Captador.query.filter(Captador.nome.like(nome), Captador.hemocentro_id.like(hemocentro_id)).paginate(page=page, per_page=itens_pesquisado)
    elif nome:
        nome = '%' + nome + '%'
        paginacao = Captador.query.filter(Captador.nome.like(nome)).paginate(page=page, per_page=itens_pesquisado)
    elif hemocentro_id:
        paginacao = Captador.query.filter(Captador.hemocentro_id.like(hemocentro_id)).paginate(page=page, per_page=itens_pesquisado)
    else:
        paginacao = Captador.query.order_by(Captador.nome).paginate(page=page, per_page=itens_pesquisado)

    lista_captador = paginacao.items

    if Counter(lista_captador):
        return render_template("consultaCaptador.html", resultado=True, hemocentros=hemocentro_registrados, lista_captador=lista_captador, paginas = paginacao, hemocentro_pesquisado=hemocentro_pesquisado, captador_pesquisado=nome_pesquisado, itens_pesquisado=itens_pesquisado,mensagem=mensagem)
    else:
        return render_template("consultaCaptador.html", lista_vazia=True, resultado=False, hemocentros=hemocentro_registrados, hemocentro_pesquisado=hemocentro_pesquisado, captador_pesquisado=nome_pesquisado, itens_pesquisado=itens_pesquisado,mensagem=mensagem)


@flaskApp.route('/captador/deletar/<captador_id>') 
@login_required
def deletar_captador(captador_id):
    cap = Captador.query.filter_by(id=captador_id).first()
    db.session.delete(cap)
    db.session.commit()
    return redirect(url_for('consulta_captador', mensagem="deletado"))