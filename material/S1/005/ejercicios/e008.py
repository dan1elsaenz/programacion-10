"""
Ejercicio 8: Determinar si una lista está ordenada

Escribe un programa que reciba una lista de números y determine si está ordenada de menor a mayor.

```
Entrada: [1, 2, 3, 4, 5]
Salida: True

Entrada: [3, 1, 4, 2, 5]
Salida: False
```
"""

# Declaración de la lista
lista = [2,1,3,4,5]

# Variable booleana que va a rastrear si la condición se sigue cumpliendo o no
estaOrdenada = True

# Recorrer la lista
for i in range(len(lista)):
    # El índice actual no es mayor que len(lista)-1
    if i >= len(lista) - 1:
        break # Salir para no generar errores de acceso de índices fuera de la lista

    # Verificar que el elemento actual sea menor que el siguiente
    if lista[i] > lista[i+1]:
        # Cambiar el estado de la variable booleana
        estaOrdenada = False
        break # Salir porque ya se determinó que no está ordenada

# Imprimir resultado
print(estaOrdenada)

