from utilidades import leer_entero

class ContadorParidad:
    def ejecutar(self):
        pares = impares = 0
        for i in range(10):
            numero = leer_entero(f"numero {i + 1}: ")
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        print(f"pares: {pares} , impares: {impares}")


if __name__ == "__main__":
    ContadorParidad().ejecutar()
