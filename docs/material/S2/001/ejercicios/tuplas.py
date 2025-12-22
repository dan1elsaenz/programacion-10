"""
Dada una lista de coordenadas (pares (x, y)), determinar cuál está más cerca del origen (0, 0).
"""

from math import sqrt

coordenadas = [(3, 4), (1, 1), (5, 5)]
distancias = []

for x, y in coordenadas:
    d = sqrt(x**2 + y**2)
    distancias.append(d)

i_min = distancias.index(min(distancias))
print(coordenadas[i_min])
