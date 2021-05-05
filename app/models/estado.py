from app import db


class Estado(db.Model):
    __tablename__ = 'estado'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(75))
    uf = db.Column(db.String(2))
    ibge = db.Column(db.Integer)
    ddd = db.Column(db.String(50))

    def __repr__(self):
        return self.nome