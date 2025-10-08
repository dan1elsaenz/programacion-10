"""
Implementación de algoritmos de suma máxima de un subarreglo
"""

# Complejidad O(n^3)
def on3(arreglo):
    suma_maxima = 0
    n = len(arreglo)

    # Recorrer el arreglo: Establecer el inicio
    for i in range(n):
        # Establecer final
        for j in range(i, n):
            suma = 0

            # Recorrer entre inicio y final
            for k in range(i, j):
                suma += arreglo[k]

            suma_maxima = max(suma, suma_maxima)

    return suma_maxima


# Complejidad O(n^2)
def on2(arreglo):
    suma_maxima = 0
    n = len(arreglo)

    # Establecer el inicio
    for i in range(n):
        suma = 0

        # Ir añadiendo elementos del arreglo progresivamente a la suma
        for j in range(i, n):
            suma += arreglo[j]

            suma_maxima = max(suma, suma_maxima)

    return suma_maxima


# Complejidad O(n): Se usa únicamente un for loop
def on(arreglo):
    suma_maxima = 0
    suma = 0
    n = len(arreglo)

    for i in range(n):
        suma = max(arreglo[i], suma + arreglo[i])
        suma_maxima = max(suma, suma_maxima)

    return suma_maxima


# Ejemplo del libro
lista = [-1, 2, 4, -3, 5, 2, -5, 2]

print(on3(lista))
print(on2(lista))
print(on(lista))

