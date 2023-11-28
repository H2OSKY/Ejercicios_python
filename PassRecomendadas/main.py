import string 
import random


# string module constants
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.whitespace)  # ' \t\n\r\x0b\x0c'
# print(string.punctuation)

def seleccionar_subcadena(cadena, longitud):
    sub_cadena = []
    for _ in range(longitud):
        i = random.randint(0, len(cadena)-1)
        caracter = cadena[i]
        sub_cadena.append(caracter)
    return ''.join(sub_cadena)

def generarContrasena(num_min, num_may, numbers, num_esp):
    cadena_min = seleccionar_subcadena(string.ascii_lowercase, num_min)
    cadena_may = seleccionar_subcadena(string.ascii_uppercase, num_may)
    cadena_num = seleccionar_subcadena(string.digits, numbers)
    cadena_esp = seleccionar_subcadena(string.punctuation, num_esp)
    password = cadena_min + cadena_may + cadena_num + cadena_esp
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


with open("PassRecomendadas/Contrasepassword.txt", "w") as archivo:
    archivo.write(generarContrasena(10, 1, 1, 1))


