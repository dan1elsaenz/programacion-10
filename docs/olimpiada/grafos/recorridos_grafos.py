"""
Grafo utilizado en el ejemplo
"""
grafo = [[0,1,1,0], [1,0,0,1], [1,0,0,1], [0,1,1,0]]
grafoLista = [[1,2], [0,3], [0, 3], [1,2]]
# Por indice: [[2-1, 3-1], [1-1, 4-1], [1-1, 4-1], [2-1,3-1]]

"""
Recorrido/recubrimiento por profundidad para un grafo a partir de una matriz de adyacencia
"""
def recorrido_profundidad(grafo):
    pila = [0]

    # 1 = Si | 0 = No
    visitados = [0] * len(grafo)

    cont = 1 # Orden de nodos visitados

    while pila != []:
        top = pila.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont+=1

            for i in range(len(grafo[top])):
                if grafo[top][i] == 1 and not visitados[i]:
                    pila.append(i)
    print(visitados)


"""
Recubrimiento por anchura para un grafo con una matriz de adyacencia
"""
def recorrido_anchura(grafo):
    cola = [0]

    # 1 = Si | 0 = No
    visitados = [0] * len(grafo)

    cont = 1 # Orden de nodos visitados

    while cola != []:
        top = cola.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont+=1

            for i in range(len(grafo[top])):
                if grafo[top][i] == 1 and not visitados[i]:
                    cola.insert(0,i)
    print(visitados)

"""
Recubrimiento por anchura para un grafo con matriz de adyacencia (Collection: deque)
"""
from collections import deque
def recorridoAnchuraDeque(grafo):
    cola = deque()
    cola.append(0)

    # 1 = Si | 0 = No
    visitados = [0] * len(grafo)

    cont = 1 # Orden de nodos visitados

    while cola:
        front = cola.popleft()
        if not visitados[front]:
            visitados[front] = cont
            cont+=1

            for i in range(len(grafo[front])):
                if grafo[front][i] == 1 and not visitados[i]:
                    cola.append(i)
    print(visitados)

"""
Recubrimiento por profundidad para un grafo con una lista de adyacencia
"""
def recubrimientoProfundidadLista(grafoLista):
    pila = [0]

    # 1 = Si | 0 = No
    visitados = [0] * len(grafo)

    cont = 1 # Orden de nodos visitados

    while pila != []:
        top = pila.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont+=1

            for vecino in grafoLista[top]:
                if not visitados[vecino]:
                    pila.append(vecino)
    print(visitados)

"""
Verificar existencia de un camino para una secuencia de nodos dada
"""
# Si es un camino, es que existe la conexion entre una serie de nodos
# [1,2,3,4]
def esCamino(sec, grafo):
    # Para matriz de adyacencia
    if len(sec) < 2:
        return True
    if grafo[sec[0]][sec[1]] == 0:
        return False
    return esCamino(sec[1:], grafo)


"""
Comprobar si un grafo es conexo
"""
# Conexo es que no hayan nodo(s) que esten aislados del resto
def esConexo(grafoLista):
    pila = [0]

    # 1 = Si | 0 = No
    visitados = [False] * len(grafo)
    visitados[0] = True

    while pila != []:
        top = pila.pop()
        visitados[top] = True

        for vecino in grafoLista[top]:
            if not visitados[vecino]:
                pila.append(vecino)

    for i in visitados:
        if not i:
            return False
    return True