from app.models.doador import Doador
from datetime import date

def test_validar_preenchimento_automatico_idade_doador_criado():
    doador = Doador(data_de_nascimento=date(2001, 4, 2))
    assert None != doador.idade
