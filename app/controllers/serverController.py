from flask.helpers import url_for
from app.models.doador import Doador
from app import flaskApp, login_manager, db
from app.models.captador import Captador
from app.models.doacao import Doacao
from app.models.estado import Estado
from app.models.municipio import Municipio
from flask import render_template, redirect, request, session, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from datetime import timedelta, date
import bcrypt

@flaskApp.before_request
def make_session_permanent():
    session.permanent = True
    flaskApp.permanent_session_lifetime = timedelta(minutes=30)
    session.modified = True

@flaskApp.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        mensagem = request.args.get('mensagem')
        return render_template("login.html", mensagem=mensagem)

    elif request.method == 'POST':

        login = request.form['login']
        senha = request.form['senha']

        captador = Captador.query.filter_by(login=login).first()

        autorizado = False
        if captador:
            autorizado = bcrypt.checkpw(senha.encode('UTF-8'), captador.senha.encode('UTF-8'))
        
        if not captador or not autorizado or not captador.ativo:
            mensagem = "Login não autorizado"
            return render_template("login.html", mensagem=mensagem)
        else:
            login_user(captador, remember=False)
            flaskApp.logger.info(f'Login - o captador { current_user.nome } de login: { current_user.login } acessou o sistema')
            return redirect('/')


@flaskApp.route('/logout')
@login_required
def logout():
    flaskApp.logger.info(f'Login - o captador { current_user.nome } de login: { current_user.login } saiu do sistema')
    logout_user()
    return redirect('/login')


@login_manager.unauthorized_handler
def nao_autorizado():
    return redirect('/login')


@flaskApp.route('/recuperar-senha')
def recuperar_senha():
    return render_template("recuperarSenha.html")


@flaskApp.route('/')
@login_required
def inicial():
    sucesso = request.args.get('sucesso')
    return render_template("paginaInicial.html", sucesso=sucesso)


@flaskApp.route('/dashboard')
@login_required
def dashboard():
    hoje = date.today()
    diasDoMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    meses = ["Janeiro", "Fevereiro", "Março","Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    relatorioDoacoes = []
    for x in range(1,13):
        relatorioDoacoes.append({
            meses[x-1]:
            Doacao.query.filter(Doacao.data.between(str(hoje.year)+'-'+str(x)+'-01',str(hoje.year)+'-'+str(x)+'-'+str(diasDoMes[x-1])), Doacao.hemocentro_id.like(current_user.get_hemocentro().id)).count()
        })

    aPositivo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'A+', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    aNegativo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'A-', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    bPositivo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'B+', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    bNegativo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'B-', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    abPositivo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'AB+', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    abNegativo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'AB-', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    oPositivo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'O+', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    oNegativo = db.session.query(Doacao.doador_id).filter(Doacao.doador_id == Doador.numero_registro, Doador.tipo_sanguineo == 'O-', Doacao.hemocentro_id == current_user.get_hemocentro().id, Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doador.hemocentro_id == current_user.get_hemocentro().id).count()
    lista_doacoes_por_tipo = [aPositivo, aNegativo, bPositivo, bNegativo, abPositivo, abNegativo, oPositivo, oNegativo]
    diaHoje = Doacao.query.filter(Doacao.data.between(str(hoje.year)+'-'+(str(hoje.month))+'-'+(str(hoje.day)),(str(hoje.year))+'-'+(str(hoje.month))+'-'+(str(hoje.day))), Doacao.hemocentro_id.like(current_user.get_hemocentro().id)).count()
    mes = Doacao.query.filter(Doacao.data.between(str(hoje.year)+'-'+(str(hoje.month))+'-01',(str(hoje.year))+'-'+(str(hoje.month))+'-'+(str(hoje.day))), Doacao.hemocentro_id.like(current_user.get_hemocentro().id)).count()
    anual = Doacao.query.filter(Doacao.data.between(str(hoje.year)+'-01-01',str(hoje.year)+'-12-31'), Doacao.hemocentro_id.like(current_user.get_hemocentro().id)).count()

    return render_template("dashboard.html", relatorioDoacoes=relatorioDoacoes, diaHoje=diaHoje, mes=mes, anual=anual, hoje = [hoje.day, meses[hoje.month - 1], hoje.year], lista_doacoes_por_tipo=lista_doacoes_por_tipo)


@flaskApp.route('/perfil')
@login_required
def perfil():
    return render_template("perfil.html")


@flaskApp.route('/perfil', methods=['POST'])
@login_required
def alterar_perfil():
    nome = request.form['nome']
    celular = request.form['celular']
    email = request.form['email']
    login = request.form['login']

    captador = Captador.query.filter_by(id=current_user.id).first()
    
    captador.nome = nome
    captador.celular = celular
    captador.email = email
    captador.login = login

    try:
        db.session.add(captador)
        db.session.commit()
    except:
        db.session.rollback()
        flaskApp.logger.info(f'Perfil - o captador { current_user.nome } de login: { current_user.login } tentou alterar informações em seu perfil, mas falhou')
        return render_template("perfil.html", mensagem="ErroBD")

    flaskApp.logger.info(f'Perfil - o captador { current_user.nome } de login: { current_user.login } alterou informações em seu perfil')
    return render_template("perfil.html", mensagem="Alterado")


@flaskApp.route('/alterar-senha') # TODO: USAR ALGUMA FORMA DE IDENTIFICAÇÃO
def alterar_senha():
    return render_template("alterarSenha.html")


@flaskApp.route('/cidades/<estado>')
def get_cidade(estado):
    estado_id = Estado.query.filter_by(nome=estado).first().id
    cidades = Municipio.query.filter_by(uf=estado_id)
    cidades = [x.nome for x in cidades]
    response = jsonify(cidades)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
