"""
La suma de prefijos es un algoritmo para hallar la suma desde un indice hasta
otro dentro de una lista (mas eficiente que recorrer cada indice)
"""

# Arreglo inicial
numeros = [23, 14, 12, 21, 45, 32]

"""
Opcion de recorrer el arreglo
"""
# inicio, fin = map(int, input().split())
#
# if inicio > 0 and fin < len(numeros):
#     suma = 0
#     for i in range(inicio, fin+1):
#         suma += numeros[i]
#
#     print(suma)

"""
Suma de prefijos
"""

# Lista con la suma acumulativa hasta cierto numero
prefijos = [0 for _ in range(len(numeros))]

prefijos[0] = numeros[0]

for i in range(1, len(numeros)):
    prefijos[i] = prefijos[i-1] + numeros[i]

print(numeros)
print(prefijos)

# Probar
consultas = 3

for _ in range(consultas):
    inicio, fin = map(int, input().split())
    resultado = prefijos[fin]

    if inicio > 0:
        resultado -= prefijos[inicio-1]
    print(resultado)

