"""
Filtrado de elementos únicos por posición

Implemente una función que reciba una lista y retorne otra lista con los elementos que sólo aparecen una vez y están en una posición par (índice par).

**Ejemplo:**
```python
Entrada: [1, 2, 3, 2, 4, 1, 5]
Salida: [3, 4, 5]
```
"""

def filtrar_posicion(lista):
    lista_salida = []

    for i in range(0, len(lista), 2):
        valor_actual = lista[i]

        if lista.count(valor_actual) == 1:
            # Sí se agrega porque es único
            lista_salida.append(valor_actual)

    return lista_salida


print(filtrar_posicion([1, 2, 3, 2, 4, 1, 5]))
