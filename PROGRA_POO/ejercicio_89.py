from utilidades import leer_entero, leer_decimal

class ClasificadorSignos:
    def ejecutar(self):
        cantidad = leer_entero("cantidad de numeros: ", minimo=1)
        positivos = negativos = ceros = 0
        for i in range(cantidad):
            numero = leer_decimal(f"numero {i + 1}: ")
            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1
            else:
                ceros += 1
        print(f"positivos: {positivos} , negativos: {negativos} , ceros: {ceros}")


if __name__ == "__main__":
    ClasificadorSignos().ejecutar()
