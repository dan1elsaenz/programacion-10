"""
Ejercicio 4: Última palabra de una oración  

Escribe una función que reciba una oración como string y devuelva la última palabra de la oración.

```
Entrada: "Hola, esto es un test"
Salida: 'test'
```
"""

# Input de la oración
oracion = input("Ingrese una oración: ")

# Separar la oración en palabras
palabras = oracion.split()

# Seleccionar la última palabra
ultima = palabras[-1]

# Imprimir
print(f"La última palabra es: {ultima}")

