from flask_login.utils import logout_user
from app import flaskApp, login_manager, db
from flask import render_template, redirect, request, url_for
from app.models.hemocentro import Hemocentro
from app.models.captador import Captador
from collections import Counter
from sqlalchemy import exc
import bcrypt
from flask_login import login_required, current_user


@login_manager.user_loader
def get_user(captador_id):
    return Captador.query.filter_by(id=captador_id).first()


@flaskApp.route('/captador', methods=['GET', 'POST'])
@login_required
def novo_captador():
    hemocentros = Hemocentro.query.all()
    mensagem = request.args.get('mensagem')

    if request.method == 'GET':
        return render_template("captador.html", mensagem=mensagem, hemocentros=hemocentros)
    elif request.method == 'POST':
        continuar = False
        if request.form['inserir'] == 'Inserir e continuar':
            continuar = True

        nome = request.form['nome']
        celular = request.form['celular']
        if current_user.servidor:
            hemocentro = request.form['hemocentro']
        else:
            hemocentro = current_user.hemocentro_id
        adm = request.form['adm']
        mail = request.form['mail']
        login = request.form['login']
        senha = request.form['senha']
        senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        try:
            if adm == 'Captador':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=False, servidor=False, ativo=True)
            elif adm == 'Administrador':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=True, servidor=False, ativo=True)
            elif adm == 'Servidor':
                cap = Captador(nome=nome, celular=celular, hemocentro_id=hemocentro, email=mail, login=login, senha=senha, administrador=True, servidor=True, ativo=True)
            db.session.add(cap)
            db.session.commit()
        except:
            flaskApp.logger.info(f'Cadastro captador - o captador { current_user.nome } de login: { current_user.login } falhou ao tentar adicionar o captador { cap.nome }')
            return redirect(url_for("novo_captador", mensagem="ErroBD"))

        flaskApp.logger.info(f'Cadastro de Captador - o captador { cap.nome } foi registrado no hemocentro de id: { str(cap.hemocentro_id) } pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
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
        cap = ''
        try:
            cap = Captador.query.filter_by(id=captador_id).first()
            cap.nome = nome
            cap.celular = celular
            cap.hemocentro_id = hemocentro
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
            db.session.add(cap)
            db.session.commit()
        except Exception as e:
            return redirect(url_for("alterar_captador", mensagem="ErroBD", captador_id=captador_id))
            # TODO ERRO: 500 - PÁGINA BANCO DE DADOS

        flaskApp.logger.info(f'Alteracao de Captador - o captador { cap.nome }, de id { str(cap.id) } foi alterado pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
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


@flaskApp.route('/captador/<hemocentro>')
@login_required
def consultar_por_hemocentro(hemocentro):
    hemocentro_id = Hemocentro.query.filter_by(nome=hemocentro).first().id
    captadores = Captador.query.filter_by(hemocentro_id=hemocentro_id)
    hemocentro_registrados = Hemocentro.query.all()

    per_page = 5

    paginacao = captadores.paginate(page=1, per_page=per_page)

    return render_template("consultaCaptador.html", resultado=True, paginas = paginacao, hemocentros=hemocentro_registrados, hemocentro_pesquisado=hemocentro, lista_captador=paginacao.items, itens_pesquisado=per_page)


@flaskApp.route('/captador/deletar/<captador_id>') 
@login_required
def deletar_captador(captador_id):
    cap = Captador.query.filter_by(id=captador_id).first()
    cap.ativo = False
    db.session.add(cap)
    db.session.commit()
    flaskApp.logger.info(f'Desativacao de Captador - o captador { cap.nome }, de id { str(cap.id) } foi desativado pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
    return redirect(url_for('consulta_captador', mensagem="deletado"))


@flaskApp.route('/captador/desativar/<captador_id>') 
@login_required
def desativar_captador(captador_id):
    cap = Captador.query.filter_by(id=captador_id).first()
    cap.ativo = False
    db.session.add(cap)
    db.session.commit()
    logout_user()
    flaskApp.logger.info(f'Desativacao de Captador - o captador { cap.nome }, de id { str(cap.id) } desativou a si mesmo')
    return redirect(url_for('login'))