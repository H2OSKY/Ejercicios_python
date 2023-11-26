#Lista de la Compra: 
# Crea un programa que permita al usuario ingresar 
# una lista de compras, elemento por elemento, y 
# luego imprima la lista completa al final.

lista_compra = []

while True:
    elemento = input("Ingrese un elemento de la lista de compras (o 'fin' para terminar): ")
    
    if elemento.lower() == 'fin':
        break

    lista_compra.append(elemento)

print("\nLista de Compras:")
for item in lista_compra:
    print(item)
