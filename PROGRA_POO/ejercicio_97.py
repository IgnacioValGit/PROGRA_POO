from utilidades import leer_decimal, leer_opcion

class CuentaBancaria:
    def __init__(self):
        self.saldo = 0.0

    def depositar(self, monto):
        self.saldo += monto
        print(f"Deposito realizado con exito. Saldo: Bs {self.saldo:.2f}")

    def retirar(self, monto):
        if monto > self.saldo:
            print("SIN FONDOS.")
        else:
            self.saldo -= monto
            print(f"retiro realizado. Saldo: Bs {self.saldo:.2f}")

    def ejecutar(self):
        while True:
            print("\n1. consultar saldo  2. depositar  3. retirar  4. salir")
            op = leer_opcion("opcion: ", {"1", "2", "3", "4"})
            if op == "4":
                break
            elif op == "1":
                print(f"Saldo: Bs {self.saldo:.2f}")
            elif op == "2":
                self.depositar(leer_decimal("monto para depositar: ", minimo=0.01))
            elif op == "3":
                self.retirar(leer_decimal("monto para retirar: ", minimo=0.01))


if __name__ == "__main__":
    CuentaBancaria().ejecutar()
