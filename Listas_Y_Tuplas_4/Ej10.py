#Mayores y Menores: 
# Dada una lista de números, encuentra el 
# número más grande y el más pequeño en la lista.

def encontrar_mayor_menor(lista):
    if not lista:
        return None, None 

    mayor = menor = lista[0]

    for numero in lista:
        if numero > mayor:
            mayor = numero
        elif numero < menor:
            menor = numero

    return mayor, menor

numeros = [12, 5, 8, 23, 7, 15, -1]

mayor, menor = encontrar_mayor_menor(numeros)

if mayor is not None and menor is not None:
    print(f"El número más grande es: {mayor}")
    print(f"El número más pequeño es: {menor}")
else:
    print("La lista está vacía.")
