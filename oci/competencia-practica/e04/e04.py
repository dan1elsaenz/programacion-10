"""
Ejercicio D. Máximo repetido
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

# Algoritmo

if not numeros:
    print(0)
else:
    maximo = max(numeros)
    print(numeros.count(maximo))
