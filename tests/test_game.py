
from src.game import generar_numero_secreto
from src.game import calcular_picas_y_fijas
from src.game import validar_intento, PartidaIndividual

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


def test_validar_intento_rechaza_longitud_incorrecta():
    assert validar_intento("582") is False
    assert validar_intento("58213") is False


def test_validar_intento_rechaza_digitos_repetidos():
    assert validar_intento("5581") is False


def test_validar_intento_rechaza_cero_inicial():
    assert validar_intento("0821") is False


def test_validar_intento_rechaza_letras():
    assert validar_intento("58A1") is False


def test_validar_intento_rechaza_numeros_enteros():
    assert validar_intento(5821) is False


def test_partida_inicia_con_diez_intentos():
    partida = PartidaIndividual(numero_secreto="5821")

    assert partida.intentos_restantes == 10
    assert partida.intentos_realizados == 0
    assert partida.terminada is False


def test_intento_invalido_no_descuenta_oportunidades():
    partida = PartidaIndividual(numero_secreto="5821")

    resultado = partida.procesar_intento("5581")

    assert resultado["valido"] is False
    assert partida.intentos_restantes == 10


def test_partida_gana_al_adivinar_numero():
    partida = PartidaIndividual(numero_secreto="5821")

    resultado = partida.procesar_intento("5821")

    assert resultado["ganada"] is True
    assert resultado["terminada"] is True
    assert resultado["fijas"] == 4
    assert partida.intentos_restantes == 9


def test_partida_pierde_al_agotar_intentos():
    partida = PartidaIndividual(
        numero_secreto="5821",
        max_intentos=2
    )

    partida.procesar_intento("6397")
    resultado = partida.procesar_intento("4069")

    assert resultado["ganada"] is False
    assert resultado["terminada"] is True
    assert resultado["intentos_restantes"] == 0


def test_no_permite_jugar_despues_de_terminar():
    import pytest

    partida = PartidaIndividual(numero_secreto="5821")
    partida.procesar_intento("5821")

    with pytest.raises(ValueError):
        partida.procesar_intento("1234")


def test_no_permite_numero_secreto_invalido():
    import pytest

    with pytest.raises(ValueError):
        PartidaIndividual(numero_secreto="5581")


def test_no_permite_maximo_de_intentos_invalido():
    import pytest

    with pytest.raises(ValueError):
        PartidaIndividual(numero_secreto="5821", max_intentos=0)