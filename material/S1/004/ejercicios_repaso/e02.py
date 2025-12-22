"""
Ejercicio 2: Clasificación de palabras  

Escribe un programa que reciba una palabra y determine si cumple con alguna de las siguientes condiciones:

- Es un palíndromo (se lee igual al derecho y al revés).
- Tiene más de 5 caracteres.
- Comienza con una vocal.

Debe imprimir una lista con los mensajes correspondientes.

```
Entrada: "radar"  
Salida: ['La palabra es un palíndromo.']
```
"""

# Recibir la palabra de la terminal por medio de un input
palabra = input("Ingrese una palabra: ")

# Lista vacía para almacenar los resultados de las condiciones
resultados = []

# Verificar si es un palíndromo
if palabra == palabra[::-1]:
    resultados.append("La palabra es un palíndromo.")

# Verificar si tiene más de 5 caracteres
if len(palabra) > 5: 
    resultados.append("La palabra tiene más de 5 caracteres.")

# Verificar si comienza con un vocal
if palabra[0].lower() in "aeiou":
    resultados.append("La palabra comienza con un vocal.")

# Imprimir resultados
print(resultados)

