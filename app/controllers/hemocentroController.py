from app import flaskApp, db
from app.models.hemocentro import Hemocentro
from app.models.municipio import Municipio
from app.models.estado import Estado
from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user


@flaskApp.route('/hemocentro', methods=['GET', 'POST'])
@login_required
def novo_hemocentro():

    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(id=current_user.get_hemocentro().get_estado().id).first().id).order_by(Municipio.nome).all()
    estados = Estado.query.all()
    sucesso = request.args.get('sucesso')

    if request.method == 'GET':
        return render_template("hemocentro.html", cidades=cidade_registradas, estados=estados, sucesso=sucesso)

    elif request.method == 'POST':
        continuar = False
        if request.form['inserir'] == 'Inserir e continuar':
            continuar = True

        nome = request.form['nome']
        telefone = request.form['telefone']
        estado = request.form['inputEstado']
        municipio = request.form['inputMunicipio']
        municipio = Municipio.query.filter_by(nome=municipio, uf=Estado.query.filter_by(nome=estado).first().id).first().id
        img = request.form['img']

        if img == "" or img == None:
            img = "dummy.png"
        try:
            hemocentro = Hemocentro(nome=nome, municipio=municipio, telefone=telefone, urlImg=img)
            db.session.add(hemocentro)
            db.session.commit()
        except:
            print("An exception occurred")
            return render_template("paginaInicial.html", sucesso="") # TODO Gerar uma página de erro

        if continuar:
            return redirect(url_for("novo_hemocentro", sucesso=True))
        else:
            return redirect(url_for('inicial', sucesso="sucesso"))


@flaskApp.route('/hemocentro/alterar/<hemocentro_id>', methods=['GET', 'POST'])
@login_required
def alterar_hemocentro(hemocentro_id):
    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(nome='Rondônia').first().id).order_by(Municipio.nome).all()
    if request.method == 'GET':
        hemocentro = Hemocentro.query.filter_by(id=hemocentro_id).first()
        return render_template("hemocentro.html", alterar=True, hemocentro=hemocentro, cidades=cidade_registradas)
    elif request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        img = request.form['img']
        hemocentro = Hemocentro.query.filter_by(id=hemocentro_id).first()
        hemocentro.nome = nome
        hemocentro.telefone = telefone
        hemocentro.img = img

        db.session.add(hemocentro)
        db.session.commit()

        return redirect(url_for('consultar_hemocentro', sucesso="sucesso"))


@flaskApp.route('/hemocentro/consultar') 
@login_required
def consultar_hemocentro():
    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(nome='Rondônia').first().id).order_by(Municipio.nome).all()
    nome = request.args.get('nome')
    municipio = request.args.get('municipio')

    sucesso = request.args.get('sucesso')

    if nome and municipio:
        nome = '%' + nome + '%'
        municipio = '%' + municipio + '%'
        lista_hemocentro = Hemocentro.query.filter(Hemocentro.nome.like(nome), Hemocentro.municipio.like(municipio))
    elif nome:
        nome = '%' + nome + '%'
        lista_hemocentro = Hemocentro.query.filter(Hemocentro.nome.like(nome))
    elif municipio:
        municipio = '%' + municipio + '%'
        lista_hemocentro = Hemocentro.query.filter(Hemocentro.municipio.like(municipio))
    else:
        return render_template("consultaHemocentro.html", sucesso=sucesso, cidades=cidade_registradas)

    if lista_hemocentro.count() > 0:
        return render_template("consultaHemocentro.html", resultado=True, lista_hemocentro=lista_hemocentro, cidades=cidade_registradas)
    else:
        return render_template("consultaHemocentro.html", lista_vazia=True, cidades=cidade_registradas)


@flaskApp.route('/hemocentro/deletar/<hemocentro_id>') 
@login_required
def deletar_hemocentro(hemocentro_id):
    hemocentro = Hemocentro.query.filter_by(id=hemocentro_id).first()
    db.session.delete(hemocentro)
    db.session.commit()
    return redirect(url_for('consultar_hemocentro', sucesso="sucesso"))

