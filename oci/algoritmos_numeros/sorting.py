"""
Tipos de sorting en un arreglo de datos dado
"""

l = [4,5,6,1,3,2,9,8,20,11]

# ---------------------- Bubble sort ----------------------
# O(n^2)
# Swaps para ordenar
def bubble_sort(lista):
    # Largo de la lista
    n = len(lista)

    # Booleano que se pone en False cuando el arreglo está ordenado
    intercambio = True
    while intercambio:
        # Colocar `intercambio` en False: Está ordenado
        intercambio = False

        # Recorrer el arreglo
        for i in range(1,n):
            if lista[i-1] > lista[i]:
                lista[i-1], lista[i] = lista[i], lista[i-1]
                intercambio = True
# bubble_sort(l)
# print(l)

def ordenamiento_burbuja(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]


# ---------------------- Selection sort ----------------------
# O(n^2)
# Busca el minimo, lo coloca al inicio y así sucesivamente para cada indice
def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        min_indice = i

        for j in range(i+1, n):
            if lista[j] < lista[min_indice]:
                min_indice = j

        lista[i], lista[min_indice] = lista[min_indice], lista[i]

# selection_sort(l)
# print(l)

# ---------------------- Insertion sort ----------------------
# O(n^2)
# Cuenta los mayores y se mueve esos espacios hacia la izquierda la presente casilla
def insertion_sort(lista):
    n = len(lista)

    for i in range(0, n):
        mayores = 0
        for j in range(0, i):
            if lista[j] > lista[i]:
                mayores += 1
        num = lista[i]

        for j in range(i, i-mayores, -1):
            lista[j] = lista[j-1]
        lista[i-mayores] = num

# insertion_sort(l)
# print(l)

# ---------------------- Merge sort ----------------------
# O( nlog(n) )
# Ordena recursivamente subarreglos
# Mas rapido que los demas

def mezclar_arreglos(l1, l2):
    resultado = []

    l1.append(float('inf'))
    l2.append(float('inf'))

    l1.reverse()
    l2.reverse()

    while len(l1) > 1 or len(l2) > 1:
        if l1[-1] < l2[-1]:
            resultado.append(l1[-1])
            l1.pop()
        else:
            resultado.append(l2[-1])
            l2.pop()
    return resultado

def merge_sort(lista):
    n = len(lista)

    if n == 0 or n == 1:
        return lista
    elif n == 2:
        return [min(lista), max(lista)]

    mitad = n // 2

    l1 = merge_sort(lista[:mitad])
    l2 = merge_sort(lista[mitad:])
    return mezclar_arreglos(l1, l2)

print(merge_sort(l))

