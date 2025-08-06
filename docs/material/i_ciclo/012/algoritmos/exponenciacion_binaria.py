"""
Exponenciación binaria
"""

# Se toma la potencia como a^b
def potencia(a, b):
    if b == 0:
        return 1

    s = potencia(a, b // 2)

    # Si b es par
    if b % 2 == 0:
        return s * s
    # Si b es impar
    else:
        return s * s * a

def potencia_recursiva(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia_recursiva(a, b-1)
