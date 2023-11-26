#Calculadora de Factorial: 
# Crea un programa que calcule el factorial de un número 
# ingresado por el usuario. Utiliza tanto un ciclo for como 
# un ciclo while para realizar el cálculo.
import sys
sys.set_int_max_str_digits(0)

numero = int(input("Ingrese un número: "))

resultado1 = 1

for i in range(1, numero + 1):
    resultado1 *= i

i = 1
resultado2 = 1

while i <= numero:
    resultado2 *= i
    i += 1
    
print(f"Factorial de {numero} (con ciclo for): {resultado1}")
print(f"Factorial de {numero} (con ciclo while): {resultado2}")

