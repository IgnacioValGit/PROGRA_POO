from utilidades import leer_entero, leer_opcion

class MenuMatematico:
    def factorial(self, numero):
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

    def tabla(self, numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    def ejecutar(self):
        while True:
            print("\n1. factorial  2. tabla  3. paridad  4. cuadrado  5. salir")
            op = leer_opcion("Opcion: ", {"1", "2", "3", "4", "5"})
            if op == "5":
                break
            numero = leer_entero("Numero: ", minimo=0 if op == "1" else None)
            if op == "1":
                print(f"Factorial: {self.factorial(numero)}")
            elif op == "2":
                self.tabla(numero)
            elif op == "3":
                print("Par" if numero % 2 == 0 else "Impar")
            else:
                print(f"Cuadrado: {numero ** 2}")


if __name__ == "__main__":
    MenuMatematico().ejecutar()
