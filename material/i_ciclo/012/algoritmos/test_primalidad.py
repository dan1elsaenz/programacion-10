"""
Test de primalidad O(√n)

Sirve para verificar si un número es primo o no, de una forma eficiente
"""


def test_primalidad(numero):

    # Definir el divisor más pequeño (2)
    x = 2

    # Booleano de cumplimiento del test
    esPrimo = True

    while x * x <= numero:
        if numero % x == 0:
            esPrimo = False
            break
        x += 1

    return esPrimo

print(test_primalidad(25))

