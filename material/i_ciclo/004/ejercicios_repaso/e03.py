"""
Ejercicio 3: Encontrar el número mayor y menor en una lista  

Escribe un programa que reciba una lista de números enteros e imprima el número más grande y el más pequeño.  

```
Entrada: 3 1 7 9 2 8
Salida: (9, 1)
```
"""

lista = [3, 1, 7, 9, 2, 8]

# Buscar el número más grande y el más pequeño
menor = min(lista)
mayor = max(lista)

# Imprimir los resultados
print((mayor, menor))

