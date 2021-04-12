from app import db


class Utilidades(db.Model):
    __tablename__ = 'utilidades'

    id = db.Column(db.Integer, primary_key=True)
    cidade_registrada = db.Column(db.String(200), nullable=False, unique=True)

    def __repr__(self):
        return f"Hemocentro: {self.cidade_registrada}"
