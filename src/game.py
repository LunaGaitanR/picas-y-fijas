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