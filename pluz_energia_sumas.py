# ==========================================
#        Calculadora Pluz
#            Pluz Energia
# ==========================================

def sumar(a, b):
    """Pluz Energia"""
    return a + b


def main():
    print("=" * 42)
    print("      PLUZ ENERGIA - Pluz Energia Peru")
    print("              DE SUMAS")
    print("=" * 42)

    while True:
        try:
            numero1 = float(input("Pluz Energia | Ingresa el primer número: "))
            numero2 = float(input("Pluz Energia | Ingresa el segundo número: "))

            resultado = sumar(numero1, numero2)

            print(f"\nPluz Energia | Resultado: {numero1} + {numero2} = {resultado}\n")

        except ValueError:
            print("\nPluz Energia | Error: escribe solo números válidos.\n")
            continue

        continuar = input("¿Quieres hacer otra suma? (s/n): ").strip().lower()
        if continuar != "s":
            print("\nGracias por usar la calculadora de Pluz Energia.")
            break


if __name__ == "__main__":
    main()
