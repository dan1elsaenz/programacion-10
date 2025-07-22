"""
Arreglos multidimensionales: Listas dentro de listas
"""

# === Arreglos bidimensionales ===

# Filas: Listas anidadas
# Columnas: Elementos dentro de la listas con índice compartido

# Tablero 3x3
tablero = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# ¿Cómo acceder a los elementos?
# nombre[fila] selecciona la fila completa
# nombre[fila][columna]
# Filas y columnas comienzan en 0

print(tablero[2][2])

