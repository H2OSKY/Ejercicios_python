#Diccionario de Sinónimos: 
# Implementa un pequeño diccionario de sinónimos, 
# donde el usuario puede ingresar una palabra y 
# obtener sinónimos de esa palabra.

diccionario_sin = [
    ['abundante', 'mucho'],
    ['acabar', 'terminar'],
    ['advertir', 'notar'],
]

palabra = input("Ingrese una palabra: ")

for conjunto_palabra in diccionario_sin:
    if palabra in conjunto_palabra:
        conjunto_palabra.remove(palabra)
        print("Está en la lista ", conjunto_palabra)



