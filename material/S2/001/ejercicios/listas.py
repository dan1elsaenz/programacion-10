"""
Convertir una lista de temperaturas en grados Celsius a Fahrenheit.
Eliminar duplicados, redondear a un decimal y ordenar de mayor a menor.
"""

celsius = [25, 30, 30, 10]

# Eliminar duplicados
celsius = list(set(celsius))

fahrenheit = [9 / 5 * x + 32 for x in celsius]
fahrenheit.sort(reverse=True)

print(fahrenheit)
