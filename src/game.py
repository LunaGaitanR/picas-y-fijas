import random


def generar_numero_secreto():
    """
    Genera un número secreto de 4 cifras,
    sin dígitos repetidos y sin iniciar en cero.
    """
    primer_digito = random.choice("123456789")
    otros_digitos = random.sample(
        [str(d) for d in range(10) if str(d) != primer_digito],
        3
    )

    return primer_digito + "".join(otros_digitos)


def calcular_picas_y_fijas(numero_secreto, intento):
    """
    Calcula la cantidad de picas y fijas entre
    el número secreto y el intento del jugador.

    Retorna una tupla: (picas, fijas).
    """
    fijas = 0
    picas = 0

    for posicion in range(4):
        if intento[posicion] == numero_secreto[posicion]:
            fijas += 1
        elif intento[posicion] in numero_secreto:
            picas += 1

    return picas, fijas


def validar_intento(intento):
    """
    Comprueba que un intento sea un número válido
    de cuatro dígitos, sin repeticiones y sin iniciar en cero.
    """
    if not isinstance(intento, str):
        return False

    if len(intento) != 4:
        return False

    if not all(digito in "0123456789" for digito in intento):
        return False

    if intento[0] == "0":
        return False

    if len(set(intento)) != 4:
        return False

    return True

