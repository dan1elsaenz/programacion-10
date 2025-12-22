# Swaps entre número spara ordenar
# Complejidad temporal: O(n^2)

# lista a ordenar
l = [4,5,6,1,3,2,9,8,20,11]

def bubble_sort1(lista):
    n = len(lista)

    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(1,n):
            if lista[i-1] > lista[i]:
                lista[i-1], lista[i] = lista[i], lista[i-1]
                intercambio = True

def bubble_sort2(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

