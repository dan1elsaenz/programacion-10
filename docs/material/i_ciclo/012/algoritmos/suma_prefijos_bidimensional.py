"""
Suma de prefijos para una matriz bidimensional
"""

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]

# Determinar tamaño de la matriz
filas, columnas = len(matriz), len(matriz[0])

p = [[0]*columnas for _ in range(filas)] # List comprehension

# Primera entrada
p[0][0] = matriz[0][0]

# Primera columna
for i in range(1, filas):
    p[i][0] = p[i-1][0] + matriz[i][0]

# Primera fila
for j in range(1, columnas):
    p[0][j] = p[0][j-1] + matriz[0][j]

# Resto de la matriz
for i in range(1, filas):
    for j in range(1, columnas):
        p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + matriz[i][j]

# Consulta entre (f1, c1) y (f2, c2)
def suma_submatriz(f1, c1, f2, c2):
    suma = p[f2][c2]
    if f1 > 0: suma -= p[f1-1][c2]
    if c1 > 0: suma -= p[f2][c1-1]
    if f1 > 0 and c1 > 0: suma += p[f1-1][c1-1]
    return suma

