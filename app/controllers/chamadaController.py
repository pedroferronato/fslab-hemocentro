from app import flaskApp
from flask import render_template

@flaskApp.route('/convocacao-tipada')
def chamada_tipada():
    return render_template("convocacaoTipada.html")

