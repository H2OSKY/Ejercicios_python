#Crear archivo.log

with open("archivo.log", "w") as archivo:
    archivo.write("Registro de Actividad\n")
    archivo.write("----------------------------\n")
    archivo.write("1. Acción exitosa\n")
    archivo.write("2. Advertencia: este es un mensaje de advertencia\n")
    archivo.write("3. Error crítico: se produjo un error en el sistema\n")
    archivo.write("4. Otra acción exitosa\n")
    archivo.write("5. Error menor: se encontró un problema\n")
    archivo.write("6. Acción exitosa\n")
    archivo.write("7. Información: esto es solo una información\n")

print("Archivo de log generado exitosamente (archivo.log).")
