from utilidades import leer_decimal

class EstadisticasNotas:
    def __init__(self, nota_minima=51):
        self.nota_minima = nota_minima

    def ejecutar(self):
        aprobados = reprobados = 0
        suma = 0
        mayor = menor = None
        for i in range(10):
            nota = leer_decimal(f"nota {i + 1} (0 a 100): ", minimo=0, maximo=100)
            suma += nota
            mayor = nota if mayor is None or nota > mayor else mayor
            menor = nota if menor is None or nota < menor else menor
            if nota >= self.nota_minima:
                aprobados += 1
            else:
                reprobados += 1
        print(f"aprobados: {aprobados} , reprobados: {reprobados}")
        print(f"promedio: {suma / 10:.2f} , mayor: {mayor:g} , menor: {menor:g}")
        print(f"porcentaje de aprobacion: {aprobados * 10}%")


if __name__ == "__main__":
    EstadisticasNotas().ejecutar()
