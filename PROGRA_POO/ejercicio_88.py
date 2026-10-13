from utilidades import leer_entero, leer_decimal

class PromedioNumeros:
    def ejecutar(self):
        cantidad = leer_entero("cantidad de numeros: ", minimo=1)
        suma = 0
        for i in range(cantidad):
            suma += leer_decimal(f"numero {i + 1}: ")
        print(f"suma: {suma:g} , Promedio: {suma / cantidad:g}")


if __name__ == "__main__":
    PromedioNumeros().ejecutar()
