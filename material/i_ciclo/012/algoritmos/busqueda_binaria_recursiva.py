"""
Búsqueda binaria recursiva
"""

def busqueda_binaria(arr, objetivo, izq, der):
    # Condición
    if izq > der:
        return -1

    # Cálculo del valor medio
    medio = (izq + der) // 2

    if arr[medio] == objetivo:
        return medio

    elif arr[medio] < objetivo:
        return busqueda_binaria(arr, objetivo, medio + 1, der)

    else:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)

lista = [1,2,3,4,5,5,6,7,8, 10]

busqueda_binaria(lista, 9, 0, len(lista)-1)
