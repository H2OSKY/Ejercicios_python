# Analizador de Log: 
# Desarrolla un script que lea un 
# archivo de registro (log) 
# y encuentre e informe sobre 
# ciertos patrones de error.

def analizar_log(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                if 'error' in linea.lower():
                    print(f'Error encontrado en la línea {numero_linea}: {linea.strip()}')
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
    except Exception as e:
        print(f"Error: {e}")

# Nombre del archivo de log
nombre_archivo_log = "archivo.log"

# Llamada a la función para analizar el log
analizar_log(nombre_archivo_log)
