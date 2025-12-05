# ejemplo de herencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def info(self):
        super().info()
        print(f"Puertas: {self.puertas}")

# Uso
coche = Coche("Toyota", "Corolla", 4)
coche.info()
