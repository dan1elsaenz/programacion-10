"""
Ejercicio 1: Contar vocales en una palabra  

Escribe un programa que reciba una palabra y cuente cuántas vocales (`a, e, i, o, u`) tiene.

```
Entrada: "elefante"
Salida: 4

Entrada: "python"
Salida: 1
```
"""

# String a analizar
string = "Elefante"

# Declaración de variable contador (mantener la cuenta de vocales)
contador = 0

# Recorrer string en minúsculas
for letra in string.lower():
    # Si la letra (variable iteradora) está en el string "aeiou", incrementar valor de contador en 1
    if letra in "aeiou":
        contador += 1

# Imprimir valor de contador
print(contador)

