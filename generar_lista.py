import random

def lista_aleatoria(N=20,a=0,b=100):
    la_lista = []
    for _ in range(N):
        elemento_aleatorio = random.randint(a, b)
        la_lista.append(elemento_aleatorio)
    return la_lista

print(lista_aleatoria())