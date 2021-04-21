from app import db


class Hemocentro(db.Model):
    __tablename__ = 'hemocentros'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False, unique=True)
    municipio = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(200), nullable=False)
    urlImg =  db.Column(db.String(200))

    def get_nome(self):
        return self.nome

    
    def get_img(self):
        return self.urlImg


    def __repr__(self):
        return f"Hemocentro: {self.nome}"

