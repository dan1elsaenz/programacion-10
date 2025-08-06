"""
Ejercicio 11: Contar letras en una lista de palabras

Dada una lista de palabras, imprime una nueva lista con la cantidad de letras que tiene cada palabra.

```
Entrada: ["hola", "elefante", "sol"]
Salida: [4, 8, 3]
```
"""

lista = ["hola", "elefante", "sol"]
longitudes = []

for palabra in lista:
    largo = len(palabra)
    longitudes.append(largo)

print(longitudes)

