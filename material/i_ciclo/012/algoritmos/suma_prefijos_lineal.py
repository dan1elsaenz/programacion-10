"""
Suma de prefijos

Almacenar en la lista `prefijos` la suma de los elementos
de la lista hasta ese punto
"""

numeros = [1, 2, 3,-4, 5, 10,-11]

# Lista de ceros con el largo de la lista original
prefijos = [0] * len(numeros)
#          [1, 3, 6, 2, 7, 17, 6]

prefijos[0] = numeros[0]

for i in range(1, len(numeros)):
    prefijos[i] = prefijos[i-1] + numeros[i]

def suma_entre_indices(i1, i2):
    return prefijos[i2] - prefijos[i1-1]

print(suma_entre_indices(3, 5))
