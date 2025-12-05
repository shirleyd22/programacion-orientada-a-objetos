# ejemplo de polimorfismo

class Ave:
    def sonido(self):
        print("Sonido de ave")

class Pato(Ave):
    def sonido(self):
        print("Cuac cuac")

class Gallina(Ave):
    def sonido(self):
        print("Cloc cloc")

# Lista de aves
aves = [Pato(), Gallina()]

for ave in aves:
    ave.sonido()
