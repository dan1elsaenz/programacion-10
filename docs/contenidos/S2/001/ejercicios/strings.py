"""
Escribir un programa que reciba una frase, elimine los signos de puntuación,
pase todo a minúsculas y cuente cuántas veces aparece cada palabra.
"""

frase = input()
frase_modificada = ""

for c in frase:
    if c.isalpha() or c.isspace():
        frase_modificada += c

lista = frase_modificada.lower().split()
diccionario = {}

for palabra in lista:
    diccionario[palabra] = diccionario.get(palabra, 0) + 1

for palabra, cantidad in diccionario.items():
    print(f"{palabra} -> {cantidad}")
