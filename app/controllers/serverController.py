from app import flaskApp, db, login_manager
from app.models.utilidadeSistema import Utilidades
from app.models.captador import Captador
from flask import render_template, redirect, request, url_for, session
from flask_login import login_user, logout_user, login_required
from datetime import timedelta
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
        
        if not captador or not autorizado:
            mensagem = "Login não autorizado"
            return render_template("login.html", mensagem=mensagem)
        else:
            login_user(captador, remember=False)
            return redirect('/inicio')


@flaskApp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@login_manager.unauthorized_handler
def nao_autorizado():
    return redirect('/login')


@flaskApp.route('/recuperar-senha')
def recuperar_senha():
    return render_template("recuperarSenha.html")


@flaskApp.route('/inicio')
@login_required
def inicial():
    sucesso = request.args.get('sucesso')

    return render_template("paginaInicial.html", sucesso=sucesso)


@flaskApp.route('/perfil')
@login_required
def perfil():
    return render_template("perfil.html")


@flaskApp.route('/alterar-senha') # TODO: USAR ALGUMA FORMA DE IDENTIFICAÇÃO
def alterar_senha():
    return render_template("alterarSenha.html")


@flaskApp.route("/cidade/nova/<fonte>", methods=['POST'])
@login_required
def nova_cidade(fonte):
    nome_cidade = request.form['novaCidade']
    registradas = Utilidades.query.filter_by(cidade_registrada=nome_cidade)
    
    if registradas.count() == 0:
        cidade_nova = Utilidades(cidade_registrada=nome_cidade)
        db.session.add(cidade_nova)
        db.session.commit()

    if fonte == 'hemocentro':
        nome = request.form['nomeSafe']
        telefone = request.form['telefoneSafe']
        img = request.form['imgSafe']
        return redirect(url_for('novo_hemocentro', reload=True, nomeBKP=nome, telefoneBKP=telefone, imgBKP=img, cidade_adicionada=nome_cidade))
    elif fonte == 'doador': 
        num_registro_safe = request.form['numRegistroSafe']
        nome_safe = request.form['nomeSafe']
        cpf_safe = request.form['cpfSafe']
        sexo_safe = request.form['sexoSafe']
        tipo_sangue_safe = request.form['tipoSangueSafe']
        nascimento_safe = request.form['nascimentoSafe']
        sus_safe = request.form['susSafe']
        estado_civil_safe = request.form['estadoCivilSafe']
        celular_safe = request.form['celularSafe']
        telefone_safe = request.form['telefoneSafe']
        mail_safe = request.form['mailSafe']
        aviso_safe = request.form['avisoSafe']
        profissao_safe = request.form['profissaoSafe']
        local_trabalho_safe = request.form['localTrabalhoSafe']
        estado_aptidao_safe = request.form['estadoAptidaoSafe']
        data_inaptidao_safe = request.form['dataInaptidaoSafe']
        mae_safe = request.form['maeSafe']
        pai_safe = request.form['paiSafe']
        return redirect(url_for('novo_doador', reload=True, numRegistroBKP= num_registro_safe, nomeBKP= nome_safe, cpfBKP= cpf_safe, sexoBKP= sexo_safe, tipoSangueBKP= tipo_sangue_safe, nascimentoBKP= nascimento_safe, susBKP= sus_safe, estadoCivilBKP= estado_civil_safe, celularBKP= celular_safe, telefoneBKP= telefone_safe, mailBKP= mail_safe, avisoBKP= aviso_safe, profissaoBKP= profissao_safe, localTrabalhoBKP= local_trabalho_safe, estadoAptidaoBKP= estado_aptidao_safe, dataInaptidaoBKP= data_inaptidao_safe, maeBKP= mae_safe, paiBKP= pai_safe, cidade_adicionada=nome_cidade))

