from utilidades import leer_entero

class ContadorCompleto:
    def ejecutar(self):
        pares = impares = positivos = negativos = 0
        while True:
            numero = leer_entero("numero (0 para terminar): ")
            if numero == 0:
                break
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
            if numero > 0:
                positivos += 1
            else:
                negativos += 1
        print(f"pares: {pares} , impares: {impares}")
        print(f"positivos: {positivos} , negativos: {negativos}")


if __name__ == "__main__":
    ContadorCompleto().ejecutar()
