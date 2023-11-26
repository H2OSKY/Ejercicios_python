# Agenda Telefónica: 
# Crea un programa que permita al usuario añadir, 
# eliminar y buscar números de teléfono en un diccionario.

def mostrar_agenda(agenda):
    print("\nAgenda Telefónica:")
    for nombre, numero in agenda.items():
        print(f"{nombre}: {numero}")

def agregar_contacto(agenda, nombre, numero):
    agenda[nombre] = numero
    print(f"\nContacto agregado: {nombre}: {numero}")

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"\nContacto eliminado: {nombre}")
    else:
        print("\nEl contacto no existe en la agenda.")

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        print(f"\nNúmero de {nombre}: {agenda[nombre]}")
    else:
        print("\nEl contacto no existe en la agenda.")

# Agenda inicial
agenda_telefonica = {
    "Hoover": "3166523461",
    "Sara": "89842834977",
    "Brandon": "7427497846"
}

while True:
    print("\nOpciones:")
    print("1. Mostrar Agenda")
    print("2. Agregar Contacto")
    print("3. Eliminar Contacto")
    print("4. Buscar Contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        mostrar_agenda(agenda_telefonica)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto: ")
        numero = input("Ingrese el número de teléfono: ")
        agregar_contacto(agenda_telefonica, nombre, numero)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        eliminar_contacto(agenda_telefonica, nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        buscar_contacto(agenda_telefonica, nombre)
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
