"""
Contar cuántas veces aparece un número en una lista

Escriba una función recursiva que cuente cuántas veces aparece un número específico dentro de una lista.

```
Entrada: lista=[1, 2, 3, 2, 2, 5], num=2
Salida: 3
```
"""

# Implementación con loops
def contador_for(lista, n):
    contador = 0

    for i in range(len(lista)):
        if lista[i] == n:
            contador += 1

    return contador

# Implementación con recursión
def contador_recursion(lista, n):
    # Caso base
    if not lista:
        return 0

    coincide = 0

    # Verificar si el número extraído coincide o no
    if lista[0] == n:
        coincide = 1

    # Recursión
    return coincide + contador_recursion(lista[1:], n)

# Entradas
lista = [1, 2, 3, 2, 2, 5]
num = 2

print(contador_for(lista, num))
print(contador_recursion(lista, num))

