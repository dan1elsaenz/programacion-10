# Deque = cola
from collections import deque


def bfs_deque(grafo, nodo_inicio):
    visitado = set()
    cola = deque([nodo_inicio])
    while cola:
        nodo = cola.popleft()
        if nodo not in visitado:
            print(nodo, end=" ")
            visitado.add(nodo)
            cola.extend([vecino for vecino in grafo[nodo] if vecino not in visitado])


grafo = [[], [2, 4], [3], [], [5, 6], [], []]
nodo = 1
bfs_deque(grafo, nodo)
