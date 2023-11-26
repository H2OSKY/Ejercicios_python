# Función de Conversión de Divisas: 
# Escribe una función que convierta una cantidad de 
# dinero de una moneda a otra utilizando tasas de cambio dadas.

def convertir_divisas(cantidad, tasa_cambio):
    """
    Convierte una cantidad de dinero de una moneda a otra utilizando la tasa de cambio proporcionada.

    Parameters:
    cantidad (float): La cantidad de dinero a convertir.
    tasa_cambio (float): La tasa de cambio entre las dos monedas.

    Returns:
    float: La cantidad convertida en la segunda moneda.
    """
    if cantidad < 0 or tasa_cambio <= 0:
        return "Ingrese cantidades y tasas de cambio válidas."

    cantidad_convertida = cantidad * tasa_cambio
    return cantidad_convertida

# Ejemplo de uso
moneda_origen = input("Ingrese la moneda de origen: ")
moneda_destino = input("Ingrese la moneda de destino: ")

try:
    cantidad = float(input("Ingrese la cantidad de dinero a convertir: "))
    tasa_cambio = float(input(f"Ingrese la tasa de cambio de {moneda_origen} a {moneda_destino}: "))

    resultado = convertir_divisas(cantidad, tasa_cambio)

    print(f"{cantidad} {moneda_origen} equivale a {resultado} {moneda_destino}")
except ValueError:
    print("Ingrese cantidades y tasas de cambio válidas.")
