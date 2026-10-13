import math
from utilidades import leer_decimal, leer_opcion

class AreasGeometricas:
    def ejecutar(self):
        while True:
            print("\n1. cuadrado  2. rectangulo  3. triangulo  4. circulo  5. salir")
            op = leer_opcion("Opción: ", {"1", "2", "3", "4", "5"})
            if op == "5":
                break
            if op == "1":
                lado = leer_decimal("lado: ", minimo=0)
                area = lado ** 2
            elif op == "2":
                base = leer_decimal("base: ", minimo=0)
                altura = leer_decimal("altura: ", minimo=0)
                area = base * altura
            elif op == "3":
                base = leer_decimal("base: ", minimo=0)
                altura = leer_decimal("altura: ", minimo=0)
                area = base * altura / 2
            else:
                radio = leer_decimal("radio: ", minimo=0)
                area = math.pi * radio ** 2
            print(f"area: {area:.2f}")


if __name__ == "__main__":
    AreasGeometricas().ejecutar()
