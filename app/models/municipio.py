from app import db
from app.models.estado import Estado


class Municipio(db.Model):
    __tablename__ = 'municipio'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    uf = db.Column(db.Integer, db.ForeignKey('estado.id'))
    ibge = db.Column(db.Integer)

    def __repr__(self):
        return self.nome