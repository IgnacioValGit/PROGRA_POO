from utilidades import leer_entero

class RegistroEdades:
    def ejecutar(self):
        mayores = menores = 0
        while True:
            edad = leer_entero("edad (0 para terminar): ", minimo=0)
            if edad == 0:
                break
            if edad >= 18:
                mayores += 1
            else:
                menores += 1
        print(f"mayores de edad: {mayores} , menores de edad: {menores}")


if __name__ == "__main__":
    RegistroEdades().ejecutar()
