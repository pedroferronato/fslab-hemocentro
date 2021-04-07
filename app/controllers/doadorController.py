from app import flaskApp
from flask import render_template

@flaskApp.route('/pagina-inicial')
def doador():
    return render_template("paginaInicial.html")
