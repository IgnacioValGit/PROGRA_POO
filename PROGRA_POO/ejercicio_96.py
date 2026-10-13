from utilidades import leer_decimal, leer_opcion

class RegistroVentas:
    def ejecutar(self):
        total = 0
        cantidad = 0
        while True:
            nombre = input("producto: ").strip()
            if not nombre:
                print("no puede estar vacío.")
                continue
            precio = leer_decimal("Precio (Bs): ", minimo=0)
            unidades = __import__('utilidades').leer_entero("unidades: ", minimo=1)
            subtotal = precio * unidades
            total += subtotal
            cantidad += unidades
            print(f"{nombre}: Bs {subtotal:.2f}")
            if leer_opcion("otro producto? (si/no): ", {"si", "no"}) == "no":
                break
        print(f"unidades vendidas: {cantidad} , total: Bs {total:.2f}")

if __name__ == "__main__":
    RegistroVentas().ejecutar()
