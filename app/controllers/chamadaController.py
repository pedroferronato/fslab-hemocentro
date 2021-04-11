from app import flaskApp
from flask import render_template

@flaskApp.route('/convocacao-tipada')
def chamada_tipada():
    return render_template("convocacaoTipada.html", tipo="tipada")


@flaskApp.route('/convocacao-tipada/resultado')
def chamada_tipada_resultado():
    return render_template("convocacaoTipada.html", tipo="tipada", resultado=True)


@flaskApp.route('/convocacao-emergencial')
def chamada_emergencial():
    return render_template("convocacaoEmergencial.html", tipo="emergencial")


@flaskApp.route('/convocacao-emergencial/resultado')
def chamada_emergencial_resultado():
    return render_template("convocacaoEmergencial.html", tipo="emergencial", resultado=True)


@flaskApp.route('/convocacao-localidades-externas')
def chamada_localidades_externas():
    return render_template("convocacaoLocalidadesExternas.html")


@flaskApp.route('/convocacao-localidades-externas/resultado')
def chamada_localidades_externas_resultado():
    return render_template("convocacaoLocalidadesExternas.html", resultado=True)


@flaskApp.route('/convocacao-convocados')
def chamada_convocados():
    return render_template("convocacaoConvocados.html")


@flaskApp.route('/convocacao-convocados/resultado')
def chamada_convocados_resultado():
    return render_template("convocacaoConvocados.html", resultado=True)

