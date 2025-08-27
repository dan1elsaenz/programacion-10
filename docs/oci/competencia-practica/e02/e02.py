"""
Ejercicio B. SumaDosGrandes
"""

import sys

sys.setrecursionlimit(101010)


def print(*objects, sep=" ", end="\n"):
    text = sep.join(map(str, objects))
    sys.stdout.write(f"{text}{end}")


def input():
    return sys.stdin.readline().rstrip("\r\n")


# Inicio de la solución

lista = list()

for _ in range(6):
    lista.append(int(input()))

max1 = lista.pop(lista.index(max(lista)))
max2 = lista.pop(lista.index(max(lista)))

print(max1 + max2)
