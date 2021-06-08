from dateutil.relativedelta import relativedelta
from sqlalchemy.sql.elements import Null
from app import flaskApp, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from datetime import date, datetime
from collections import Counter
from app.models.doacao import Doacao
from app.models.doador import Doador
from app.models.hemocentro import Hemocentro


# hemocentro_id = current_user.get_hemocentro().get_id()

@flaskApp.route('/doacao', methods=['GET', 'POST'])
@login_required
def nova_doacao():
    hoje = date.today()
    hoje = hoje.strftime('%d/%m/%Y')
    mensagem = request.args.get('mensagem')
    numero_registro = request.args.get('numero_registro')
    nome = request.args.get('nome')
    tipoSangue = request.args.get('tipoSangue')

    if request.method == 'GET':
        return render_template("doacao.html", date=hoje, mensagem=mensagem,numero_registro=numero_registro,nome=nome,tipoSangue=tipoSangue)

    elif request.method == 'POST':

        if request.form['botao'] == "search":
            convocacao = request.form['convocacao']
            data = request.form['data']
            numRegistro = request.form['numRegistro']
            if not numRegistro == '':
                doador = Doador.query.filter(Doador.numero_registro.like(numRegistro), Doador.hemocentro_id.like(current_user.get_hemocentro().id)).first()
                primeiraDoacao = Doacao.query.filter(Doacao.doador_id.like(numRegistro), Doacao.hemocentro_id.like(current_user.get_hemocentro().id)).count()
                if primeiraDoacao > 0:
                    if doador and ( (doador.sexo == "mas" and datetime(doador.ultima_doacao.year, doador.ultima_doacao.month, doador.ultima_doacao.day) > (datetime.today() - relativedelta(months=3))) or (doador.sexo == "fem" and datetime(doador.ultima_doacao.year, doador.ultima_doacao.month, doador.ultima_doacao.day) > (datetime.today() - relativedelta(months=4))) ):
                        return render_template("doacao.html", date=data, doador=doador, convocacao=convocacao,mensagem="ErroBD_6")
                if doador:
                    return render_template("doacao.html", date=data, doador=doador, convocacao=convocacao)
                else:
                    return render_template("doacao.html", date=data, convocacao=convocacao,mensagem="ErroBD_4")
            else:
                return redirect(url_for("pesquisa_doador"))
        elif request.form['botao'] == "Inserir e continuar" or request.form['botao'] == "Inserir":
            continuar = False
            if request.form['botao'] == 'Inserir e continuar':
                continuar = True
            
            numRegistro = request.form['numRegistro']
            nome = request.form['nome']

            try:
                doador = Doador.query.filter_by(numero_registro=numRegistro, hemocentro_id=current_user.get_hemocentro().id).first()
                if doador != None and (doador.legado or doador.get_idade() >= 61):
                    return redirect(url_for("nova_doacao", date=hoje, mensagem="ErroBD_5"))
                if doador == None or nome != doador.nome:
                    return redirect(url_for("nova_doacao", date=hoje, mensagem="ErroBD_2"))
            except:
                return redirect(url_for("nova_doacao", date=hoje, mensagem="ErroBD_2"))
            else:
                fidelidade = request.form['fidelidade']
                if doador.fidelidade != fidelidade:
                    try:
                        doador.fidelidade = fidelidade
                        db.session.add(doador)
                        db.session.commit()
                    except:
                        return redirect(url_for("doacao.html", date=hoje, mensagem="ErroBD_3"))
                data = request.form['data']
                data = datetime.strptime(data, '%d/%m/%Y').date()
                convocacao = request.form['convocacao']
                observacoes = request.form['observacoes']
                hemocentro_id = current_user.get_hemocentro().get_id()
                doacao = Doacao(hemocentro_id = hemocentro_id, doador_id= numRegistro, data= data,
                convocacao=convocacao, observacao = observacoes)
                try:
                    doador.ultima_doacao = data
                    doador.contatado = False
                    db.session.add(doador)
                    db.session.add(doacao)
                    db.session.commit()
                except Exception as e:
                    return redirect(url_for("nova_doacao", date=hoje, mensagem="ErroBD"))

                if continuar:
                    return redirect(url_for("nova_doacao", mensagem="Inserido"))
                else:
                    return redirect(url_for('inicial', sucesso="sucesso"))
        

@flaskApp.route('/doacao/doador') 
@login_required
def pesquisa_doador():
    return render_template("doacaoDoador.html")


