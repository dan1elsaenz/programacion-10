"""
Ejercicio C. Rango simple
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

numeros = [int(x) for x in input().split()]

inf, sup = map(int, input().split())

# Algoritmo
contador = 0

for n in numeros:
    if n >= inf and n <= sup:
        contador += 1

# Imprimir resultados
print(contador)
