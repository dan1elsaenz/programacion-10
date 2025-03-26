"""
Ejercicio 9: Concatenar todas las palabras de una lista

Dada una lista de palabras, devuelve un solo string donde todas las palabras estén separadas por un espacio (sin utilizar el método `join()`)

```
Entrada: ["Hola", "mundo", "esto", "es", "Python"]
Salida: "Hola mundo esto es Python"
```
"""

# Declaración de lista
lista = ["Hola", "mundo", "esto", "es", "Python"]

string = ""

# Método 1: Iterador
for palabra in lista:
    # Concatenar al string la palabra y un espacio al final
    string += palabra + " "


# Método 2: Índice
for i in range(len(lista)):
    # Concatenar al string la palabra y un espacio al final
    string += lista[i] + " "

# Imprimir el string sin espacios alrededor (para quitar el último espacio agregado de la concatenación)
print(string.strip())

