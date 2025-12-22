"""
Ejercicio I. Inecuación de altura
"""

import sys

sys.setrecursionlimit(101010)


def print(*objects, sep=" ", end="\n"):
    text = sep.join(map(str, objects))
    sys.stdout.write(f"{text}{end}")


def input():
    return sys.stdin.readline().rstrip("\r\n")


# Inicio de la solución

# Lectura de cantidad de preguntas
Q = int(input())

for _ in range(Q):
    a, b, c, p = map(int, input().split())
    objetivo = p * p  # p^2

    izquierda = 0
    derecha = 10**16

    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        valor = a * medio + b * medio * medio + c * medio * medio * medio

        if valor >= objetivo:
            derecha = medio
        else:
            izquierda = medio + 1

    print(izquierda)

# for _ in range(Q):
#     a, b, c, p = map(int, input().split())
#     objetivo = p * p  # p^2
#
#     for i in range(10**16):
#         valor = a * i + b * i * i + c * i * i * i
#
#         if valor > objetivo:
#             print(i)
#             break
