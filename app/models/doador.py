from app import db
from app.models.doacao import Doacao
from app.models.municipio import Municipio

from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class Doador(db.Model):
    __tablename__ = 'doadores'

    numero_registro = db.Column(db.Integer, primary_key=True, autoincrement=False)
    hemocentro_id = db.Column(db.Integer, db.ForeignKey('hemocentros.id'), primary_key=True, autoincrement=False)
    nome = db.Column(db.String(200), nullable=False)
    cpf = db.Column(db.String(50), nullable=False)
    data_de_nascimento = db.Column(db.Date(), nullable=False)
    idade = db.Column(db.Integer)
    tipo_sanguineo = db.Column(db.String(5), nullable=False)
    municipio = db.Column(db.Integer, db.ForeignKey('municipio.id'), nullable=False)
    telefone = db.Column(db.String(40))
    celular = db.Column(db.String(40))
    email = db.Column(db.String(150))
    cadastro_SUS = db.Column(db.String(30), nullable=False)
    sexo = db.Column(db.String(3), nullable=False)
    estado_civil = db.Column(db.String(50))
    avisado = db.Column(db.Boolean(), default=0)
    contatado = db.Column(db.Boolean(), default=0)
    contatos_preferidos = db.Column(db.String(50))
    nome_mae = db.Column(db.String(200))
    nome_pai = db.Column(db.String(200))
    profissao = db.Column(db.String(100))
    local_trabalho = db.Column(db.String(100))
    fidelidade = db.Column(db.String(50))
    inaptidao = db.Column(db.Boolean(), default=False)
    final_inaptidao = db.Column(db.Date())
    legado = db.Column(db.Boolean(), default=False)
    ultima_doacao = db.Column(db.Date())


    def __repr__(self):
        return f'Doador: {self.nome}'


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        LIMITE_SUPERIOR_IDADE_DOADOR = 60
        hoje = date.today()
        self.idade = (hoje.year - self.data_de_nascimento.year - ((hoje.month, hoje.day) < (self.data_de_nascimento.month, self.data_de_nascimento.day)))
        if self.idade > LIMITE_SUPERIOR_IDADE_DOADOR:
            self.legado = True


    def get_idade(self):
        hoje = date.today()
        return (hoje.year - self.data_de_nascimento.year - ((hoje.month, hoje.day) < (self.data_de_nascimento.month, self.data_de_nascimento.day)))


    def get_ultima_doacao(self):
        return Doacao.query.order_by(Doacao.data.desc()).filter_by(doador_id=self.numero_registro).first()


    def get_total_doacoes(self):
        return len(Doacao.query.filter_by(doador_id=self.numero_registro).all())


    def get_ultimas_dez_doacoes(self):
        return Doacao.query.filter_by(doador_id=self.numero_registro).order_by(Doacao.data.desc()).limit(10).all()


    def get_municipio(self):
        return Municipio.query.filter_by(id=self.municipio).first().nome

