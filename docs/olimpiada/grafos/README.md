# Algoritmos de Grafos

### Introducción a los Grafos

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

### _Depth First Search_ (DFS)

La **búsqueda en profundidad (DFS)** es un algoritmo de recorrido de grafos que explora tan profundo como sea posible a lo largo de cada rama antes de retroceder.

DFS se puede implementar de dos formas principales:

- **Recursiva**: Límitado por el _stack_ en la recursión para grafos grandes.
- **Iterativa**: útil para evitar límites de recursión.

#### DFS recursivo con lista de adyacencia

```python
def dfs(grafo, nodo, visitado=None):
    if visitado is None:
        visitado = set()  # Conjunto para registrar nodos ya visitados (evita repeticiones)
    visitado.add(nodo)
    print(nodo, end=' ')  # Procesa el nodo actual

    # Recorre todos los vecinos del nodo actual
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado)  # Llamada recursiva sobre el vecino no visitado
```

**Explicación**:

- Se parte de un nodo inicial (por ejemplo, `nodo = 0`).
- Se marca el nodo como visitado.
- Se visitan recursivamente sus vecinos no visitados.
- Al terminar de visitar todos los descendientes de un nodo, se "retrocede" y continúa con otros caminos.

---

#### DFS iterativo con matriz de adyacencia

```python
def dfs(grafo):
    pila = [0]  # Empieza desde el nodo 0 por ejemplo
    visitados = [0] * len(grafo)  # Marca si el nodo fue visitado y el orden en que fue visitado
    cont = 1  # Contador para registrar el orden de visita

    while pila:
        top = pila.pop()  # Extrae el nodo del top de la pila
        if not visitados[top]:
            visitados[top] = cont  # Marca el nodo como visitado con el contador
            cont += 1
            # Recorre los vecinos (desde el nodo más alto al más bajo)
            for i in reversed(range(len(grafo[top]))):
                if grafo[top][i] == 1 and not visitados[i]:
                    pila.append(i)  # Agrega vecinos no visitados a la pila
    print(visitados)
```

**Explicación**:

- Se utiliza una **pila explícita** (lista).
- La matriz `grafo[i][j] == 1` indica que existe una arista entre el nodo `i` y `j`.
- El recorrido sigue apilando vecinos conforme se descubren, y va sacando nodos del top de la pila.
- Se visita el nodo más recientemente descubierto antes de los anteriores (LIFO).

#### DFS iterativo con lista de adyacencia

```python
def dfs(grafoLista):
    pila = [0]  # Inicia desde el nodo 0, por ejemplo
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

**Explicación**:

- Similar a la versión con matriz, pero se usa una **lista de adyacencia**, que es más eficiente en espacio para grafos dispersos.
- `grafoLista[i]` contiene directamente una lista con los vecinos del nodo `i`, por lo que no se necesita revisar todos los índices como en una matriz.

---

### _Breadth First Search_ (BFS)

La **búsqueda en anchura (BFS)** es un algoritmo de recorrido de grafos que explora primero los nodos más cercanos al nodo de inicio, antes de avanzar hacia niveles más profundos.

BFS se basa en una **cola/deque (FIFO)**, lo que le permite recorrer los nodos nivel por nivel.

#### BFS iterativo con lista de adyacencia

```python
from collections import deque

def bfs(grafo, nodo_inicio):
    visitado = set()
    cola = deque([nodo_inicio]) # Inicializar cola
    while cola:
        nodo = cola.popleft()
        if nodo not in visitado:
            print(nodo, end=' ')
            visitado.add(nodo)
            # Agrega vecinos no visitados al final de la cola
            cola.extend([vec for vec in grafo[nodo] if vec not in visitado])
```

**Explicación**:

- Se comienza con el nodo de inicio.
- Se usa una `deque` como cola para extraer elementos del frente.
- Por cada nodo, se procesan sus vecinos inmediatos y se agregan a la cola si no han sido visitados.
- Se garantiza que todos los nodos a una misma _distancia_ del nodo inicial se visiten antes de avanzar al siguiente nivel.

#### BFS iterativo con matriz de adyacencia

```python
def bfs(grafo):
    cola = [0]  # Nodo inicial
    visitados = [0] * len(grafo)
    cont = 1

    while cola:
        top = cola.pop()  # Al usar .pop(), se extrae del final (poco eficiente)
        if not visitados[top]:
            visitados[top] = cont
            cont += 1
            # Se insertan nuevos vecinos al inicio de la cola (simula FIFO)
            for i in range(len(grafo[top])):
                if grafo[top][i] == 1 and not visitados[i]:
                    cola.insert(0, i)
    print(visitados)
