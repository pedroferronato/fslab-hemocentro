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
        pass


@flaskApp.route('/hemocentro/consultar') 
def consultar_hemocentro():
    return render_template("consultaHemocentro.html")


@flaskApp.route('/hemocentro/consultar/resultado') 
def consultar_hemocentro_resultado():
    return render_template("consultaHemocentro.html", resultado=True)

