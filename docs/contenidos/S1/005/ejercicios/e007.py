"""
Ejercicio 7: Eliminar palabras repetidas de una lista

Dada una lista de palabras, devuelve una nueva lista con las palabras sin repetir, conservando el orden original.

```
Entrada: ["manzana", "pera", "manzana", "uva", "pera"]
Salida: ["manzana", "pera", "uva"]
```
"""

# Declarar lista
lista = ["manzana", "pera", "manzana", "uva", "pera"]

# Declarar lista de elementos únicos
elementos_unicos = []

# Recorrer la lista
for palabra in lista:
    # Si la palabra no está en la lista de elementos únicos, se agrega con append() para mantener el orden
    if palabra not in elementos_unicos:
        elementos_unicos.append(palabra)

# Imprimir resultado
print(elementos_unicos)

