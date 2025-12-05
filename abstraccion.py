# ejemplo de abstraccion

from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

# Clase concreta
class Coche(Vehiculo):
    def encender(self):
        return "El coche está encendido"

class Moto(Vehiculo):
    def encender(self):
        return "La moto está encendida"

# Uso
coche = Coche()
moto = Moto()
print(coche.encender())  # El coche está encendido
print(moto.encender())   # La moto está encendida
