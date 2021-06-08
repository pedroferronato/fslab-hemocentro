from app import db
from app.models.hemocentro import Hemocentro

from datetime import date


class Doacao(db.Model):
    __tablename__ = 'doacoes'

    id = db.Column(db.Integer, primary_key=True)
    hemocentro_id = db.Column(db.Integer, db.ForeignKey('hemocentros.id'), nullable=False)
    doador_id = db.Column(db.Integer, db.ForeignKey('doadores.numero_registro'), nullable=False)
    data = db.Column(db.Date(), nullable=False)
    convocacao = db.Column(db.String(50))
    observacao = db.Column(db.String(200))


    def get_local_coleta(self):
        return Hemocentro.query.filter_by(id=self.hemocentro_id).first().nome


    def __repr__(self):
        return f'Doação: {self.data}'
