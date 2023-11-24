#Contador de Vocales: 
# Desarrolla un programa que cuente la cantidad 
# de vocales en una frase proporcionada por el usuario.

frase = str(input("Ingrese una frase: "))

vocales = "aeiouAEIOU"
contador_vocales = 0

for caracter in frase:
    if caracter in vocales:
        contador_vocales += 1

print(f"La frase tiene {contador_vocales} vocales")

