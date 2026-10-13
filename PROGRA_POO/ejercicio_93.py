from utilidades import leer_decimal, leer_opcion

class NotasEstudiantes:
    def ejecutar(self):
        cantidad = 0
        suma = 0
        mayor = menor = None
        while True:
            nota = leer_decimal("nota (0 a 100): ", minimo=0, maximo=100)
            cantidad += 1
            suma += nota
            if mayor is None or nota > mayor:
                mayor = nota
            if menor is None or nota < menor:
                menor = nota
            if leer_opcion("¿registrar otra nota? (si/no): ", {"si", "no"}) == "no":
                break
        print(f"notas: {cantidad} , promedio: {suma / cantidad:.2f} , mayor: {mayor:g} , menor: {menor:g}")


if __name__ == "__main__":
    NotasEstudiantes().ejecutar()
