from app import db, login_manager
from flask_login import UserMixin

from app.models.hemocentro import Hemocentro


class Captador(db.Model, UserMixin):
    __tablename__ = 'captadores'

    id = db.Column(db.Integer, primary_key=True)
    hemocentro_id = db.Column(db.Integer, db.ForeignKey('hemocentros.id'), nullable=False)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    celular = db.Column(db.String(200), nullable=False)
    login = db.Column(db.String(200), nullable=False, unique=True)
    senha = db.Column(db.String(200), nullable=False)
    administrador = db.Column(db.Boolean(), default=False)
    servidor = db.Column(db.Boolean(), default=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return f'Captador: {self.email}'

