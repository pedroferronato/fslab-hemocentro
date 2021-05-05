from app import db
from app.models.doacao import Doacao

from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class Doador(db.Model):
    __tablename__ = 'doadores'

    numero_registro = db.Column(db.Integer, primary_key=True, autoincrement=False)
    hemocentro_id = db.Column(db.Integer, db.ForeignKey('hemocentros.id'), primary_key=True, autoincrement=False)
    nome = db.Column(db.String(200), nullable=False)
    cpf = db.Column(db.String(200), nullable=False)
    data_de_nascimento = db.Column(db.Date(), nullable=False)
    idade = db.Column(db.Integer)
    tipo_sanguineo = db.Column(db.String(200), nullable=False)
    municipio = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(200))
    celular = db.Column(db.String(200))
    email = db.Column(db.String(200))
    cadastro_SUS = db.Column(db.String(200), nullable=False)
    sexo = db.Column(db.String(200), nullable=False)
    estado_civil = db.Column(db.String(200))
    avisado = db.Column(db.Boolean(), default=0)
    contatado = db.Column(db.Boolean(), default=0)
    contatos_preferidos = db.Column(db.String(200))
    nome_mae = db.Column(db.String(200))
    nome_pai = db.Column(db.String(200))
    profissao = db.Column(db.String(200))
    local_trabalho = db.Column(db.String(200))
    fidelidade = db.Column(db.String(200))
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


    def definir_inaptidao(self, inaptidao, data):
        self.inaptidao = inaptidao
        self.final_inaptidao = data
        if data is None and inaptidao:
            self.final_inaptidao = datetime.today() + relativedelta(months=1)
            
    
    def get_idade(self):
        self.idade = (hoje.year - self.data_de_nascimento.year - ((hoje.month, hoje.day) < (self.data_de_nascimento.month, self.data_de_nascimento.day)))
        db.session.add(self)
        db.session.commit()
        return self.idade


    def dia_do_aniversario(self):
        # Deve retornar um booleano (é ou não dia de seu aniversário)
        pass


    def get_ultima_doacao(self):
        return Doacao.query.order_by(Doacao.data.desc()).filter_by(doador_id=self.numero_registro).first()


    def get_total_doacoes(self):
        return len(Doacao.query.filter_by(doador_id=self.numero_registro).all())


    def get_ultimas_dez_doacoes(self):
        return Doacao.query.filter_by(doador_id=self.numero_registro).order_by(Doacao.data.desc()).limit(10).all()

