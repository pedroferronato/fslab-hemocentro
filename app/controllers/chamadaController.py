from app import flaskApp
from flask import render_template

@flaskApp.route('/convocacao-tipada')
@login_required
def chamada_tipada():
    return render_template("convocacaoTipada.html", tipo="tipada")


@flaskApp.route('/convocacao-tipada/resultado')
@login_required
def chamada_tipada_resultado():
    return render_template("convocacaoTipada.html", tipo="tipada", resultado=True)


@flaskApp.route('/convocacao-emergencial')
@login_required
def chamada_emergencial():
    return render_template("convocacaoEmergencial.html", tipo="emergencial")


@flaskApp.route('/convocacao-emergencial/resultado')
@login_required
def chamada_emergencial_resultado():
    return render_template("convocacaoEmergencial.html", tipo="emergencial", resultado=True)


@flaskApp.route('/convocacao-localidades-externas')
@login_required
def chamada_localidades_externas():
    return render_template("convocacaoLocalidadesExternas.html")


@flaskApp.route('/convocacao-localidades-externas/resultado')
@login_required
def chamada_localidades_externas_resultado():
    return render_template("convocacaoLocalidadesExternas.html", resultado=True)


@flaskApp.route('/convocacao-convocados')
@login_required
def chamada_convocados():
    return render_template("convocacaoConvocados.html")


@flaskApp.route('/convocacao-convocados/resultado')
@login_required
def chamada_convocados_resultado():
    return render_template("convocacaoConvocados.html", resultado=True)

