"""
Ejercicio 6: Comparar la longitud de dos palabras

Solicita dos palabras al usuario y muestra cuál es más larga o si tienen la misma cantidad de letras.

```
Entrada: "manzana pera"  
Salida: "La palabra 'manzana' es más larga que 'pera'."
```
"""

# Recibir las dos palabras
palabra1, palabra2 = input("Ingrese dos palabras separadas por un espacio: ").split()

# Verificar cuál palabra es más largo
if len(palabra1) > len(palabra2):
    print(f"La palabra '{palabra1}' es más larga que '{palabra2}'")
elif len(palabra1) < len(palabra2):
    print(f"La palabra '{palabra2}' es más larga que '{palabra1}'")
else:
    print(f"Las palabras '{palabra1}' y '{palabra2}' son del mismo largo")






