from app import flaskApp, db
from app.models.utilidadeSistema import Utilidades
from app.models.doador import Doador
from flask import render_template, redirect, request, url_for
from datetime import datetime, date


@flaskApp.route('/doador', methods=['GET', 'POST'])
def novo_doador():

    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()
    sucesso = request.args.get('sucesso')

    recarregar = request.args.get('reload')

    numRegistroBKP = request.args.get('numRegistroBKP')
    nomeBKP = request.args.get('nomeBKP')
    cpfBKP = request.args.get('cpfBKP')
    sexoBKP = request.args.get('sexoBKP')
    tipoSangueBKP = request.args.get('tipoSangueBKP')
    nascimentoBKP = request.args.get('nascimentoBKP')
    susBKP = request.args.get('susBKP')
    estadoCivilBKP = request.args.get('estadoCivilBKP')
    celularBKP = request.args.get('celularBKP')
    telefoneBKP = request.args.get('telefoneBKP')
    mailBKP = request.args.get('mailBKP')
    avisoBKP = request.args.get('avisoBKP')
    profissaoBKP = request.args.get('profissaoBKP')
    localTrabalhoBKP = request.args.get('localTrabalhoBKP')
    estadoAptidaoBKP = request.args.get('estadoAptidaoBKP')
    dataInaptidaoBKP = request.args.get('dataInaptidaoBKP')
    maeBKP = request.args.get('maeBKP')
    paiBKP = request.args.get('paiBKP')
    cidade_adicionada = request.args.get('cidade_adicionada')

    if request.method == 'GET':
        if recarregar:
            return render_template("doador.html", reload=recarregar, cidades=cidade_registradas, numRegistroBKP=numRegistroBKP,
             nomeBKP=nomeBKP, cpfBKP=cpfBKP, sexoBKP=sexoBKP, tipoSangueBKP=tipoSangueBKP, nascimentoBKP=nascimentoBKP,
             susBKP=susBKP, estadoCivilBKP=estadoCivilBKP, celularBKP=celularBKP, telefoneBKP=telefoneBKP, mailBKP=mailBKP,
             avisoBKP=avisoBKP, profissaoBKP=profissaoBKP, localTrabalhoBKP=localTrabalhoBKP, estadoAptidaoBKP=estadoAptidaoBKP,
             dataInaptidaoBKP=dataInaptidaoBKP, maeBKP=maeBKP, paiBKP=paiBKP, cidade_adicionada=cidade_adicionada)
        else:
            return render_template("doador.html", cidades=cidade_registradas, sucesso=sucesso)

    elif request.method == 'POST':
        continuar = False
        if request.form['inserir'] == 'Inserir e continuar':
            continuar = True

        numRegistro = request.form['numRegistro']
        nome = request.form['nome']
        cpf = request.form['cpf']
        sexo = request.form['sexo']
        tipoSangue = request.form['tipoSangue']
        nascimento = request.form['nascimento']
        dateNasc = datetime.strptime(nascimento, '%d/%m/%Y').date()
        sus = request.form['sus']
        estadoCivil = request.form['estadoCivil']
        celular = request.form['celular']
        telefone = request.form['telefone']
        mail = request.form['mail']
        aviso = request.form['aviso'] 
        municipio = request.form['municipio']
        profissao = request.form['profissao']
        localTrabalho = request.form['localTrabalho']
        estadoAptidao = request.form['estadoAptidao']
        dataInaptidao = request.form['dataInaptidao']
        if not dataInaptidao:
            dateInap = None
        else:
            dateInap = datetime.strptime(dataInaptidao, '%d/%m/%Y').date()
        mae = request.form['mae']
        pai = request.form['pai']

        try:
            doador = Doador(numero_registro=numRegistro, hemocentro_id = 1, nome=nome, cpf=cpf, sexo=sexo, tipo_sanguineo=tipoSangue, data_de_nascimento=dateNasc,
             cadastro_SUS=sus, estado_civil=estadoCivil, celular=celular, telefone=telefone, email=mail, municipio=municipio,
             profissao=profissao, local_trabalho=localTrabalho, final_inaptidao=dateInap, contatos_preferidos= aviso,
             nome_mae=mae, nome_pai=pai )
            db.session.add(doador)
            db.session.commit()

        except Exception as e:
            print(e)
            return render_template("paginaInicial.html", sucesso="") # TODO Gerar uma página de erro
        
        if continuar:
            return redirect(url_for("novo_doador", sucesso=True))
        else:
            return redirect(url_for('inicial', sucesso="sucesso"))


