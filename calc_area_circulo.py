
import math

# Paso 1 : Solicitar al usuario que ingrese el radio del circulo

radio=float(input("Ingrese el radio del circulo a calcular: "))

#Paso 2:Definir y asignar a la variable area el resultado de PI*radio²

area= math.pi*(radio**2)

#Paso 3: Mostrar mensaje: "El área del círculo con radio ", radio , "es: ", area
print("El área del círculo con radio ", radio , "es: ", area)

