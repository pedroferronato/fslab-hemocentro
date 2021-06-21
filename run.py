from app import flaskApp, db

from sqlalchemy.sql.expression import extract
from app.models.doador import Doador
from datetime import datetime
from sqlalchemy import and_, or_
from dateutil.relativedelta import relativedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import smtplib
import os
import time
import threading


def iniciar_flask():
    flaskApp.run(debug=False, use_reloader=False)


def get_lista_inaptos_para_aptos():
    filtros = []

    filtros.append(Doador.ativo == True)
    filtros.append(Doador.inaptidao == True)
    filtros.append(Doador.legado == False)
    filtros.append(and_(Doador.idade < 70, Doador.idade > 15))
    filtros.append(Doador.final_inaptidao == datetime.today().date())

    doadores_alterar_para_aptos = Doador.query.filter(*filtros).all()
   
    return doadores_alterar_para_aptos


def alterar_doadores_inaptos_para_aptos(lista):
    for doador in lista:
        doador.final_inaptidao = None
        doador.inaptidao = False
        db.session.add(doador)
        db.session.commit()
    

def get_lista_doadores_aptos_nao_contatados():
    filtros = []

    filtros.append(Doador.ativo == True)
    filtros.append(
        or_(
            and_(Doador.sexo == "mas", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=3))), 
            and_(Doador.sexo == "fem", Doador.ultima_doacao <= (datetime.today() - relativedelta(months=4)))
        )
    )
    filtros.append(Doador.avisado == False)
    filtros.append(Doador.contatado == False)
    filtros.append(Doador.inaptidao == False)
    filtros.append(Doador.legado == False)
    filtros.append(and_(Doador.idade < 70, Doador.idade > 15))
    filtros.append(or_(Doador.contatos_preferidos == 'email', Doador.contatos_preferidos == 'email&sms'))
    filtros.append(Doador.email != '')
    
    doadores_enviar_email = Doador.query.filter(*filtros).all()

    return doadores_enviar_email


def enviar_notificacao_doador_para_doacao(lista):
    email_from = str(os.getenv("EMAIL_LOGIN"))
    email_pass = str(os.getenv("EMAIL_PASS"))
    email_smtp_server = str(os.getenv("EMAIL_SERVER"))

    assunto = "Retorno já pode ser realizado"

    for doador in lista:
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['Subject'] = assunto

        texto = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">
</head>
<body style="font-family: 'Quicksand', sans-serif;">
    <div style="-webkit-box-shadow: 0px 0px 22px 5px #B7B7B7; 
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25); border-radius: 4px; padding-left: 16px; padding-bottom: 16px;">
    <h2 style="padding-top: 16px;">Já é possivel doar novamente</h2>
    <p style="margin-top: 24px;">Olá, { doador.nome }.</p>
    <p>Agradecemos suas doações no hemocentro { doador.get_hemocentro_nome() } e gostariamos de informar que já é possível realizar uma nova doação,
    </p>
    <p style="margin-top: 48px;">Desde já gratos,</p>
    <p>Equipe { doador.get_hemocentro_nome() }.</p>
    <p style="padding-bottom: 0px;">Telefone: { doador.get_hemocentro_telefone() }</p>
    </div>
</body>
</html>
        '''
        msg_text = MIMEText(texto, 'html')
        msg.attach(msg_text)

        smtp = smtplib.SMTP(email_smtp_server, 587)

        destination = [doador.email]
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_from, email_pass)
            smtp.sendmail(email_from, ','.join(destination), msg.as_string())
            smtp.quit()
            doador.avisado = True
            db.session.add(doador)
            db.session.commit()
        except Exception as e:
            flaskApp.logger.info(f'E-mail - Falha ao enviar E-mail de retorno para { destination }: {e}')
        time.sleep(10)

def get_aniversariantes():
    hoje = datetime.today().date()
    filtros = []

    filtros.append(Doador.ativo == True)
    filtros.append(Doador.legado == False)
    filtros.append(Doador.ultima_doacao != None)
    filtros.append(and_(Doador.idade < 70, Doador.idade > 15))
    filtros.append(or_(Doador.contatos_preferidos == 'email', Doador.contatos_preferidos == 'email&sms'))
    filtros.append(Doador.email != '')
    filtros.append(and_(
            extract('day', Doador.data_de_nascimento) == hoje.day,
            extract('month', Doador.data_de_nascimento) == hoje.month))

    aniversariantes = Doador.query.filter(*filtros).all()
    return aniversariantes


def enviar_parabenizacao_aniversario(lista):
    email_from = str(os.getenv("EMAIL_LOGIN"))
    email_pass = str(os.getenv("EMAIL_PASS"))
    email_smtp_server = str(os.getenv("EMAIL_SERVER"))

    assunto = "Feliz aniversário"

    for doador in lista:
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['Subject'] = assunto

        texto = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">
</head>
<body style="font-family: 'Quicksand', sans-serif;">
    <div style="-webkit-box-shadow: 0px 0px 22px 5px #B7B7B7; 
    box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.25); border-radius: 4px; padding-left: 16px; padding-bottom: 16px;">
    <h2 style="padding-top: 16px;">Parabéns</h2>
    <p style="margin-top: 24px;">Olá, { doador.nome }.</p>
    <p>Hoje é um dia muito especial, nós do { doador.get_hemocentro_nome() } damos os parabéns pelo seu aniversário, e gostariamos também de agradecer sua grande contribuição.
    </p>
    <p style="margin-top: 48px;">Felicidades,</p>
    <p>Equipe { doador.get_hemocentro_nome() }.</p>
    <p style="padding-bottom: 0px;">Telefone: { doador.get_hemocentro_telefone() }</p>
    </div>
</body>
</html>
        '''
        msg_text = MIMEText(texto, 'html')
        msg.attach(msg_text)

        smtp = smtplib.SMTP(email_smtp_server, 587)

        destination = [doador.email]
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_from, email_pass)
            smtp.sendmail(email_from, ','.join(destination), msg.as_string())
            smtp.quit()
        except Exception as e:
            flaskApp.logger.info(f'E-mail - Falha ao enviar E-mail de parabens para { destination }: {e}')
        time.sleep(10)


def enviar_mensagens():
    diaAnterior = open('envioMensagensSP.txt', 'r').readline()
    diaAnterior = datetime.strptime(diaAnterior, '%Y-%m-%d')
    while True:
        arquivo = open('envioMensagensSP.txt', 'w')
        
        diaAtual = datetime.today().date()

        if diaAtual != diaAnterior:
            lista_inaptos_para_aptos = get_lista_inaptos_para_aptos()
            if len(lista_inaptos_para_aptos) > 0:
                alterar_doadores_inaptos_para_aptos(lista_inaptos_para_aptos)
                time.sleep(2)

            lista_doadores_aptos_nao_contatados = get_lista_doadores_aptos_nao_contatados()
            if len(lista_doadores_aptos_nao_contatados) > 0:
                enviar_notificacao_doador_para_doacao(lista_doadores_aptos_nao_contatados)
                time.sleep(2)

            aniversariantes = get_aniversariantes()
            if len(aniversariantes) > 0:
                enviar_parabenizacao_aniversario(aniversariantes)
                time.sleep(2)

        diaAnterior = diaAtual
        arquivo.writelines([str(diaAnterior)])
        arquivo.close()
        time.sleep(3600)
        

if __name__ == '__main__':
    threading.Thread(target=iniciar_flask).start()
    threading.Thread(target=enviar_mensagens).start()

