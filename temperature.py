# een este programa voy a convertir una temperatura de grados Celsius a Fahrenheit.
# Utiliza diferentes tipos de datos y sigue las convenciones de nomenclatura en Python.

# Se solicita al usuario que ingrese su nombre
user_name = input("por favor ingrese su nombre y su apellido: ")

# Se solicita al usuario que ingrese la temperatura en grados Celsius como un tipo de datos float
celsius_temperature = float(input("por favor ingrese la temperatura en grados Celsius: "))

# Se realiza la conversión de Celsius a Fahrenheit
fahrenheit_temperature = (celsius_temperature * 9 / 5) + 32

# Variable booleana que indica si la conversión fue exitosa
conversion_successful = True

# Se muestran los resultados en pantalla
print("Hola,", user_name)
print("La temperatura en grados Fahrenheit es:", fahrenheit_temperature)
print("¿La conversión fue exitosa?", conversion_successful)
