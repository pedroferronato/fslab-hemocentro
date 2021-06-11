from app import flaskApp, db
from app.models.municipio import Municipio
from app.models.doador import Doador
from app.models.estado import Estado 
from flask import render_template, redirect, request, url_for
from datetime import datetime, date
from collections import Counter
from flask_login import login_required, current_user


@flaskApp.route('/doador', methods=['GET', 'POST'])
@login_required
def novo_doador():

    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(id=current_user.get_hemocentro().get_estado().id).first().id).order_by(Municipio.nome).all()
    estados = Estado.query.all()
    sucesso = request.args.get('sucesso')

    if request.method == 'GET':
        return render_template("doador.html", cidades=cidade_registradas, estados=estados, sucesso=sucesso)

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
        estado = request.form['inputEstado']
        municipio = request.form['inputMunicipio']
        municipio = Municipio.query.filter_by(nome=municipio, uf=Estado.query.filter_by(nome=estado).first().id).first().id
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
            data_inaptidao = datetime.strptime(data_inaptidao, '%d/%m/%Y').date()
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
            flaskApp.logger.info(f'Cadastro doador - o captador { current_user.nome } de login: { current_user.login } falhou ao tentar adicionar o doador { doador.nome }')
            return render_template("paginaInicial.html", sucesso="") # TODO Gerar uma página de erro
        
        flaskApp.logger.info(f'Cadastro de doador - o doador { doador.nome } foi registrado no hemocentro de id: { str(doador.hemocentro_id) } pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
        if continuar:
            return redirect(url_for("novo_doador", sucesso=True))
        else:
            return redirect(url_for('inicial', sucesso="sucesso"))


@flaskApp.route('/doador/alterar/<doador_numRegistro>/<doador_hemocentroID>', methods=['GET', 'POST'])
@login_required
def alterar_doador(doador_numRegistro, doador_hemocentroID):
    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(id=current_user.get_hemocentro().get_estado().id).first().id).order_by(Municipio.nome).all()
    estados = Estado.query.all()
    if request.method == 'GET':
        doador = Doador.query.filter_by(numero_registro=doador_numRegistro, hemocentro_id=doador_hemocentroID).first()
        return render_template("doador.html", alterar=True, doador=doador, cidades=cidade_registradas, estados=estados)
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
        doador = Doador.query.filter_by(numero_registro=doador_numRegistro, hemocentro_id=doador_hemocentroID).first()

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

        flaskApp.logger.info(f'Alteracao de doador - o doador { doador.nome } foi alterado no hemocentro de id: { str(doador.hemocentro_id) } pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
        return redirect(url_for('consultar_doador', mensagem="sucesso", registro_alterado=doador.numero_registro))


@flaskApp.route('/doador/consultar') 
@login_required
def consultar_doador():
    registro_alterado = request.args.get('registro_alterado')
    mensagem = request.args.get('mensagem')
    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(id=current_user.get_hemocentro().get_estado().id).first().id).order_by(Municipio.nome).all()
    estados = Estado.query.all()

    if registro_alterado:
        return render_template("consultaDoadores.html", cidades=cidade_registradas, registro_alterado=registro_alterado, mensagem=mensagem, estados=estados)
    else:
        return render_template("consultaDoadores.html", cidades=cidade_registradas, mensagem=mensagem, estados=estados)


@flaskApp.route('/doador/consulta') 
@login_required
def consulta_doador():
    cidade_registradas = Municipio.query.filter_by(uf=Estado.query.filter_by(id=current_user.get_hemocentro().get_estado().id).first().id).order_by(Municipio.nome).all()
    estados = Estado.query.all()
    nome = request.args.get('nome')
    tipo_sanguineo = request.args.get('tipoSangue')
    numero_registro = request.args.get('registro')
    municipio = request.args.get('inputMunicipio')
    estado = request.args.get('inputEstado')
    municipio_pesquisado = municipio

    parametros = []

    if nome:
       parametros.append(Doador.nome.like("%{}%".format(nome)))
    if tipo_sanguineo and tipo_sanguineo != "null":
       parametros.append(Doador.tipo_sanguineo == tipo_sanguineo)
    if numero_registro:
       parametros.append(Doador.numero_registro == numero_registro)
    if municipio:
       municipio = Municipio.query.filter_by(nome=municipio, uf=Estado.query.filter_by(nome=estado).first().id).first().id
       parametros.append(Doador.municipio == municipio)

    parametros.append(Doador.ativo == True)

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
        return render_template("consultaDoadores.html", resultado=True, paginas=paginacao, doadores=lista_doador, cidades=cidade_registradas, itens=itens_pesquisados, nome_pesquisado=nome, tipo_pesquisado=tipo_sanguineo, registro_pesquisado=numero_registro, municipio_pesquisado=municipio_pesquisado, estados=estados, estado_pesquisado=request.args.get('inputEstado'))
    else:
        return render_template("consultaDoadores.html", lista_vazia=True, cidades=cidade_registradas, itens=itens_pesquisados, nome_pesquisado=nome, tipo_pesquisado=tipo_sanguineo, registro_pesquisado=numero_registro, municipio_pesquisado=municipio_pesquisado, estados=estados, estado_pesquisado=request.args.get('inputEstado'))


