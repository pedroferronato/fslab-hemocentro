from app import db
from app.models.doador import Doador

doador = Doador(nome="Teste")
db.session.add(doador)
db.session.commit()
