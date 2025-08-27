"""
Ejercicio E. Encuentra el tesoro
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
matriz = [[int(x) for x in input().split()] for _ in range(3)]

# Verificar que las diagonales son iguales
if matriz[0][0] == matriz[0][2] == matriz[1][1] == matriz[2][0] == matriz[2][2]:
    print("Tesoro encontrado")
else:
    print("Sigue buscando")
