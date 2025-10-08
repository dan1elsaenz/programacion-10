"""
Ejercicio 3: Encontrar la palabra más larga en una lista  

Dada una lista de palabras, devuelve la palabra con más caracteres. Si hay más de una con la misma longitud, devuelve la primera que aparece.

```
Entrada: ["perro", "elefante", "ratón"]  
Salida: "elefante"
```
"""

# Declarar lista
lista = ["perro", "elefante", "ratón"]

# Definir palabra más larga como el primer elemento de la lista
palabra_mas_larga = lista[0]

# Recorrer la lista por medio de un for (elemento por elemento)
for palabra in lista:
    # Si el largo de la palabra que por la que se está iterando es mayor que el largo de la palabra más larga hasta el momento
    if len(palabra) > len(palabra_mas_larga):
        # Sustituir la palabra más larga, por la palabra actual
        palabra_mas_larga = palabra

print(palabra_mas_larga)

