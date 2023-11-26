#Calculadora de IMC: Crea un programa que 
# calcule el Índice de Masa Corporal (IMC) 
# a partir del peso (en kilogramos) y la altura 
# (en metros) ingresados por el usuario.

peso = float(input("Ingrese su peso en Kg "))
altura = float(input("Ingrese su altura en metros "))

imc =  peso/(altura * altura)

print(f"Su IMC es de: {imc}")