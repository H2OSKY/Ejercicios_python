#Adivina el Número: 
# Escribe un programa que genere un número aleatorio 
# y pida al usuario que lo adivine. Si el usuario 
# no acierta, indica si su número es demasiado alto 
# o demasiado bajo.

import random

intentos = int(input("Ingrese el número de intentos que desea "))
numeroAleatorio = random.randint(1, 100)

contador = 0

while contador < intentos:
    numero = int(input("Adivina el número (entre 1 y 100): "))
    
    contador += 1

    if numero > numeroAleatorio:
        print (" Este es el intento: ", contador)
        print("El número ingresado es mayor. \n")
    elif numero < numeroAleatorio:
        print(" Este es el intento: ", contador)
        print("El número ingresado es menor. \n")
    else:
        print(f"Felicidades, ¡adivinaste el número {numeroAleatorio}! en el intento {contador}")
        break

if contador == intentos:
    print (f"El número secreto era: {numeroAleatorio}")