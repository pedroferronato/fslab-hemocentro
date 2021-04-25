from app import flaskApp, db
from app.models.utilidadeSistema import Utilidades
from app.models.doador import Doador
from flask import render_template, redirect, request, url_for
from datetime import datetime, date
from collections import Counter
from flask_login import login_required, current_user


@flaskApp.route('/doador', methods=['GET', 'POST'])
@login_required
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

        num_registro = request.form['numRegistro']
        nome = request.form['nome']
        cpf = request.form['cpf']
        sexo = request.form['sexo']
        tipo_sangue = request.form['tipoSangue']
        nascimento = request.form['nascimento']
        data_nascimento = datetime.strptime(nascimento, '%d/%m/%Y').date()
        sus = request.form['sus']
        estado_civil = request.form['estadoCivil']
        celular = request.form['celular']
        telefone = request.form['telefone']
        mail = request.form['mail']
        aviso = request.form['aviso']
        municipio = request.form['municipio']
        profissao = request.form['profissao']
        local_trabalho = request.form['localTrabalho']
        estado_aptidao = request.form['estadoAptidao']
        if estado_aptidao == "apto":
            estado_aptidao = False
        else:
            estado_aptidao = True
        data_inaptidao = request.form['dataInaptidao']
        if not data_inaptidao:
            data_inaptidao = None
        else:
            data_inaptidao = datetime.strptime(dataInaptidao, '%d/%m/%Y').date()
        mae = request.form['mae']
        pai = request.form['pai']

        try:
            doador = Doador(numero_registro=num_registro, hemocentro_id = current_user.get_hemocentro().get_id(), nome=nome, cpf=cpf, sexo=sexo, tipo_sanguineo=tipo_sangue, data_de_nascimento=data_nascimento,
            cadastro_SUS=sus, estado_civil=estado_civil, celular=celular, telefone=telefone, email=mail, municipio=municipio,
            profissao=profissao, local_trabalho=local_trabalho, inaptidao=estado_aptidao, final_inaptidao=data_inaptidao, contatos_preferidos= aviso,
            nome_mae=mae, nome_pai=pai)
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
@login_required
def alterar_doador(doador_numRegistro):
    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()
    if request.method == 'GET':
        doador = Doador.query.filter_by(numero_registro=doador_numRegistro).first()
        return render_template("doador.html", alterar=True, doador=doador, cidades=cidade_registradas)
    elif request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        sexo = request.form['sexo']
        tipoSangue = request.form['tipoSangue']
        nascimento = datetime.strptime(request.form['nascimento'], '%d/%m/%Y').date()
        sus = request.form['sus']
        estadoCivil = request.form['estadoCivil']
        celular = request.form['celular']
        telefone = request.form['telefone']
        mail = request.form['mail']
        aviso = request.form['aviso']
        profissao = request.form['profissao']
        localTrabalho = request.form['localTrabalho']
        mae = request.form['mae']
        pai = request.form['pai']
        doador = Doador.query.filter_by(numero_registro=doador_numRegistro).first()


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
        doador.profissao = profissao
        doador.local_trabalho = localTrabalho
        doador.nome_mae = mae
        doador.nome_pai = pai 
        db.session.add(doador)
        db.session.commit()
        return redirect(url_for('consultar_doador', mensagem="sucesso", registro_alterado=doador.numero_registro))


@flaskApp.route('/doador/consultar') 
@login_required
def consultar_doador():
    registro_alterado = request.args.get('registro_alterado')
    mensagem = request.args.get('mensagem')

    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()

    if registro_alterado:
        return render_template("consultaDoadores.html", cidades=cidade_registradas, registro_alterado=registro_alterado, mensagem=mensagem)
    else:
        return render_template("consultaDoadores.html", cidades=cidade_registradas, mensagem=mensagem)


@flaskApp.route('/doador/consulta') 
@login_required
def consulta_doador():
    cidade_registradas = Utilidades.query.order_by(Utilidades.id).all()
    nome = request.args.get('nome')
    tipo_sanguineo = request.args.get('tipoSangue')
    numero_registro = request.args.get('registro')
    municipio = request.args.get('municipio')

    parametros = []

    if nome:
       parametros.append(Doador.nome.like("%{}%".format(nome)))
    if tipo_sanguineo and tipo_sanguineo != "null":
       parametros.append(Doador.tipo_sanguineo == tipo_sanguineo)
    if numero_registro:
       parametros.append(Doador.numero_registro == numero_registro)
    if municipio and municipio != "null":
       parametros.append(Doador.municipio == municipio)


    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    itens = request.args.get('itens')
    
    if itens:
        itens_pesquisados = int(itens)
    else:
        itens_pesquisados = 5

    paginacao = Doador.query.filter(*parametros).paginate(page=page, per_page=itens_pesquisados)

    lista_doador = paginacao.items

    if Counter(lista_doador):
        return render_template("consultaDoadores.html", resultado=True, paginas=paginacao, doadores=lista_doador, cidades=cidade_registradas, itens=itens_pesquisados, nome_pesquisado=nome, tipo_pesquisado=tipo_sanguineo, registro_pesquisado=numero_registro, municipio_pesquisado=municipio)
    else:
        return render_template("consultaDoadores.html", lista_vazia=True, cidades=cidade_registradas, itens=itens_pesquisados, nome_pesquisado=nome, tipo_pesquisado=tipo_sanguineo, registro_pesquisado=numero_registro, municipio_pesquisado=municipio)

@flaskApp.route('/doador/deletar/<doador_numRegistro>')
@login_required
def deletar_doador(doador_numRegistro):
    doador = Doador.query.filter_by(numero_registro=doador_numRegistro).first()
    db.session.delete(doador)
    db.session.commit()
    return redirect(url_for('consultar_doador', mensagem="deletado"))


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

