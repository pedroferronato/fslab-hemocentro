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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import bcrypt
import smtplib
import os

@flaskApp.before_request
def make_session_permanent():
    session.permanent = True
    flaskApp.permanent_session_lifetime = timedelta(minutes=30)
    session.modified = True

@flaskApp.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'GET':
        sucesso = request.args.get('sucesso')
        mensagem = request.args.get('mensagem')
        return render_template("login.html", mensagem=mensagem, sucesso=sucesso)

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


def enviar_email(captador):
    email_from = str(os.getenv("EMAIL_LOGIN"))
    email_pass = str(os.getenv("EMAIL_PASS"))
    email_smtp_server = str(os.getenv("EMAIL_SERVER"))

    destination = [captador.email]

    assunto = 'Alteração de senha'

    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['Subject'] = assunto

    token = captador.get_reset_token()
    texto = f'''Solicitação de senha realizada, para fazer a alteração de sua senha acesse o link:<br> { url_for('recuperar_senha_token', token=token, _external=True) }. <br>Após acessar você será redirecionado para uma página de alteração de senha com um prazo de até 5 minutos para fazer sua alteração de senha.
<br>
Por favor não responda ou mande mensagens para este e-mail, não terá nenhuma resposta, entre em contato via telefone.
<br>
Atenciosamente,
<br>
FSLab & Sawenv.
    '''

    msg_text = MIMEText(texto, 'html')
    msg.attach(msg_text)

    smtp = smtplib.SMTP(email_smtp_server, 587)

    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_from, email_pass)
        smtp.sendmail(email_from, ','.join(destination), msg.as_string())
        smtp.quit()
    except Exception as e:
        flaskApp.logger.info(f'E-mail - Falha ao enviar E-mail: {e}')


@flaskApp.route('/recuperar-senha')
def recuperar_senha():
    return render_template("recuperarSenha.html")


@flaskApp.route('/recuperar-senha', methods=['POST'])
def recuperar_senha_envio():
    email = request.form['email']
    captador = Captador.query.filter_by(email=email).first()
    if captador:
        enviar_email(captador)
        flaskApp.logger.info(f'Recuperar senha - Foi enviado um e-mail de recuperacao de senha para: {email}')
        return render_template("recuperarSenha.html", envio=True)
    else:
        flaskApp.logger.info(f'Recuperar senha - Houve uma tentativa falha de alterar senha em um e-mail, o envio foi: {email}, não existe captador com este e-mail')
    return redirect(url_for('login'))


@flaskApp.route('/recuperar-senha/<token>', methods=['GET','POST'])
def recuperar_senha_token(token):
    captador = Captador.verify_reset_token(token)
    
    if captador is None:
        return render_template("alterarSenha.html", invalido=True)

    if request.method == 'GET':
        return render_template("alterarSenha.html")    
    
    if request.method == 'POST':
        password1 = request.form['password1']
        password2 = request.form['password2']

        if password1 != password2:
            return render_template("alterarSenha.html", diferentes=True)

        captador.senha = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
        
        db.session.add(captador)
        db.session.commit()

        return redirect(url_for("login", sucesso=True))


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


@flaskApp.route('/cidades/<estado>')
def get_cidade(estado):
    estado_id = Estado.query.filter_by(nome=estado).first().id
    cidades = Municipio.query.filter_by(uf=estado_id)
    cidades = [x.nome for x in cidades]
    response = jsonify(cidades)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