@flaskApp.route('/doador/alterar/<doador_numRegistro>', methods=['GET', 'POST'])
def alterar_doador(doador_numRegistro):
    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()
    if request.method == 'GET':
        doador = Doador.query.filter_by(id=doador_numRegistro).first()
        return render_template("doador.html", alterar=True, doador=doador, cidades=cidade_registradas)
    elif request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        sexo = request.form['sexo']
        tipoSangue = request.form['tipoSangue']
        nascimento = request.form['nascimento']
        sus = request.form['sus']
        estadoCivil = request.form['estadoCivil']
        celular = request.form['celular']
        telefone = request.form['telefone']
        mail = request.form['mail']
        aviso = request.form['aviso']
        municipio = request.form['municipio']
        profissao = request.form['profissao']
        localTrabalho = request.form['localTrabalho']
        estadoAptidao = request.form['estadoAptidao']
        dataInaptidao = request.form['dataInaptidao']
        mae = request.form['mae']
        pai = request.form['pai']
        doador = Doador.query.filter_by(id=doador_numRegistro).first()

        doador.nome = nome
        doador.cpf = cpf
        doador.sexo = sexo
        doador.tipo_sanguineo = tipoSangue
        doador.data_de_nascimento = nascimento
        doador.cadastro_SUS = sus
        doador.estado_civil = estadoCivil
        doador.celular = celular
        doador.telefone = telefone
        doador.email = mail
        doador.contatos_preferidos = aviso
        doador.municipio = municipio
        doador.profissao = profissao
        doador.local_trabalho = localTrabalho
        doador.inaptidao = estadoAptidao
        doador.final_inaptidao = dataInaptidao
        doador.nome_mae = mae
        doador.nome_pai = pai 
        db.session.add(doador)
        db.session.commit()

        return redirect(url_for('consultar_doador', sucesso="sucesso"))


@flaskApp.route('/doador/consultar') 
def consultar_doador():
    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()
    nome = request.args.get('nome')
    tipo_sanguineo = request.args.get('tipoSangue')
    numero_registro = request.args.get('registro')
    municipio = request.args.get('municipio')

    sucesso = request.args.get('sucesso')

    if nome and tipo_sanguineo and numero_registro and municipio:
        nome = '%' + nome + '%'
        tipo_sanguineo = '%' + tipo_sanguineo + '%'
        numero_registro = '%' + numero_registro + '%'
        municipio = '%' + municipio + '%'
        lista_doador = Doador.query.filter(Doador.nome.like(nome), Doador.tipo_sanguineo.like(tipo_sanguineo), Doador.numero_registro.like(numero_registro), Doador.municipio.like(municipio))
    elif nome and tipo_sanguineo:
        nome = '%' + nome + '%'
        tipo_sanguineo = '%' + tipo_sanguineo + '%'
        lista_doador = Doador.query.filter(Doador.nome.like(nome), Doador.tipo_sanguineo.like(tipo_sanguineo))
    elif nome and numero_registro:
        nome = '%' + nome + '%'
        numero_registro = '%' + numero_registro + '%'
        lista_doador = Doador.query.filter(Doador.nome.like(nome), Doador.numero_registro.like(numero_registro))
    elif nome and municipio:
        nome = '%' + nome + '%'
        municipio = '%' + municipio + '%'
        lista_doador = Doador.query.filter(Doador.nome.like(nome), Doador.municipio.like(municipio))
    elif nome:
        nome = '%' + nome + '%'
        lista_doador = Doador.query.filter(Doador.nome.like(nome))
    elif tipo_sanguineo:
        tipo_sanguineo = '%' + tipo_sanguineo + '%'
        lista_doador = Doador.query.filter(Doador.tipo_sanguineo.like(tipo_sanguineo))
    elif numero_registro:
        numero_registro = '%' + numero_registro + '%'
        lista_doador = Doador.query.filter(Doador.numero_registro.like(numero_registro))
    elif municipio:
        municipio = '%' + municipio + '%'
        lista_doador = Doador.query.filter(Doador.municipio.like(municipio))
    else:
        return render_template("consultaDoadores.html", sucesso=sucesso, cidades=cidade_registradas)

    if lista_doador.count() > 0:
        return render_template("consultaDoadores.html", resultado=True, lista_doador=lista_doador, cidades=cidade_registradas)
    else:
        return render_template("consultaDoadores.html", lista_vazia=True, cidades=cidade_registradas)


@flaskApp.route('/doador/deletar/<doador_numRegistro>') 
def deletar_doador(doador_numRegistro):
    doador = Doador.query.filter_by(id=doador_numRegistro).first()
    db.session.delete(doador)
    db.session.commit()
    return redirect(url_for('consultar_doador', sucesso="sucesso"))


# @flaskApp.route('/alterar-inaptidao') # '/alterar_inatidao/<id>'
# def alterar_inaptidao():
#     return render_template("alterarInaptidao.html")


# @flaskApp.route('/consultar-inaptidao') 
# def consultar_inaptidao():
#     return render_template("consultaDoadores.html")


# @flaskApp.route('/consultar-inaptidao/resultado') 
# def consultar_inaptidao_resultado():
#     return render_template("consultaDoadores.html", resultado=True)


# @flaskApp.route('/realatorio-doador') 
# def relatorio_doador():
#     return render_template("relatorioDoador.html")


# @flaskApp.route('/realatorio-doador/id') # '/alterar_inatidao/<id>'
# def detalhes_doador():
#     return render_template("detalhesDoador.html")