@flaskApp.route('/doador/deletar/<doador_numRegistro>/<doador_hemocentroId>')
@login_required
def deletar_doador(doador_numRegistro, doador_hemocentroId):
    doador = Doador.query.filter_by(numero_registro=doador_numRegistro, hemocentro_id=doador_hemocentroId).first()
    doador.ativo = False
    db.session.add(doador)
    db.session.commit()

    flaskApp.logger.info(f'Desativacao de doador - o doador { doador.nome } de id: { str(doador.numero_registro) } foi desativado pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
    return redirect(url_for('consultar_doador', mensagem="deletado"))


@flaskApp.route('/relatorio-doador') 
@login_required
def relatorio_doador():
    return render_template("relatorioDoador.html")


@flaskApp.route('/detalhes-doador') 
@login_required
def detalhes_doador():
    registro = request.args.get('registro')
    nome = request.args.get('nome')
    cpf = request.args.get('cpf')

    parametros = []

    if registro:
        parametros.append(Doador.numero_registro == registro)
    if nome:
        parametros.append(Doador.nome.like("%{}%".format(nome)))
    if cpf:
        parametros.append(Doador.cpf == cpf)

    parametros.append(Doador.ativo == True)

    resultado = Doador.query.filter(*parametros)

    if resultado.count() == 1:
        return render_template("detalhesDoador.html", doador=resultado.first())
    elif resultado.count() == 0:
        return render_template("relatorioDoador.html", nenhum_encontrado=True)
    else:
        return render_template("relatorioDoador.html", resultados=resultado.limit(15))


@flaskApp.route('/detalhes-doador/<num>/<hem>') 
@login_required
def detalhes_doador_num(num, hem):
    doador = Doador.query.filter_by(numero_registro=num, hemocentro_id=hem).first()
    if not doador:
        return render_template("relatorioDoador.html", nenhum_encontrado=True)
    else:
        return render_template("detalhesDoador.html", doador=doador)


@flaskApp.route('/alterar-inaptidao/<num>/<doador_hemocentroID>', methods=['GET', 'POST'])
@login_required
def alterar_inaptidao(num, doador_hemocentroID):
    doador = Doador.query.filter_by(numero_registro=num, hemocentro_id=doador_hemocentroID).first()

    if request.method == "GET":
        if not doador:
            return render_template("relatorioDoador.html", nenhum_encontrado=True)
        else:
            return render_template("alterarInaptidao.html", doador=doador)
    if request.method == "POST":
        inaptidao = request.form['estadoAptidao']
        if request.form['data']:
            data = datetime.strptime(request.form['data'], '%d/%m/%Y').date()
        
        if inaptidao == "apto":
            doador.inaptidao = False
            doador.final_inaptidao = None
        elif inaptidao == "inapto":
            doador.inaptidao = True
            doador.final_inaptidao = data

        if doador.ativo:
            db.session.add(doador)
            db.session.commit()
        else:
            flaskApp.logger.info(f'Cadastro de doador - o doador { doador.nome } e id: { str(doador.numero_registro) } recebeu uma tentativa de alteração inválida, sendo que o mesmo está desativado, pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
            return redirect(url_for('detalhes_doador_num', num=num, hem=doador_hemocentroID))
        
        flaskApp.logger.info(f'Cadastro de doador - o doador { doador.nome } e id: { str(doador.numero_registro) } teve o estado de inaptidao alterado para { str(doador.inaptidao) } pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
        return redirect(url_for('detalhes_doador_num', num=num, hem=doador_hemocentroID))


@flaskApp.route('/alterar-contatado/<num>/<doador_hemocentroID>')
@login_required
def alterar_contatado(num, doador_hemocentroID):
    doador = Doador.query.filter_by(numero_registro=num, hemocentro_id=doador_hemocentroID).first()
    doador.contatado = True
    db.session.add(doador)
    db.session.commit()

    flaskApp.logger.info(f'Cadastro de doador - o doador { doador.nome } e id: { str(doador.numero_registro) } foi contatado pelo usuario de login: { current_user.login } e nome: { current_user.nome }')
    return redirect(url_for('detalhes_doador_num', num=num, hem=doador_hemocentroID))