```

**Explicación**:

- Esta versión utiliza una lista como cola, pero realiza `insert(0, ...)`, lo que puede ser ineficiente en listas grandes.
- `grafo[i][j] == 1` indica que existe una arista entre `i` y `j`.
- Aunque funcional, esta versión no es tan eficiente como la que usa `deque`.

---

#### BFS iterativo con `deque` y matriz de adyacencia

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

**Explicación**:

- Utiliza `deque` para un rendimiento mejorado al insertar y extraer elementos de la cola.
- Explora nodos adyacentes nivel por nivel, lo cual garantiza el orden adecuado.

---

### Orden Topológico (DAG)

El **orden topológico** es una enumeración lineal de los nodos de un **grafo dirigido acíclico (DAG)**, de forma que si existe una arista del nodo `u` al nodo `v`, entonces `u` aparece antes que `v` en el orden resultante.

Este tipo de recorrido es fundamental para tareas que presentan **dependencias** entre elementos, como:

- Compilación de módulos (donde un archivo depende de otros).
- Resolución de cursos con requisitos previos.

---

#### Implementación usando DFS

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

    return pila[::-1]  # Invierte la pila para obtener el orden correcto
```

**Explicación**:

- Se recorre el grafo en profundidad (DFS) desde cada nodo no visitado.
- Al finalizar la exploración de un nodo y todos sus descendientes, se agrega el nodo a una pila.
- Una vez completado el recorrido, se invierte la pila para obtener el **orden topológico**.
- `grafo.get(nodo, [])` permite manejar grafos donde algunos nodos pueden no tener vecinos explícitamente listados.

**Ejemplo**:

Para el grafo:

```python
grafo = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}
```

Una posible salida de `orden_topologico(grafo)` sería:

```
['B', 'D', 'A', 'C', 'E', 'H', 'F', 'G']
```

- Puede haber múltiples órdenes válidos siempre que se respete la precedencia de las aristas.
- El orden topológico **solo es posible si el grafo no contiene ciclos**. Si se detecta un ciclo, el algoritmo debe manejarlo o reportarlo.
- Este algoritmo tiene una complejidad de **O(V + E)**, donde `V` es el número de vértices y `E` el número de aristas.

### Detección de Ciclos

Detectar **ciclos** en un grafo permite determinar si existen **caminos cerrados**.

Sirve para verificar si un grafo dirigido es un **DAG** (grafo dirigido acíclico), condición necesaria para aplicar un orden topológico.

#### En grafo **no dirigido**

Se utiliza una búsqueda en profundidad (DFS) y se mantiene una referencia al **nodo padre** desde el cual se llegó al nodo actual.
Esto evita confundir la arista que regresa al padre con un ciclo real.

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

**Explicación**:

- Al visitar un vecino ya visitado que **no es el padre**, se ha encontrado un ciclo.
- La función recorre cada componente conexo del grafo.
- Se retorna `True` en cuanto se detecta el primer ciclo.

**Ejemplo**:

```python
# Ciclo: 1-2-3-4-1
grafo = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 1]
}
```

`tiene_ciclo(grafo)` retornará `True`.

#### En grafo **dirigido**

En grafos dirigidos, se debe evitar visitar nodos en el mismo camino de recursión.
Para ello, se emplean dos conjuntos:

- `visitado`: nodos ya completamente procesados.
- `en_recursion`: nodos que están actualmente en el camino de llamada recursiva.

```python
def tiene_ciclo_dirigido(grafo):
    visitado = set()
    en_recursion = set()

    def dfs(nodo):
        visitado.add(nodo)
        en_recursion.add(nodo)

        for vecino in grafo.get(nodo, []):
            if vecino not in visitado:
                if dfs(vecino):
                    return True
            elif vecino in en_recursion:
                return True  # Se encontró un ciclo

        en_recursion.remove(nodo)
        return False

    for nodo in grafo:
        if nodo not in visitado:
            if dfs(nodo):
                return True
    return False
```

**Explicación**:

- Si durante el recorrido se encuentra un nodo que ya está en el conjunto `en_recursion`, hay un ciclo.
- Al terminar de procesar un nodo, se elimina de `en_recursion`.
- Se explora el grafo desde todos los nodos que aún no han sido visitados.

**Ejemplo**:

```python
# Ciclo dirigido: A → B → C → A
grafo = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
```

`tiene_ciclo_dirigido(grafo)` retornará `True`.

---

### Componentes Conexas

Una **componente conexa** en un **grafo no dirigido** es un conjunto máximo de nodos donde existe al menos un camino entre cualquier par de nodos dentro del conjunto.

Si un grafo no dirigido tiene varias componentes conexas, significa que hay grupos de nodos completamente aislados unos de otros.

#### Identificación de componentes conexas con DFS

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

**Explicación**:

