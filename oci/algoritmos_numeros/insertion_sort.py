# Cuenta los mayores y se mueve esos espacios hacia la izquierda la presente casilla
# Complejidad temporal O(n^2)

# Arreglo a ordenar


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
