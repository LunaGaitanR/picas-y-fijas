
from src.game import generar_numero_secreto
from src.game import calcular_picas_y_fijas
from src.game import validar_intento

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


def test_calcular_picas_y_fijas_con_dos_fijas_y_una_pica():
    picas, fijas = calcular_picas_y_fijas("5821", "5129")

    assert picas == 1
    assert fijas == 2
def test_calcular_picas_y_fijas_con_todas_fijas():
    picas, fijas = calcular_picas_y_fijas("5821", "5821")

    assert picas == 0
    assert fijas == 4


def test_calcular_picas_y_fijas_sin_coincidencias():
    picas, fijas = calcular_picas_y_fijas("5821", "6397")

    assert picas == 0
    assert fijas == 0


def test_calcular_picas_y_fijas_con_todas_picas():
    picas, fijas = calcular_picas_y_fijas("5821", "1285")

    assert picas == 4
    assert fijas == 0


def test_validar_intento_acepta_numero_correcto():
    assert validar_intento("5821") is True


def test_validar_intento_rechaza_numero_corto():
    assert validar_intento("582") is False


def test_validar_intento_rechaza_numero_largo():
    assert validar_intento("58213") is False


def test_validar_intento_rechaza_digitos_repetidos():
    assert validar_intento("5581") is False


def test_validar_intento_rechaza_cero_al_inicio():
    assert validar_intento("0821") is False


def test_validar_intento_rechaza_letras():
    assert validar_intento("58A1") is False


def test_validar_intento_rechaza_valores_no_textuales():
    assert validar_intento(5821) is False
