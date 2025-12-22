"""
Ejercicio 16: Mostrar letras comunes entre pares de palabras (for anidado)

Dada una lista de dos palabras, muestra las letras que tienen en común (sin repetir letras).

```
Entrada: ["python", "elefante"]
Salida: ['t', 'n']
```
"""

lista = ["python", "elefante"]

palabra1 = lista[0]
palabra2 = lista[1]

letras_repetidas = []


# Método 1: Con el operador in
for letra in palabra1:
    # Comprobar que letra esté en palabra2 y que no esté ya colocada en la lista
    if letra in palabra2 and letra not in letras_repetidas:
        letras_repetidas.append(letra)


# Método 2: Con for anidados
# Recorrer palabra1
for caracter1 in palabra1:
    # Recorrer palabra2
    for caracter2 in palabra2:
        # Comprobar que los caracteres son iguales y que no está en la lista
        if caracter1 == caracter2 and caracter1 not in letras_repetidas:
            letras_repetidas.append(caracter1)

print(letras_repetidas)

