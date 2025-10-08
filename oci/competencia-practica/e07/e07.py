"""
Ejercicio G. Recolectando café
"""

import sys

sys.setrecursionlimit(101010)


def print(*objects, sep=" ", end="\n"):
    text = sep.join(map(str, objects))
    sys.stdout.write(f"{text}{end}")


def input():
    return sys.stdin.readline().rstrip("\r\n")


# Inicio de la solución

# Lectura
cantidad = int(input())
arbustos = [int(x) for x in input().split()]

# Crear una lista para conocer la posición de cada arbusto
posicion = [0] * (cantidad + 1)  # índices de 1 a N

for idx, arbusto in enumerate(arbustos):
    posicion[arbusto] = idx

# Calcular el costo total
costo = 0

for i in range(1, cantidad):
    distancia = abs(posicion[i + 1] - posicion[i])
    costo += i * distancia

print(costo)
