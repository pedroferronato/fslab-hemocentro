from app import db
from app.models.hemocentro import Hemocentro
from app.models.doador import Doador

from datetime import date


class Doacao(db.Model):
    __tablename__ = 'doacoes'

    id = db.Column(db.Integer, primary_key=True)
    hemocentro_id = db.Column(db.Integer, db.ForeignKey('hemocentros.id'), nullable=False)
    doador_id = db.Column(db.Integer, db.ForeignKey('doadores.numero_registro'), nullable=False)
    data = db.Column(db.Date(), nullable=False)
    convocacao = db.Column(db.String(200))
    observacao = db.Column(db.String(200))


    def __repr__(self):
        return f'Doação: {self.data}'

