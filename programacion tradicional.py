#prorama para calcular el promedio semanal del cluma usando programacion tradicional
#esta funcion pide las temperaturas cada dia y las guarda en una lista

def pedir_temperaturas():
    temperaturas = []
    print ("por favor ingrese la temperatura de cada dia: ")
    for i in range(7):
        temp= float(input(f"dia { i+1}: "))
        temperaturas.append(temp)
    return temperaturas

#en esta funcion calcularemos el promedio semanal

def promedio_semanal(lista):
    suma = 0
    for temp in lista:
        suma += temp
        promedio = suma / len(lista)
    return promedio


#funcion principal donde se coordina
def main():
    temps= pedir_temperaturas()
    prom = promedio_semanal(temps)
    print(f"\n el promedio semanal del clima es: {prom:.2f} grados celsius")

main()
