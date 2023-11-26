# Lector de Poemas: 
# Crea un programa que lea un archivo 
# de texto con un poema y lo muestre en la consola.

nombre_archivo = "poema.txt"

try:
    # Abrir el archivo en modo lectura
    with open(nombre_archivo, "r") as archivo:
        poema = archivo.read()

        print("Poema:")
        print(poema)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
except Exception as e:
    print(f"Error: {e}")
