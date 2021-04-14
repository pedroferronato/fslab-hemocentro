from app import flaskApp, db
from app.models.utilidadeSistema import Utilidades
from app.models.hemocentro import Hemocentro
from flask import render_template, redirect, request, url_for


@flaskApp.route('/hemocentro', methods=['GET', 'POST'])
def novo_hemocentro():

    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()
    sucesso = request.args.get('sucesso')

    if request.method == 'GET':
        return render_template("hemocentro.html", cidades=cidade_registradas, sucesso=sucesso)

    elif request.method == 'POST':
        continuar = False
        if request.form['inserir'] == 'Inserir e continuar':
            continuar = True

        nome = request.form['nome']
        telefone = request.form['telefone']
        cidade = request.form['municipio']
        img = request.form['img']

        if img == "" or img == None:
            img = "dummy.png"
        try:
            hemocentro = Hemocentro(nome=nome, municipio=cidade, telefone=telefone, urlImg=img)
            db.session.add(hemocentro)
            db.session.commit()
        except:
            print("An exception occurred")
            return render_template("paginaInicial.html", sucesso="") # TODO geral uma página de erro

        if continuar:
            return redirect(url_for("novo_hemocentro", sucesso=True))
        else:
            return redirect(url_for('inicial', sucesso="sucesso"))


@flaskApp.route('/hemocentro/alterar/<hemocentro_id>', methods=['GET', 'POST'])
def alterar_hemocentro(hemocentro_id):
    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()
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
def consultar_hemocentro():
    nome = request.args.get('nome')
    municipio = request.args.get('cidade')

    sucesso = request.args.get('sucesso')

    if nome and municipio:
        nome = '%' + nome + '%'
        municipio = '%' + municipio + '%'
        lista_hemocentro = Hemocentro.query.filter(Hemocentro.nome.like(nome), Hemocentro.municipio.like(municipio))
        return render_template("consultaHemocentro.html", resultado=True, lista_hemocentro=lista_hemocentro)
    elif nome:
        nome = '%' + nome + '%'
        lista_hemocentro = Hemocentro.query.filter(Hemocentro.nome.like(nome))
        return render_template("consultaHemocentro.html", resultado=True, lista_hemocentro=lista_hemocentro)
    elif municipio:
        municipio = '%' + municipio + '%'
        lista_hemocentro = Hemocentro.query.filter(Hemocentro.municipio.like(municipio))
        return render_template("consultaHemocentro.html", resultado=True, lista_hemocentro=lista_hemocentro)
    else:
        return render_template("consultaHemocentro.html", sucesso=sucesso)


@flaskApp.route('/hemocentro/deletar/<hemocentro_id>') 
def deletar_hemocentro(hemocentro_id):
    hemocentro = Hemocentro.query.filter_by(id=hemocentro_id).first()
    db.session.delete(hemocentro)
    db.session.commit()
    return redirect(url_for('consultar_hemocentro', sucesso="sucesso"))

