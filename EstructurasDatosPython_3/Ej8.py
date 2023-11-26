#Eliminación de Duplicados: 
# Escribe un programa que tome una lista de 
# números ingresada por el usuario y elimine 
# todos los números duplicados.

lista_numeros = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada del usuario a una lista de números
numeros = [int(x) for x in lista_numeros.split()]

# Eliminar duplicados utilizando un conjunto (set)
lista_sin_duplicados = list(set(numeros))

# Mostrar la lista original y la lista sin duplicados
print("\nLista original:", numeros)
print("Lista sin duplicados:", lista_sin_duplicados)
