from utilidades import leer_decimal, leer_opcion

class Calculadora:
    def calcular(self, opcion, a, b):
        if opcion == "1":
            return a + b
        elif opcion == "2":
            return a - b
        elif opcion == "3":
            return a * b
        elif opcion == "4":
            if b == 0:
                print("No se puede dividir entre cero.")
                return None
            return a / b

    def ejecutar(self):
        while True:
            print("\n1. sumar  2. restar  3. multiplicar  4. dividir  5. salir")
            op = leer_opcion("Opción: ", {"1", "2", "3", "4", "5"})
            if op == "5":
                break
            a = leer_decimal("Primer numero: ")
            b = leer_decimal("Segundo numero: ")
            resultado = self.calcular(op, a, b)
            if resultado is not None:
                print(f"resultado: {resultado:g}")


if __name__ == "__main__":
    Calculadora().ejecutar()
