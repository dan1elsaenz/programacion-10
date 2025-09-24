"""
Busqueda binaria:

Algoritmo que sirve para encontrar el indice de un numero entero objetivo dentro
de una lista ORDENADA
"""

# Implementacion con while loop

def busqueda_binaria_iterativa(arreglo, objetivo):
    izquierdo, derecho = 0, len(arreglo) - 1

    while izquierdo <= derecho:
        medio = (izquierdo + derecho) // 2

        if arreglo[medio] == objetivo:
            return medio
        elif arreglo[medio] < objetivo:
            izquierdo = medio + 1
        else:
            derecho = medio - 1
    return -1

# Ejemplo de uso
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 7
resultado = busqueda_binaria_iterativa(arreglo, objetivo)
print(resultado)

# Implementacion recursiva
def busqueda_binaria_recursiva(arreglo, objetivo, izquierdo, derecho):
    if izquierdo > derecho:
        return -1
    medio = (izquierdo + derecho) // 2
    if arreglo[medio] == objetivo:
        return medio
    elif arreglo[medio] < objetivo:
        return busqueda_binaria_recursiva(arreglo, objetivo, medio + 1, derecho)
    else:
        return busqueda_binaria_recursiva(arreglo, objetivo, izquierdo, medio - 1)

# Ejemplo de uso
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 7
resultado = busqueda_binaria_recursiva(arreglo, objetivo, 0, len(arreglo) - 1)
print(resultado)
