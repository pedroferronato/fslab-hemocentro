from app import flaskApp, db
from flask import render_template, request
from flask_login import login_required, current_user
from sqlalchemy import and_, or_
from app.models.doador import Doador
from app.models.municipio import Municipio
from app.models.estado import Estado
from dateutil.relativedelta import relativedelta
from datetime import datetime


@flaskApp.route('/convocacao-tipada')
@login_required
def chamada_tipada():
    return render_template("convocacaoTipada.html", tipo="tipada")


@flaskApp.route('/convocacao-tipada/resultado', methods=['POST'])
@login_required
def chamada_tipada_resultado():
    tipo = request.form['tipagem']

    itens = request.form['itens']
    page = request.form['page']

    telefonados = request.form['telefonados']
    telefonados_string = telefonados
    telefonados = telefonados.split("&")
    telefonados.pop()
    telefonados = [int(x) for x in telefonados]
    
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if itens:
        itens_pesquisados = int(itens)
    else:
        itens_pesquisados = 5

    filtros = []

    filtros.append(
        or_( Doador.ultima_doacao == None ,
            or_(
                and_(Doador.sexo == "mas", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=3))), 
                and_(Doador.sexo == "fem", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=4)))
            )
        )
    )
    filtros.append(Doador.contatado == False)
    filtros.append(Doador.hemocentro_id == current_user.get_hemocentro().get_id())
    filtros.append(Doador.tipo_sanguineo == tipo)
    filtros.append(Doador.inaptidao == False)
    filtros.append(Doador.legado == False)
    filtros.append(Doador.idade < 70)

    resultado = Doador.query.filter(*filtros).limit(100).from_self().order_by(Doador.municipio != current_user.get_hemocentro().get_municipio()).order_by(Doador.ultima_doacao.desc())

    if len(resultado.all()) == 0:
        return render_template("convocacaoTipada.html", listaVazia=True, tipo_sanguineo=tipo, tipo="tipada")
    else:
        if request.form['botao'] == 'Marcar Telefonados':
            for numero in telefonados:
                telefonado = Doador.query.filter_by(numero_registro= numero).first()
                telefonado.contatado = True
                db.session.add(telefonado)
                db.session.commit()
            return render_template("convocacaoTipada.html", tipo_sanguineo=tipo, tipo="tipada")
        else:
            paginacao = resultado.paginate(page=page, per_page=itens_pesquisados)
            return render_template("convocacaoTipada.html", resultado=True, doadores=paginacao.items, paginas=paginacao, tipo_sanguineo=tipo, tipo="tipada", itens=itens_pesquisados, telefonados=telefonados, telefonadosStr=telefonados_string)

    

@flaskApp.route('/convocacao-emergencial')
@login_required
def chamada_emergencial():
    return render_template("convocacaoEmergencial.html", tipo="emergencial")


@flaskApp.route('/convocacao-emergencial/resultado', methods=['POST'])
@login_required
def chamada_emergencial_resultado():
    tipo = request.form['tipagem']

    itens = request.form['itens']
    page = request.form['page']

    telefonados = request.form['telefonados']
    telefonados_string = telefonados
    telefonados = telefonados.split("&")
    telefonados.pop()
    telefonados = [int(x) for x in telefonados]
    
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if itens:
        itens_pesquisados = int(itens)
    else:
        itens_pesquisados = 5

    filtros = []

    filtros.append(
        or_( Doador.ultima_doacao == None ,
            or_(
                and_(Doador.sexo == "mas", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=2))), 
                and_(Doador.sexo == "fem", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=3)))
            )
        )
    )
    filtros.append(Doador.contatado == False)
    filtros.append(Doador.hemocentro_id == current_user.get_hemocentro().get_id())
    filtros.append(Doador.tipo_sanguineo == tipo)
    filtros.append(Doador.inaptidao == False)
    filtros.append(Doador.legado == False)
    filtros.append(Doador.idade < 70)

    resultado = Doador.query.filter(*filtros).limit(100).from_self().order_by(Doador.municipio != current_user.get_hemocentro().get_municipio()).order_by(Doador.ultima_doacao.desc())

    if len(resultado.all()) == 0:
        return render_template("convocacaoEmergencial.html", listaVazia=True, tipo_sanguineo=tipo, tipo="emegencial")
    else:
        if request.form['botao'] == 'Marcar Telefonados':
            for numero in telefonados:
                telefonado = Doador.query.filter_by(numero_registro= numero).first()
                telefonado.contatado = True
                db.session.add(telefonado)
                db.session.commit()
            return render_template("convocacaoEmergencial.html", tipo_sanguineo=tipo, tipo="emegencial")
        else:
            paginacao = resultado.paginate(page=page, per_page=itens_pesquisados)
            return render_template("convocacaoEmergencial.html", resultado=True, doadores=paginacao.items, paginas=paginacao, tipo_sanguineo=tipo, tipo="emegencial", itens=itens_pesquisados, telefonados=telefonados, telefonadosStr=telefonados_string)


