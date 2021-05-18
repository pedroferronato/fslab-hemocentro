from app import db
from app.models.estado import Estado
from app.models.municipio import Municipio


class Hemocentro(db.Model):
    __tablename__ = 'hemocentros'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False, unique=True)
    municipio = db.Column(db.Integer, db.ForeignKey('municipio.id'), nullable=False)
    telefone = db.Column(db.String(40), nullable=False)
    urlImg =  db.Column(db.String(100))

    def get_nome(self):
        return self.nome

    
    def get_img(self):
        return self.urlImg


    def get_id(self):
        return self.id


    def __repr__(self):
        return f"Hemocentro: {self.nome}"


    def get_municipio(self):
        return self.municipio


    def get_municipio_nome(self):
        return Municipio.query.filter_by(id=self.municipio).first().nome

    
    def get_estado(self):
        return Estado.query.filter_by(id=Municipio.query.filter_by(id=self.municipio).first().uf).first()
