from app import flaskApp
from flask import render_template


@flaskApp.route('/doador')
def doador():
    return render_template("index.html")