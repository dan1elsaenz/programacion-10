"""
Ejercicio 2: Filtrar palabras cortas  

Dada una lista de palabras, devuelve una nueva lista que contenga solo aquellas palabras con más de 4 letras.

```
Entrada: ["sol", "estrella", "luz", "universo"]
Salida: ["estrella", "universo"]
```
"""

# Lista inicial
lista = ["sol", "estrella", "luz", "universo"]

# Declaración de nueva lista vacía
nueva_lista = []

# Recorrer lista elemento por elemento
for elemento in lista:
    # Si el largo de mi elemento es mayor que 0, lo agrego a la nueva lista
    if len(elemento) > 4:
        nueva_lista.append(elemento)

print(nueva_lista)