- Se recorre el grafo desde cada nodo no visitado.
- Para cada nueva búsqueda, se crea una nueva lista `componente` que agrupa los nodos conectados entre sí.
- Se utiliza DFS para agregar todos los nodos alcanzables desde el nodo actual.
- Al terminar, se agregan todas las componentes encontradas a una lista principal `componentes`.

#### Ejemplo

```python
grafo = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: [],
    5: [6],
    6: [5]
}
```

Este grafo tiene tres componentes conexas:

```python
[[0, 1], [2, 3], [4], [5, 6]]
```

- La complejidad del algoritmo es **O(V + E)**, donde `V` es el número de nodos y `E` el número de aristas.
- También se puede utilizar **BFS** en lugar de DFS, según se prefiera o por necesidades del entorno.

---

### Puntos de Articulación y Puentes (Tarjan)

En un **grafo no dirigido**, existen nodos y aristas críticas cuya eliminación puede afectar la conectividad del grafo:

- Un **punto de articulación** (o vértice de corte) es un **nodo** cuya eliminación incrementa el número de componentes conexas.
- Un **puente** (o arista de corte) es una **arista** cuya eliminación desconecta el grafo.

#### Algoritmo de Tarjan

El algoritmo de **Tarjan** se basa en DFS y utiliza:

- `disc[u]`: el tiempo en que se descubre el nodo `u`. Orden en el la DFS visita el nodo (`tiempo`).
- `low[u]`: el menor tiempo de descubrimiento alcanzable `disc[]` desde `u` (ya sea por un hijo o por un retroceso), descendiendo en el DFS (se retrocede hacia un tiempo menor, lo cual indica un nodo previo).
- `padre[u]`: el nodo padre desde el cual se llegó a `u` en el DFS.

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
                # Si `v` o un descendiente alcanza un nodo descubierto antes que `u`, entonces `u`
                # también puede alcanzarlo y se actualiza con este valor
                low[u] = min(low[u], low[v])

                # Condición para punto de articulación
                if padre.get(u) is None and hijos > 1:
                    articulaciones.add(u)

                # Si no existe un camino desde `v` o sus descendientes hacia un nodo descubierto antes que `u`
                # entonces el único camino hacia los anteriores, sería a través de `u`
                if padre.get(u) is not None and low[v] >= disc[u]:
                    articulaciones.add(u)

                # Condición para puente
                # Si no se alcanza ningún nodo descubierto antes que `u`
                if low[v] > disc[u]:
                    puentes.append((u, v))
            elif v != padre.get(u):
                # Caso de arista de retroceso
                #
                low[u] = min(low[u], disc[v])

    for u in grafo:
        if u not in visitado:
            dfs(u)

    return articulaciones, puentes
```

#### Condiciones para Punto de Articulación

Existen dos casos en que un nodo `u` es punto de articulación:

##### a) `u` es la raíz del árbol DFS y tiene más de un hijo

```python
if padre.get(u) is None and hijos > 1:
    articulaciones.add(u)
```

- Esto significa que `u` origina múltiples ramas desconectadas entre sí.
- Si se elimina `u`, esas ramas se separan.

##### b) `u` no es raíz y tiene un hijo `v` tal que `low[v] >= disc[u]`

```python
if padre.get(u) is not None and low[v] >= disc[u]:
    articulaciones.add(u)
```

- Esto implica que desde `v` (y sus descendientes) **no se puede alcanzar ningún ancestro de `u` sin pasar por `u`**.
- Si se elimina `u`, `v` y su subárbol quedan desconectados.

#### Condición para Puente

```python
if low[v] > disc[u]:
    puentes.append((u, v))
```

- Significa que la arista `(u, v)` es la **única conexión** entre los nodos `u` y `v`.
- No existe un camino alternativo desde `v` (ni sus descendientes) que regrese hacia `u` o sus ancestros.

#### Explicación del algoritmo

1. Al visitar `u`, se asigna `disc[u] = low[u] = tiempo`.
2. Se recorre cada vecino `v` de `u`.
   - Si `v` no está visitado, se hace DFS sobre `v`.
   - Al volver de la recursión, se actualiza `low[u] = min(low[u], low[v])`.
3. Se verifica si `u` es punto de articulación y si `(u, v)` es un puente.
4. Si `v` ya fue visitado **y no es el padre de `u`**, se actualiza:

   ```python
   low[u] = min(low[u], disc[v])
   ```

   Esto corresponde a una arista de retroceso.

#### Ejemplo

```python
grafo = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4, 5],
    4: [3],
    5: [3]
}
```

Salida:

```python
articulaciones = {2, 3}
puentes = [(2, 3), (3, 4), (3, 5)]
```

- El algoritmo tiene complejidad **O(V + E)**.
- Solo aplica para **grafos no dirigidos**.

---
