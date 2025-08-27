"""
Buscar un elemento en una lista

Cree una función que reciba una lista y un número, y retorne `True` si el número está en la lista usando el operador `in`.

**Ejemplo:**
```python
Entrada: lista=[1, 3, 5, 7], número=5
Salida: True
```
"""

def buscarNumero(lista, numero):
    if numero in lista:
        return True
    return False

print(buscarNumero([1, 3, 5, 7], 6))

