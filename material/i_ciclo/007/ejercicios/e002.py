"""
Solicita al usuario una lista de palabras (separadas por coma). Luego:

Crea una lista con palabras que empiezan con vocal
Otra con palabras que empiezan con consonante
Muestra la cantidad de palabras en cada categoría y sus listas respectivas
"""

# Solicitar la lista de palabras y separarlas por coma
lista_palabras = input("Ingrese una lista de palabras separadas por coma: ").split(",")

# Quitar espacios iniciales de las palabras
for i in range(len(lista_palabras)):
    lista_palabras[i] = lista_palabras[i].strip()

# Definir una lista que almacena las palabras que inician con vocal y consonante
lista_vocales = []
lista_consonantes = []

# Recorrer la lista de palabras y clasificar por su letra inicial en vocales y consonantes
for palabra in lista_palabras:
    if palabra[0] in "aeiou":
        lista_vocales.append(palabra)
    else:
        lista_consonantes.append(palabra)

# Imprimir resultados
print(f"\nPalabras que empiezan con vocal: {lista_vocales}")
print(f"Cantidad con vocal: {len(lista_vocales)}")

print(f"Palabras que empiezan con consonantes: {lista_consonantes}")
print(f"Cantidad con consonante: {len(lista_consonantes)}")

