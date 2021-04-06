from app import db


class Doador(db.Model):
    __tablename__ = 'doador'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)

