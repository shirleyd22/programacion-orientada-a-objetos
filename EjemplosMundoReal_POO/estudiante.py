#caso del mundo real: estudiante
#este codigo presenta a un estudiante con sus caracteristicas y acciones

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        #con este metodo se muestra la informacion del estudiante
        print(f"hola, mi nombre es {self.nombre} y tengo {self.edad} años")
#se pide al usuario que ingrese sus datos
nombre= input("¿como te llamas?\n")
edad= int(input("¿cuantos años tienes?\n"))
#ahora se crea un objeto de la clase estudiante con los datos ingresados
est1=Estudiante(nombre,edad)
#por ultimo se llama al metodo del objeto para que el estudiante se presente
est1.presentarse()