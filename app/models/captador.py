from app import db, login_manager, flaskApp
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.models.hemocentro import Hemocentro


class Captador(db.Model, UserMixin):
    __tablename__ = 'captadores'

    id = db.Column(db.Integer, primary_key=True)
    hemocentro_id = db.Column(db.Integer, db.ForeignKey('hemocentros.id'), nullable=False)
    nome = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    celular = db.Column(db.String(40), nullable=False)
    login = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)
    administrador = db.Column(db.Boolean(), default=False)
    servidor = db.Column(db.Boolean(), default=False)
    ativo = db.Column(db.Boolean(), default=True)


    def is_authenticated(self):
        return True


    def is_active(self):
        return True


    def is_anonymous(self):
        return False


    def get_id(self):
        return self.id


    def get_cargo(self):
        if self.servidor:
            return 'Servidor'
        else:
            return 'Captador'

    
    def get_hemocentro(self):
        return Hemocentro.query.filter_by(id=self.hemocentro_id).first()

    
    def get_nome(self):
        return self.nome


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(flaskApp.config['SECRET_KEY'], expires_sec)
        return s.dumps({'captador_id' : self.id}).decode('utf-8')


    @staticmethod
    def verify_reset_token(token):
        s = Serializer(flaskApp.config['SECRET_KEY'])
        try:
            captador_id = s.loads(token)['captador_id']
        except:
            return None
        return Captador.query.get(captador_id)


    def __repr__(self):
        return f'Captador: {self.email}'

