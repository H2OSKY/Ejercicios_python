def maxmin(la_lista = [40, 20, 10, 30]):
    minimo = la_lista[0]
    maximo = la_lista[0]
    for num in la_lista:
        if maximo < num:
            maximo = num
        
        if minimo > num:
            minimo = num
    return maximo, minimo

print(maxmin())