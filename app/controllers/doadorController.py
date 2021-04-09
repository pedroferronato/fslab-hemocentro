from app import flaskApp
from flask import render_template


@flaskApp.route('/pagina-inicial')
def doador():
    return render_template("paginaInicial.html")


@flaskApp.route('/novo-doador')
def novoDoador():
    return render_template("doadorNovo.html")

