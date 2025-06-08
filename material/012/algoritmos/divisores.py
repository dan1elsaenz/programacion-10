"""
Cálculo de divisores de un número
"""


from math import sqrt

def divisores(n):
    resultado = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            resultado.add(i)
            resultado.add(n // i)

    return sorted(resultado)

print(divisores(100))

