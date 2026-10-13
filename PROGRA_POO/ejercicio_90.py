from utilidades import leer_entero, leer_opcion

class TablasMultiplicar:
    def mostrar_tabla(self, numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    def ejecutar(self):
        while True:
            numero = leer_entero("numero para la tabla: ")
            self.mostrar_tabla(numero)
            if leer_opcion("otra tabla? (si/no): ", {"si", "n"}) == "n":
                break


if __name__ == "__main__":
    TablasMultiplicar().ejecutar()
