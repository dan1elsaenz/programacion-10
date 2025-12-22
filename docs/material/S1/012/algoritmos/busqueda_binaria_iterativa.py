"""
Búsqueda binaria

Algoritmo que me permite buscar un número en una lista
Ese número puede estar o no

La lista debe estar ordenada
"""

def busqueda_binaria(arr, objetivo):
    # Definir límites iniciales de búsqueda
    izq = 0
    der = len(arr) - 1

    while izq <= der:
        # Calcular la posición media
        medio = (izq + der) // 2

        # Consultar el valor medio
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
