
from src.game import PartidaIndividual


def jugar_modo_individual():
    partida = PartidaIndividual()

    print("\n================================")
    print("        PICAS Y FIJAS")
    print("================================")
    print("¡Adivina el número secreto!")
    print("Tiene 4 dígitos diferentes.")
    print("No comienza por cero.")
    print(f"Tienes {partida.max_intentos} intentos.")
    print("--------------------------------")

    while not partida.terminada:
        intento = input(
            f"\nIntento {partida.intentos_realizados + 1}: "
        ).strip()

        resultado = partida.procesar_intento(intento)

        if not resultado["valido"]:
            print("Entrada inválida.")
            print("Escribe 4 dígitos diferentes y no comiences por cero.")
            continue

        print(f"Picas: {resultado['picas']}")
        print(f"Fijas: {resultado['fijas']}")
        print(f"Intentos restantes: {resultado['intentos_restantes']}")

        if resultado["ganada"]:
            print("\n¡FELICIDADES! ¡Adivinaste el número secreto!")
            print(f"Lo lograste en {partida.intentos_realizados} intento(s).")

        elif resultado["terminada"]:
            print("\n¡Se acabaron los intentos!")
            print(f"El número secreto era: {partida.numero_secreto}")
            print("¡Mejor suerte la próxima vez!")

    print("\nGracias por jugar Picas y Fijas.")


def main():
    jugar_modo_individual()


if __name__ == "__main__":
    main()
