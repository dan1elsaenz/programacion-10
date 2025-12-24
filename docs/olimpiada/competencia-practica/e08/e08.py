"""
Ejercicio H. Minimizando costos de mantenimiento
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

bombillas = list()

for _ in range(cantidad):
    p, c = map(int, input().split())

    bombillas.append((p, c))

m = int(input())
a = int(input())

# Variable para el costo total
costo = 0

# Ordenar bombillas por calidad
bombillas.sort(key=lambda x: (x[1], -x[0]))

for p, c in bombillas[-a:]:
    costo += p

# Quitar las bombillas que ya se compraron
bombillas = bombillas[:-a]

# Ordenar bombillas por precio
bombillas.sort(key=lambda x: x[0])

for p, c in bombillas[: m - a]:
    costo += p

print(costo)
