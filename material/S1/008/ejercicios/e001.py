"""
Ejercicio 1: Análisis de coordenadas

Solicita al usuario una lista de coordenadas (x, y), almacenadas como tuplas (desplazamiento).
Calcula la distancia total.
"""
from math import sqrt

# Solicitar la lista de puntos
cantidad_puntos = int(input("Ingrese la cantidad de puntos: "))

# Solicitar las coordenadas (x,y)
puntos = []

for punto in range(1, cantidad_puntos+1):
    x = int(input(f"Ingrese la coordenada x{punto}: "))
    y = int(input(f"Ingrese la coordenada y{punto}: "))

    puntos.append((x, y))

# Recorrer lista de tuplas
# lista = [(x1, y1), (x2, y2), ...]

distancia_total = 0

for i in range(cantidad_puntos-1):
    x1 = puntos[i][0]
    y1 = puntos[i][1]

    x2 = puntos[i+1][0]
    y2 = puntos[i+1][1]

    distancia_parcial = sqrt((x2 - x1)**2 + (y2 - y1)**2)

    distancia_total += distancia_parcial

print(f"La distancia total recorrida fue: {distancia_total}.")

