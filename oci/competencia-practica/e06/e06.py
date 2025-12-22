"""
Ejercicio F. Ordenando las letras de la línea
"""

import sys

sys.setrecursionlimit(101010)


def print(*objects, sep=" ", end="\n"):
    text = sep.join(map(str, objects))
    sys.stdout.write(f"{text}{end}")


def input():
    return sys.stdin.readline().rstrip("\r\n")


# Inicio de la solución

linea = input()

# Lista de letras
letras = list()

# Guardar únicamente letras (excluir caracteres no alfabéticos)
for c in linea:
    if c.isalpha():
        letras.append(c)

# Ordenar
letras.sort()

# Reconstruir la línea
resultado = ""
indice_letra = 0

for c in linea:
    if c.isalpha():
        resultado += letras[indice_letra]
        indice_letra += 1
    else:
        resultado += c

# Imprimir resultado final
print(resultado)
