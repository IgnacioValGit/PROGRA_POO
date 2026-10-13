from utilidades import leer_entero

class ClasificadorEdades:
    def clasificar(self, edad):
        if edad <= 11:
            return "niños"
        elif edad <= 17:
            return "adolescentes"
        elif edad <= 59:
            return "adultos"
        else:
            return "adultos mayores"

    def ejecutar(self):
        cantidad = leer_entero("cantidad de edades: ", minimo=1)
        conteo = {"niños": 0, "adolescentes": 0, "adultos": 0, "adultos mayores": 0}
        for i in range(cantidad):
            edad = leer_entero(f"Edad {i + 1}: ", minimo=0)
            conteo[self.clasificar(edad)] += 1
        for grupo, total in conteo.items():
            print(f"{grupo.capitalize()}: {total}")


if __name__ == "__main__":
    ClasificadorEdades().ejecutar()