@flaskApp.route('/doacao/doador/pesquisa')
@login_required
def pesquisar_doador():
    nome = request.args.get('nome')
    cpf = request.args.get('cpf')
    resultadoPesquisa = []

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if nome and cpf:
        nome_pesquisa = '%' + nome + '%'
        paginate = Doador.query.filter(Doador.nome.like(nome_pesquisa),Doador.cpf.like(cpf), Doador.hemocentro_id.like(current_user.get_hemocentro().id)).paginate(page=page, per_page=10)
        resultadoPesquisa = paginate.items
    elif nome:
        nome_pesquisa = '%' + nome + '%'
        paginate = Doador.query.filter(Doador.nome.like(nome_pesquisa), Doador.hemocentro_id.like(current_user.get_hemocentro().id)).paginate(page=page, per_page=10)
        resultadoPesquisa = paginate.items
    elif cpf:
        paginate = Doador.query.filter_by(cpf=cpf, hemocentro_id = current_user.get_hemocentro().id).paginate(page=page, per_page=10)
        resultadoPesquisa = paginate.items
    else:
        paginate = Doador.query.filter(Doador.hemocentro_id.like(current_user.get_hemocentro().id)).paginate(page=page, per_page=10)
        resultadoPesquisa = paginate.items

    if Counter(resultadoPesquisa):
        return render_template("doacaoDoador.html", resultadoPesquisa=resultadoPesquisa, paginate=paginate,nome=nome,cpf=cpf)
    else:
        return render_template("doacaoDoador.html", lista_vazia=True,nome=nome,cpf=cpf)


@flaskApp.route('/alterar-doacao') # '/alterar_doacao/<id>'
@login_required
def alterar_doacao():
    return render_template("doacao.html", alterar=True)


@flaskApp.route('/detalhes-doacao/<num>')
@login_required
def detalhes_doacao(num):
    doacao = Doacao.query.filter_by(id = num).first()
    
    if not doacao:
        return render_template("consultaDoacoes.html", nenhum_encontrado=True)
    else:
        doador = Doador.query.filter_by(numero_registro = doacao.doador_id).first()
        hemocentro = Hemocentro.query.filter_by(id = doacao.hemocentro_id).first()
        return render_template("detalhesDoacao.html", doador = doador, doacao=doacao, hemocentro = hemocentro)


@flaskApp.route('/consultar-doacao') 
@login_required
def consultar_doacao():
    return render_template("consultarDoacoes.html")

@flaskApp.route('/consultar-doacao/resultado', methods=['POST']) 
@login_required
def consultar_doacao_resultado():
        dataBKP = request.form['data']
        dataFinalBKP = request.form['dataFinal']
        data = datetime.strptime(request.form['data'], '%d/%m/%Y').date()
        dataFinal = datetime.strptime(request.form['dataFinal'], '%d/%m/%Y').date()
        itens = request.form['itens']

        page = request.form['page']

        if page and page.isdigit():
            page = int(page)
        else:
            page = 1

        if itens:
            itens_pesquisados = int(itens)
        else:
            itens_pesquisados = 10

        try:
            paginacao = db.session.query(Doacao.id, Doacao.data, Doador.nome, Doacao.convocacao).filter(Doacao.doador_id == Doador.numero_registro, Doacao.data.between(data, dataFinal)).order_by(Doacao.data.desc()).paginate(page=page, per_page=itens_pesquisados)
            lista_doacoes = paginacao.items
            if Counter(lista_doacoes):
                return render_template("consultarDoacoes.html", resultado=True, paginas=paginacao, doacoes=lista_doacoes, itens=itens_pesquisados, data = dataBKP, dataFinal = dataFinalBKP)
            else:
                return render_template("consultarDoacoes.html", lista_vazia=True, itens=itens_pesquisados, data = dataBKP, dataFinal = dataFinalBKP)
        except Exception as e:
            return render_template("consultarDoacoes.html") 


@flaskApp.route('/consultar-doacao/doador') 
@login_required
def consultar_doacao_por_doador():
    return render_template("consultarDoacoesDoador.html")


@flaskApp.route('/consultar-doacao/doador/consulta', methods=['POST']) 
@login_required
def consulta_doacao_por_doador():
    nome = request.form['nome']
    cpf = request.form['cpf']
    numero_registro = request.form['numeroRegistro']

    itens = request.form['itens']
    page = request.form['page']

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if itens:
        itens_pesquisados = int(itens)
    else:
        itens_pesquisados = 10

    parametros = []

    if nome:
       parametros.append(Doador.nome.like("%{}%".format(nome)))
    if cpf:
       parametros.append(Doador.cpf == cpf)
    if numero_registro:
       parametros.append(Doador.numero_registro == numero_registro)

    doador = Doador.query.filter(*parametros).first()

    if doador:
        doacoes = Doacao.query.filter_by(doador_id=doador.numero_registro).order_by(Doacao.data.desc())
        if doacoes.count() > 0:
            doacoes = doacoes.paginate(page=page, per_page=itens_pesquisados)
            return render_template("consultarDoacoesDoador.html", resultado=True, doacoes=doacoes.items, doador=doador, itens=itens_pesquisados, paginas=doacoes, nome=nome, cpf=cpf, numeroRegistro=numero_registro)
        else:
            return render_template("consultarDoacoesDoador.html", nenhumaDoacao=True)
    else:
        return render_template("consultarDoacoesDoador.html", usuarioNaoEncontrado=True)
