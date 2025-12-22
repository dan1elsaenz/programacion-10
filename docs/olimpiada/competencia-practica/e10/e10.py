"""
Ejercicio J. Recorrido en amplitud y profundidad
"""

import sys

sys.setrecursionlimit(101010)


def print(*objects, sep=" ", end="\n"):
    text = sep.join(map(str, objects))
    sys.stdout.write(f"{text}{end}")


def input():
    return sys.stdin.readline().rstrip("\r\n")


# Inicio de la solución

from collections import deque

# Lectura

n = int(input())

# Construir lista de adyacencia
arbol = [[] for _ in range(n)]

for _ in range(n):
    datos = list(map(int, input().split()))
    padre, cantidad_hijos = datos[0], datos[1]
    hijos = datos[2:]
    arbol[padre].extend(hijos)


# Recorrido BFS (amplitud)
def bfs(raiz):
    visitado = [False] * n
    orden = []
    cola = deque([raiz])
    visitado[raiz] = True

    while cola:
        nodo = cola.popleft()
        orden.append(nodo)
        for hijo in arbol[nodo]:
            if not visitado[hijo]:
                visitado[hijo] = True
                cola.append(hijo)
    return orden


# Recorrido DFS (profundidad)
def dfs(raiz, visitado, orden):
    visitado[raiz] = True
    orden.append(raiz)
    for hijo in arbol[raiz]:
        if not visitado[hijo]:
            dfs(hijo, visitado, orden)


# Ejecutar recorridos
orden_bfs = bfs(0)

visitado_dfs = [False] * n
orden_dfs = []
dfs(0, visitado_dfs, orden_dfs)

# Imprimir resultados
print(" ".join(map(str, orden_bfs)))
print(" ".join(map(str, orden_dfs)))
