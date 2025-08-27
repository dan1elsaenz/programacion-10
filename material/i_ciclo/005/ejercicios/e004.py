"""
Ejercicio 4: Contar palabras que contienen una letra específica  

Dada una lista de palabras y una letra, cuenta cuántas palabras contienen esa letra.

```
Entrada: ["casa", "carro", "perro", "gato"], "r"  
Salida: 2
```
"""

# Declarar la lista de la palabras
lista = ["casa", "carro", "perro", "gato"]

# Declarar palabra a buscar
letra = "r"

# Declarar variable contador
contador = 0

for palabra in lista:
    if letra in palabra:
        contador += 1

print(contador)

