"""
Ejercicio 13: Contar cuántas veces aparece una letra en cada palabra

Dada una lista de palabras y una letra, crea una nueva lista con la cantidad de veces que esa letra aparece en cada palabra.

```
Entrada: ["banana", "manzana", "pera"], "a"
Salida: [3, 3, 1]
```
"""

# Lista a analizar
lista = ["banana", "manzana", "pera"]

# Letra
letra = "a"

# Lista de contadores
contadores = []

# Recorrer la lista
for palabra in lista:
    # Acá palabra es un string de la lista
    contador = 0 # Declarar contador fuera del for interior porque interesa que su valor se mantenga respecto a las iteraciones del interior

    # Iterar sobre los caracteres de la palabra y contar
    for caracter in palabra:
        if caracter == letra:
            contador += 1

    # Guardar contador en lista de contadores
    contadores.append(contador)

print(contadores)

