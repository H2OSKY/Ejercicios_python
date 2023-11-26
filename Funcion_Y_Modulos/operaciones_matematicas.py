# Módulo de Operaciones Matemáticas: 
# Crea un módulo propio que incluya 
# funciones básicas como suma, resta, 
# multiplicación y división.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