@flaskApp.route('/convocacao-localidades-externas')
@login_required
def chamada_localidades_externas():
    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(id=current_user.get_hemocentro().get_estado().id).first().id).order_by(Municipio.nome).all()
    estados = Estado.query.all()
    return render_template("convocacaoLocalidadesExternas.html", cidades=cidade_registradas, estados=estados)


@flaskApp.route('/convocacao-localidades-externas/resultado', methods=['POST'])
@login_required
def chamada_localidades_externas_resultado():
    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(id=current_user.get_hemocentro().get_estado().id).first().id).order_by(Municipio.nome).all()
    estados = Estado.query.all()
    tipo = request.form['tipagem']
    estado = request.form['inputEstado']
    municipio = request.form['inputMunicipio']
    municipio = Municipio.query.filter_by(nome=municipio, uf=Estado.query.filter_by(nome=estado).first().id).first().id

    itens = request.form['itens']
    page = request.form['page']

    telefonados = request.form['telefonados']
    telefonados_string = telefonados
    telefonados = telefonados.split("&")
    telefonados.pop()
    telefonados = [int(x) for x in telefonados]

    print("Telefonados:")
    print(telefonados)
    
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if itens:
        itens_pesquisados = int(itens)
    else:
        itens_pesquisados = 5

    filtros = []

    filtros.append(
        or_( Doador.ultima_doacao == None ,
            or_(
                and_(Doador.sexo == "mas", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=3))), 
                and_(Doador.sexo == "fem", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=4)))
            )
        )
    )
    filtros.append(Doador.contatado == False)
    filtros.append(Doador.tipo_sanguineo == tipo)
    filtros.append(Doador.municipio == int(municipio))
    filtros.append(Doador.inaptidao == False)
    filtros.append(Doador.legado == False)
    filtros.append(Doador.idade < 70)

    resultado = Doador.query.filter(*filtros).limit(100).from_self().order_by(Doador.ultima_doacao.desc())

    if len(resultado.all()) == 0:
        return render_template("convocacaoLocalidadesExternas.html", listaVazia=True, estados=estados , tipo_sanguineo=tipo, cidades=cidade_registradas, cidade_pesquisada=int(municipio))
    else:
        if request.form['botao'] == 'Marcar Telefonados':
            for numero in telefonados:
                telefonado = Doador.query.filter_by(numero_registro=numero).first()
                telefonado.contatado = True
                db.session.add(telefonado)
                db.session.commit()
            return render_template("convocacaoLocalidadesExternas.html", estados=estados , tipo_sanguineo=tipo, cidades=cidade_registradas, cidade_pesquisada=int(municipio))
        else:
            paginacao = resultado.paginate(page=page, per_page=itens_pesquisados)
            return render_template("convocacaoLocalidadesExternas.html", estados=estados , resultado=True, doadores=paginacao.items, paginas=paginacao, tipo_sanguineo=tipo, itens=itens_pesquisados, telefonados=telefonados, telefonadosStr=telefonados_string, cidades=cidade_registradas, cidade_pesquisada=int(municipio))

