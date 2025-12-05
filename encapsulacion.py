# ejemplo de encapsulacion

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota  # privado

    def obtener_nota(self):
        return self.__nota

    def actualizar_nota(self, nueva_nota):
        if 0 <= nueva_nota <= 100:
            self.__nota = nueva_nota
        else:
            print("Nota inválida")

# Uso
alumno = Estudiante("Ana", 85)
print(alumno.obtener_nota())  # 85
alumno.actualizar_nota(90)
print(alumno.obtener_nota())  # 90
