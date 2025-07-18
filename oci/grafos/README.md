# Algoritmos de Grafos

---

### 1. Introducción a los Grafos

Un **grafo** es una estructura que modela relaciones entre pares de elementos.
Cada elemento se llama **nodo** o **vértice**, y cada conexión entre dos nodos se llama **arista**.

- Un grafo puede ser:
  - **Dirigido**: las aristas tienen una dirección (A → B).
  - **No dirigido**: las aristas no tienen dirección (A ↔ B).
  - **Ponderado**: las aristas tienen un peso o costo.

```python
# Representación con lista de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

También se puede representar con una **matriz de adyacencia**:

```python
grafo = [[0,1,1,0], [1,0,0,1], [1,0,0,1], [0,1,1,0]]
grafoLista = [[1,2], [0,3], [0, 3], [1,2]]
# Por índice: [[2-1, 3-1], [1-1, 4-1], [1-1, 4-1], [2-1,3-1]]
```

---

### 2. _Depth First Search_ (DFS)

La **búsqueda en profundidad** explora cada rama del grafo lo más profundo posible antes de retroceder.
Se implementa normalmente de forma recursiva o con una pila.

```python
def dfs(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(nodo)
    print(nodo, end=' ')
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)
```

Versión con matriz de adyacencia:

```python
def dfs(grafo):
    pila = [0]
    visitados = [0] * len(grafo)
    cont = 1
    while pila:
        top = pila.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont += 1
            for i in range(len(grafo[top])):
                if grafo[top][i] == 1 and not visitados[i]:
                    pila.append(i)
    print(visitados)
```

Con lista de adyacencia:

```python
def dfs(grafoLista):
    pila = [0]
    visitados = [0] * len(grafoLista)
    cont = 1
    while pila:
        top = pila.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont += 1
            for vecino in grafoLista[top]:
                if not visitados[vecino]:
                    pila.append(vecino)
    print(visitados)
```

---

### 3. _Breadth First Search_ (BFS)

La **búsqueda en anchura** explora los nodos más cercanos primero.
Utiliza típicamente una cola para recorrer los nodos nivel por nivel.

```python
from collections import deque

def bfs(grafo, nodo_inicio):
    visitado = set()
    cola = deque([nodo_inicio])
    while cola:
        nodo = cola.popleft()
        if nodo not in visitado:
            print(nodo, end=' ')
            visitado.add(nodo)
            cola.extend([vec for vec in grafo[nodo] if vec not in visitado])
```

Con matriz de adyacencia:

```python
def bfs(grafo):
    cola = [0]
    visitados = [0] * len(grafo)
    cont = 1
    while cola:
        top = cola.pop()
        if not visitados[top]:
            visitados[top] = cont
            cont += 1
            for i in range(len(grafo[top])):
                if grafo[top][i] == 1 and not visitados[i]:
                    cola.insert(0, i)
    print(visitados)
```

Con deque (más eficiente):

```python
from collections import deque

def bfs(grafo):
    cola = deque()
    cola.append(0)
    visitados = [0] * len(grafo)
    cont = 1
    while cola:
        front = cola.popleft()
        if not visitados[front]:
            visitados[front] = cont
            cont += 1
            for i in range(len(grafo[front])):
                if grafo[front][i] == 1 and not visitados[i]:
                    cola.append(i)
    print(visitados)
```

---

### 4. Orden Topológico (DAG)

El **orden topológico** es una enumeración lineal de los nodos de un grafo dirigido acíclico (DAG) tal que si existe una arista de $u$ a $v$, entonces $u$ aparece antes que $v$.
Es útil para planificar tareas con dependencias, como la compilación de módulos o la resolución de prerequisitos académicos.

```python
def orden_topologico(grafo):
    visitado = set()
    pila = []

    def dfs(nodo):
        visitado.add(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitado:
                dfs(vecino)
        pila.append(nodo)

    for nodo in grafo:
        if nodo not in visitado:
            dfs(nodo)

    return pila[::-1]
```

---

### 5. Detección de Ciclos

Detectar **ciclos** permite saber si un grafo contiene caminos cerrados.
Esto es fundamental para verificar si un grafo es un DAG, por ejemplo.

#### En grafo no dirigido

Se utiliza DFS manteniendo referencia al _parent_ del nodo actual para no confundir la arista de regreso con un ciclo real.

```python
def tiene_ciclo(grafo):
    visitado = set()

    def dfs(nodo, padre):
        visitado.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitado:
                if dfs(vecino, nodo):
                    return True
            elif vecino != padre:
                return True
        return False

    for nodo in grafo:
        if nodo not in visitado:
            if dfs(nodo, None):
                return True
    return False
```

---

### 6. Componentes Conexas

Una **componente conexa** es un conjunto máximo de nodos conectados entre sí mediante caminos.
En grafos no dirigidos, podemos encontrarlas usando DFS o BFS.

```python
def componentes_conexas(grafo):
    visitado = set()
    componentes = []

    def dfs(nodo, componente):
        visitado.add(nodo)
        componente.append(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitado:
                dfs(vecino, componente)

    for nodo in grafo:
        if nodo not in visitado:
            componente = []
            dfs(nodo, componente)
            componentes.append(componente)

    return componentes
```

---

### 7. Puntos de Articulación y Puentes (Tarjan)

- Un **punto de articulación** es un nodo cuya eliminación incrementa el número de componentes conexas.
- Un **puente** es una arista cuya eliminación desconecta el grafo.

El algoritmo de **Tarjan** utiliza DFS y registra el tiempo de descubrimiento y el menor tiempo alcanzable (`low`) para detectar estos puntos críticos.

```python
def articulaciones_y_puentes(grafo):
    tiempo = 0
    visitado = set()
    disc = {}
    low = {}
    padre = {}
    articulaciones = set()
    puentes = []

    def dfs(u):
        nonlocal tiempo
        visitado.add(u)
        disc[u] = low[u] = tiempo
        tiempo += 1
        hijos = 0

        for v in grafo[u]:
            if v not in visitado:
                padre[v] = u
                hijos += 1
                dfs(v)
                low[u] = min(low[u], low[v])

                if padre.get(u) is None and hijos > 1:
                    articulaciones.add(u)
                if padre.get(u) is not None and low[v] >= disc[u]:
                    articulaciones.add(u)

                if low[v] > disc[u]:
                    puentes.append((u, v))
            elif v != padre.get(u):
                low[u] = min(low[u], disc[v])

    for u in grafo:
        if u not in visitado:
            dfs(u)

    return articulaciones, puentes
```

---
