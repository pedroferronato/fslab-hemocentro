from app import flaskApp
from flask import render_template


@flaskApp.route('/')
def doador():
    return render_template("base.html")
