"""
Dada una lista de enteros, queremos:

1. Filtrar los que sean **mayores que cero**.
2. Determinar cuáles son **cuadrados perfectos** (por ejemplo, 1, 4, 9, 16...).
3. Calcular la suma de esos cuadrados perfectos.

Ejemplo de entrada:
```python
numeros = [0, 1, 2, 3, 4, 5, 9, 10, 16, 20, 25]
```

Resultado esperado:
```
[1, 4, 9, 16, 25]
Suma: 55
```

Recuerde que un número es cuadrado perfecto si la raíz cuadrada entera al cuadrado
es igual al número.
    ```python
    import math
    math.isqrt(n)**2 == n
    ```
"""

import math

# Lista inicial
numeros = [0, 1, 2, 3, 4, 5, 9, 10, 16, 20, 25]

# Filtrar los positivos
lista_filtrada = [n for n in numeros if n > 0 and math.isqrt(n) ** 2 == n]
# lista_filtrada = list(filter(lambda n: n > 0 and math.isqrt(n) ** 2 == n, numeros))

total = sum(lista_filtrada)

print(lista_filtrada)
print(f"Suma: {total}")
