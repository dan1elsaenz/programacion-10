"""
Ejercicio 7: Verificar si una palabra empieza con vocal

Pide al usuario una palabra y muestra un mensaje indicando si comienza con una vocal.

```
Entrada: "elefante"  
Salida: "La palabra comienza con una vocal."
```
"""

# Ingresar una palabra del usuario
palabra = input("Ingrese una palabra: ")

if palabra[0].lower() in "aeiou":
    print("La palabra comienza con una vocal.")
else:
    print("La palabra no comienza con una vocal.")

