# Inversión de Tupla: 
# Escribe un programa que invierta 
# los elementos de una tupla.

tupla = (1,2,3,4,5,6,7)
tupla_invertida = tuple(reversed(tupla))

print("Tupla normal", tupla)
print("Tupla invertida", tupla_invertida)

print(len(tupla))

i = len(tupla)-1
while i > 0:
    i -= 1
    print(tupla[i])
    