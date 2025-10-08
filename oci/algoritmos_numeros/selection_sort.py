# Busca el minimo, lo coloca al inicio y así sucesivamente para cada indice
# Complejidad temporal: O(n^2)

# Arreglo a ordenar
l = [4,5,6,1,3,2,9,8,20,11]

def selection_sort(lista):
    n = len(lista)

    for i in range(0, n):
        min_indice = i

        for j in range(i+1, n):
            if lista[j] < lista[min_indice]:
                min_indice = j

        lista[i], lista[min_indice] = lista[min_indice], lista[i]

