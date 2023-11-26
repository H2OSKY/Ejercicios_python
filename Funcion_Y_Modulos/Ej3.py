
# Función Recursiva de Fibonacci: 
# Implementa una función recursiva 
# que calcule el n-ésimo número de Fibonacci.

def fibonacci_recursivo(n):
    if n <= 0:
        return "Ingrese un número entero positivo"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Ejemplo de uso
n = int(input("Ingrese el valor de n para calcular el n-ésimo número de Fibonacci: "))

resultado = fibonacci_recursivo(n)

print(f"El {n}-ésimo número de Fibonacci es: {resultado}")
