class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def caracterize(self):
        print("Vehículo: Auto")
        print("Marca:", self.brand)
        print("Modelo:", self.model)

    def move(self):
        print("drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def caracterize(self):
        print("Vehículo: Barco")
        print("Marca:", self.brand)
        print("Modelo:", self.model)

    def move(self):
        print("sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def caracterize(self):
        print("Vehículo: Avion")
        print("Marca:", self.brand)
        print("Modelo:", self.model)

    def move(self):
        print("fly")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.caracterize()
    x.move()
    print(".")