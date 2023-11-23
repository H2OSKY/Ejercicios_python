#Conversor de Temperatura: 
# Escribe un programa que convierta 
# la temperatura de grados Celsius a Fahrenheit y viceversa. 
# El usuario debe poder ingresar una temperatura y especificar 
# a qué unidad desea convertirla.

temperatura = float(input("Ingrese el valor de la temperatura "))
unidad = str(input("Ingrese la unidad de temperatura a convertir: C o F "))

if unidad == 'C' or unidad == 'c':
    temperatura = ( temperatura * 1.8 ) +32
elif unidad == 'F' or unidad == 'f':
    temperatura = ( temperatura - 32 ) / 1.8

else : print("Unidad no valida")

print(temperatura)