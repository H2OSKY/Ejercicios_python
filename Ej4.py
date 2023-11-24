#Adivina el Número: 
# Escribe un programa que genere un número aleatorio 
# y pida al usuario que lo adivine. Si el usuario 
# no acierta, indica si su número es demasiado alto 
# o demasiado bajo.

import random

numeroAleatorio = random.randint(1, 100)

while True:
    numero = int(input("Adivina el número (entre 1 y 100): "))
    
    if numero > numeroAleatorio:
        print("El número ingresado es mayor.")
    elif numero < numeroAleatorio:
        print("El número ingresado es menor.")
    else:
        print(f"Felicidades, ¡adivinaste el número {numeroAleatorio}!")
        break
