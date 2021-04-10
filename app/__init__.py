from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

flaskApp = Flask(__name__)
flaskApp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ os.getenv("DB_USUARIO") +':'+ os.getenv("DB_SENHA") +'@'+ os.getenv("DB_LOCAL") + '/' + os.getenv("DB_BASEDEDADOS")
flaskApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db, compare_type=True)
manager = Manager(flaskApp)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(flaskApp)
login_manager.init_app(flaskApp)

import app.models.hemocentro
import app.models.doador
import app.models.doacao
import app.models.captador

from app.controllers import doadorController
from app.controllers import captadorController
from app.controllers import serverController

from app.controllers import chamadaController
