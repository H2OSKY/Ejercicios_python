# Contador de Palabras: 
# Dada una cadena de texto, cuenta cuántas veces 
# aparece cada palabra y presenta los resultados 
# en un diccionario.

def contar_palabras(cadena):
    # Eliminar signos de puntuación y convertir a minúsculas
    cadena = cadena.lower().replace(",", "").replace(".", "")
    
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Crear un diccionario para contar las palabras
    contador_palabras = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1

    return contador_palabras

# Obtener la cadena de texto del usuario
texto_usuario = input("Ingrese una cadena de texto: ")

# Calcular y mostrar el diccionario de frecuencias
resultado = contar_palabras(texto_usuario)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")
