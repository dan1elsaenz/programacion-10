"""
Lista de adyacencia
"""
def dfs_lista_adyacencia(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo, end=' ')

    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_lista_adyacencia(grafo, vecino, visitado)

# # Lista de adyacencia del grafo
# grafo = [[], [2,4], [3], [], [5,6], [], []]
#
# # Nodo de partida
# nodo = 1
#
# dfs_lista_adyacencia(grafo, nodo)

"""
Pila
"""

def dfs_pila(grafo, nodo):
    pila = [nodo] # Vecinos por visitar
    visitados = [0] * len(grafo)
    cont = 1 # Posición en la que se visitó el nodo

    while pila:
        top = pila.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont += 1
            for vecino in reversed(grafo[top]):
                if not visitados[vecino]:
                    pila.append(vecino)
    print(visitados)

# grafo = [[], [2,4], [3], [], [5,6], [], []]
# nodo = 1
# dfs_pila(grafo, nodo)


"""
Matriz de adyacencia
"""

def dfs_matriz_adyacencia(grafo, nodo):
    pila = [nodo] # Vecinos pendientes por visitar
    visitados = [0] * len(grafo)
    cont = 1

    while pila:
        top = pila.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont += 1
            for i in reversed(range(len(grafo[top]))):
                if grafo[top][i] == 1 and not visitados[i]:
                    pila.append(i)
    print(visitados)

grafo = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
nodo = 1

dfs_matriz_adyacencia(grafo, nodo)


