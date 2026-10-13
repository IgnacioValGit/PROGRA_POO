from utilidades import leer_decimal

class MayorMenor:
    def ejecutar(self):
        mayor = menor = leer_decimal("numero 1: ")
        for i in range(2, 11):
            numero = leer_decimal(f"numero {i}: ")
            if numero > mayor:
                mayor = numero
            if numero < menor:
                menor = numero
        print(f"mayor: {mayor:g} , menor: {menor:g}")


if __name__ == "__main__":
    MayorMenor().ejecutar()
