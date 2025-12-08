#programa para calcular el promedio semanal del clima
#codigo realizado con programacion orientada a objetos

#se ingresa una clase base apra demostrar herencia

class registroclima:
    def mostrar_titulo (self):
        print ("== registro climatico ==")
#clase principal que hereda la clase anterior
class climasemanal(registroclima):
    def __init__(self):
        self. temperaturas =[]  #atributos donde se guardan los datos de las temperaturas
        # metodo para ingresar las temperaturas
    def ingresar_temperaturas (self):
        print("por favor ingrese las temperaturas de la semana: ")
        for i in range (7):
            temp= float(input(f"dia { i+1}: "))
            self.temperaturas.append(temp)
    #se calcula el promedio
    def promedio(self):
        if len(self.temperaturas) == 0: #la lista está vacia, devuelve 0 para asi evitar errores
           return 0
        suma = 0
        for t in self.temperaturas:
           suma += t
        return suma/len(self.temperaturas)
     #polimorfismo: sobrescritura del metodo del padre
    def mostrar_titulo(self):
        print("== clima semanal==")
#programa principal en POO
clima =climasemanal()
clima.mostrar_titulo()
clima.ingresar_temperaturas()
prom = clima.promedio()
print(f"\n el promedio semanal es: {prom: .2f} grados celsius")