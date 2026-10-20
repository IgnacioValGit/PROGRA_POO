class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        pass

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)
        pass

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento;
        # controla el caso de pila vacía
        if not self.items:
            return None
        return self.items.pop()
        pass

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)
        pass

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento;
        # controla el caso de cola vacía
        if not self.items:
            return None
        return self.items.pop(0)
        pass

    # Reto: consultar sin modificar la cola.
    def consultar_frente(self):
        if not self.items:
            return None
        return self.items[0]

# Agrega tus pruebas debajo. Usa los datos asignados en tu versión.

if __name__ == "__main__":
    lista = ListaEnlazada()
    pila = Pila()
    cola = Cola()

    solicitudes = [
        ("NET01", "Sin señal"),
        ("NET02", "Lentitud"),
        ("NET03", "Router"),
    ]

    for codigo, descripcion in solicitudes:
        lista.agregar(codigo, descripcion)
        pila.apilar(codigo)
        cola.encolar(codigo)

    print("LISTA ENLAZADA:")
    lista.mostrar()

    print("\nRETO 36 - CONSULTAR SIN MODIFICAR LA COLA:")
    print("cola antes:", cola.items)
    print("frente:", cola.consultar_frente())
    print("cola despues:", cola.items)
    assert cola.items == ["NET01", "NET02", "NET03"]

    print("\nCOLA - FIFO (primero en entrar, primero en salir):")
    print(cola.desencolar(), cola.desencolar(), cola.desencolar())
    print("cola vacia:", cola.desencolar())
    print("consulta con cola vacia:", cola.consultar_frente())

    print("\nPILA - LIFO (ultimo en entrar, primero en salir):")
    print(pila.desapilar(), pila.desapilar(), pila.desapilar())
    print("Pila vacia:", pila.desapilar())

