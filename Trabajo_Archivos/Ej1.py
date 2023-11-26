# Registro de Usuario: 
# Escribe un programa que permita al 
# usuario ingresar su nombre y edad, 
# y guarda estos datos en un archivo.

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

datos_usuario = f"Nombre: {nombre}, Edad: {edad}\n"

# Guardar los datos en un archivo llamado "registro.txt"
with open("registro.txt", "a") as archivo:
    archivo.write(datos_usuario)

print("Datos guardados exitosamente en el archivo 'registro_usuario.txt'.")
