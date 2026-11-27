
from src.game import generar_numero_secreto


def test_numero_secreto_tiene_cuatro_digitos():
    numero = generar_numero_secreto()

    assert len(numero) == 4


def test_numero_secreto_no_tiene_digitos_repetidos():
    numero = generar_numero_secreto()

    assert len(set(numero)) == 4


def test_numero_secreto_no_comienza_en_cero():
    numero = generar_numero_secreto()

    assert numero[0] != "0"


def test_numero_secreto_contiene_solo_digitos():
    numero = generar_numero_secreto()

    assert numero.isdigit()
