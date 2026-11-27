
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


def validar_intento(intento):
    """
    Comprueba que el intento tenga cuatro dígitos,
    que no comience en cero y que no repita dígitos.
    """
    if not isinstance(intento, str):
        return False

    if len(intento) != 4:
        return False

    if not intento.isdigit():
        return False

    if intento[0] == "0":
        return False

    if len(set(intento)) != 4:
        return False

    return True


def calcular_picas_y_fijas(numero_secreto, intento):
    """
    Calcula la cantidad de picas y fijas.
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


class PartidaIndividual:
    """
    Controla una partida individual de Picas y Fijas.
    """

    def __init__(self, numero_secreto=None, max_intentos=10):
        if not isinstance(max_intentos, int) or max_intentos <= 0:
            raise ValueError("El máximo de intentos debe ser positivo.")

        if numero_secreto is None:
            numero_secreto = generar_numero_secreto()

        if not validar_intento(numero_secreto):
            raise ValueError("El número secreto no es válido.")

        self.numero_secreto = numero_secreto
        self.max_intentos = max_intentos
        self.intentos_realizados = 0
        self.ganada = False
        self.terminada = False

    @property
    def intentos_restantes(self):
        return self.max_intentos - self.intentos_realizados

    def procesar_intento(self, intento):
        """
        Procesa un intento y devuelve el resultado de la jugada.
        Los intentos inválidos no descuentan oportunidades.
        """
        if self.terminada:
            raise ValueError("La partida ya ha terminado.")

        if not validar_intento(intento):
            return {
                "valido": False,
                "mensaje": "El intento no es válido.",
                "picas": None,
                "fijas": None,
                "intentos_restantes": self.intentos_restantes,
                "ganada": False,
                "terminada": False
            }

        self.intentos_realizados += 1

        picas, fijas = calcular_picas_y_fijas(
            self.numero_secreto,
            intento
        )

        if fijas == 4:
            self.ganada = True
            self.terminada = True
        elif self.intentos_restantes == 0:
            self.terminada = True

        return {
            "valido": True,
            "mensaje": "Intento procesado.",
            "picas": picas,
            "fijas": fijas,
            "intentos_restantes": self.intentos_restantes,
            "ganada": self.ganada,
            "terminada": self.terminada
        }
