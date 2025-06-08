# Clase 13: Estrategias de resolución de problemas y Complejidad temporal y espacial <!-- omit from toc -->

<details> 
  <summary>Tabla de contenidos</summary>

- [1. Estrategias mediante Ciclos](#1-estrategias-mediante-ciclos)
  - [Conceptos clave:](#conceptos-clave)
  - [¿En qué consisten?](#en-qué-consisten)
  - [Estrategias de identificación:](#estrategias-de-identificación)
  - [Ejemplo clave:](#ejemplo-clave)
- [2. Algoritmos de Fuerza Bruta (Búsqueda Exhaustiva)](#2-algoritmos-de-fuerza-bruta-búsqueda-exhaustiva)
  - [Conceptos clave:](#conceptos-clave-1)
  - [¿En qué consisten?](#en-qué-consisten-1)
  - [Estrategias de identificación:](#estrategias-de-identificación-1)
  - [Métodos comunes:](#métodos-comunes)
  - [Ejemplo clave:](#ejemplo-clave-1)
- [3. Algoritmos Voraces (_Greedy Algorithms_)](#3-algoritmos-voraces-greedy-algorithms)
  - [Conceptos clave:](#conceptos-clave-2)
  - [¿En qué consisten?](#en-qué-consisten-2)
  - [Estrategias de identificación:](#estrategias-de-identificación-2)
  - [Ejemplos típicos:](#ejemplos-típicos)
  - [Ejemplo clave:](#ejemplo-clave-2)
- [4. Divide y Vencerás](#4-divide-y-vencerás)
  - [Conceptos clave:](#conceptos-clave-3)
  - [¿En qué consisten?](#en-qué-consisten-3)
  - [Estrategias de identificación:](#estrategias-de-identificación-3)
  - [Técnicas frecuentes:](#técnicas-frecuentes)
  - [Ejemplo clave:](#ejemplo-clave-3)
- [5. Vuelta atrás (_Backtracking_)](#5-vuelta-atrás-backtracking)
  - [Conceptos clave:](#conceptos-clave-4)
  - [¿En qué consisten?](#en-qué-consisten-4)
  - [Estrategias de identificación:](#estrategias-de-identificación-4)
  - [Optimización mediante poda:](#optimización-mediante-poda)
  - [Ejemplo clave:](#ejemplo-clave-4)
- [6. Programación Dinámica (_Dynamic Programming_)](#6-programación-dinámica-dynamic-programming)
  - [Conceptos clave:](#conceptos-clave-5)
  - [¿En qué consisten?](#en-qué-consisten-5)
  - [Estrategias de identificación:](#estrategias-de-identificación-5)
  - [Técnicas clave:](#técnicas-clave)
  - [Ejemplos:](#ejemplos)
  - [Ejemplo clave:](#ejemplo-clave-5)
- [Complejidad temporal y espacial](#complejidad-temporal-y-espacial)
  - [1. Complejidad temporal](#1-complejidad-temporal)
    - [Clases de Complejidad Temporal](#clases-de-complejidad-temporal)
  - [2. Complejidad Espacial](#2-complejidad-espacial)
    - [Clases de Complejidad Espacial](#clases-de-complejidad-espacial)

</details> 

---

## 1. Estrategias mediante Ciclos

### Conceptos clave:

- Uso eficiente de ciclos (`for`, `while`) para explorar soluciones.
- Técnicas básicas para recorrer estructuras y verificar condiciones.

### ¿En qué consisten?

- Repetición sistemática y controlada para evaluar múltiples posibilidades.
- Muy útil para problemas simples o de tamaño pequeño.

### Estrategias de identificación:

- Se identifican cuando las soluciones requieren verificar casos particulares o iteraciones limitadas.
- Ejemplo típico: evaluar condiciones de todos los elementos o combinaciones simples.

### Ejemplo clave:

Encontrar el máximo en un arreglo recorriendo cada elemento:

```python
arr = [3, 7, 2, 9, 4]
maximo = arr[0]
for i in range(1, len(arr)):
    if arr[i] > maximo:
        maximo = arr[i]
print("Máximo:", maximo)
```

---

## 2. Algoritmos de Fuerza Bruta (Búsqueda Exhaustiva)

### Conceptos clave:

- Explorar todas las soluciones posibles.
- Asegurar respuesta correcta con métodos sencillos, aunque potencialmente ineficientes.

### ¿En qué consisten?

- Generar explícitamente todas las soluciones posibles para elegir la mejor o contar soluciones.
- Técnicas comunes: generación de subconjuntos y permutaciones.

### Estrategias de identificación:

- Útil cuando la entrada es suficientemente pequeña.
- Se usa cuando la exactitud es esencial y el tiempo lo permite.

### Métodos comunes:

- Generación de subconjuntos (recursión, representación en bits).
- Generación de permutaciones (recursión, funciones como `next_permutation`).

### Ejemplo clave:

Generar todas las permutaciones de un conjunto pequeño de números:

```python
from itertools import permutations
for p in permutations([1, 2, 3]):
    print(p)
```

---

## 3. Algoritmos Voraces (_Greedy Algorithms_)

### Conceptos clave:

- Tomar decisiones localmente óptimas esperando un resultado globalmente óptimo.
- Soluciones rápidas y eficientes cuando se garantiza su corrección.

### ¿En qué consisten?

- Construir la solución paso a paso escogiendo la opción óptima inmediata.

### Estrategias de identificación:

- Útil cuando las elecciones locales garantizan un óptimo global (justificación matemática clara).
- Ejemplos clásicos: problemas de monedas, planificación, selección de actividades.

### Ejemplos típicos:

- Problema de monedas (selección de moneda más grande posible).
- Tareas y tiempos límite (ordenar por duración).

### Ejemplo clave:

Problema de monedas: seleccionar la menor cantidad posible de monedas para formar una suma dada.

**Lógica:** Este algoritmo ordena las monedas en orden descendente y selecciona repetidamente la moneda más grande posible que no exceda el monto restante. Como siempre se elige la mayor moneda disponible, el número de monedas usadas es mínimo (siempre que el conjunto de monedas cumpla con la propiedad de ser un sistema canónico, como el del euro).

```python
monedas = [1, 2, 5, 10, 20, 50, 100, 200]
monto = 520
conteo = 0

monedas.sort(reverse=True)
for moneda in monedas:
    while monto >= moneda:
        monto -= moneda
        conteo += 1

print("Número mínimo de monedas:", conteo)
```

---

## 4. Divide y Vencerás

### Conceptos clave:

- Dividir problemas grandes en subproblemas más pequeños y manejables.
- Resolver subproblemas individualmente y combinar resultados.

### ¿En qué consisten?

- Dividir el problema original en subproblemas del mismo tipo más pequeños.
- Resolver cada subproblema independientemente y combinarlos eficientemente.

### Estrategias de identificación:

- Identificar que el problema se puede partir en partes más pequeñas.
- Ejemplos clásicos: mergesort, búsqueda binaria, multiplicación rápida de matrices, problemas de suma con "encuentro en el medio".

### Técnicas frecuentes:

- Encuentro en el medio: reduce complejidad exponencial significativamente.

### Ejemplo clave:

Algoritmo mergesort: dividir un arreglo, ordenar subarreglos y combinarlos.

**Lógica:** El algoritmo divide recursivamente el arreglo en mitades hasta obtener subarreglos de un solo elemento. Luego, en la fase de combinación, fusiona esos subarreglos en orden usando comparaciones. Esta estrategia logra un tiempo de ejecución de O(n log n) en el peor caso.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

---

## 5. Vuelta atrás (_Backtracking_)

### Conceptos clave:

- Construcción incremental de soluciones con verificación temprana de viabilidad.
- Exploración profunda de soluciones parciales.

### ¿En qué consisten?

- Explorar soluciones parciales hasta encontrar una completa válida.
- Se retrocede cuando una solución parcial es inviable ("poda").

### Estrategias de identificación:

- Adecuado cuando no se puede asegurar una solución óptima inmediata.
- Ejemplos típicos: Problema de las n-reinas, caminos en cuadrícula.

### Optimización mediante poda:

- Evitar exploraciones inútiles identificando condiciones que indiquen inviabilidad temprano.

### Ejemplo clave:

Problema de las 8 reinas en un tablero de ajedrez.

**Lógica:** El algoritmo intenta colocar una reina en cada fila del tablero asegurando que no haya conflicto con reinas previamente colocadas en columnas o diagonales. Si no es posible, retrocede (backtrack) y prueba otra posición. Esta técnica permite recorrer todo el espacio de soluciones válidas.

```python
n = 8
count = 0
col = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

def buscar(y):
    global count
    if y == n:
        count += 1
        return
    for x in range(n):
        if col[x] or diag1[x + y] or diag2[x - y + n - 1]:
            continue
        col[x] = diag1[x + y] = diag2[x - y + n - 1] = True
        buscar(y + 1)
        col[x] = diag1[x + y] = diag2[x - y + n - 1] = False

buscar(0)
print("Soluciones encontradas:", count)
```

---

## 6. Programación Dinámica (_Dynamic Programming_)

### Conceptos clave:

- División del problema en subproblemas más pequeños solapados.
- Almacenamiento de resultados de subproblemas para evitar recálculos (memoización).

### ¿En qué consisten?

- Resolver problemas mediante relaciones recursivas y almacenamiento eficiente de resultados.
- Combina precisión de búsqueda exhaustiva y eficiencia.

### Estrategias de identificación:

- Subproblemas con solapamiento evidente y estructuras recursivas claras.
- Ejemplos clásicos: Problemas de monedas, subsecuencia creciente más larga, caminos óptimos, problemas de mochila, distancia de edición.

### Técnicas clave:

- Formulación recursiva clara.
- Memoización y construcción iterativa.
- Recuperación de soluciones óptimas con rastreo adicional.

### Ejemplos:

- Problema de monedas (mínimo número y conteo de formas).
- Subsecuencia creciente más larga.
- Caminos óptimos en cuadrícula.
- Problemas de mochila.
- Distancia de edición.

### Ejemplo clave:

Calcular la distancia de edición (distancia de Levenshtein) entre dos palabras.

**Lógica:** Se usa programación dinámica para calcular el número mínimo de operaciones (inserción, eliminación, sustitución) requeridas para transformar una cadena en otra. Se construye una matriz donde cada celda representa la distancia entre prefijos de las cadenas.

```python
a = "LOVE"
b = "MOVIE"
dp = [[0] - (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a) + 1):
    dp[i][0] = i
for j in range(len(b) + 1):
    dp[0][j] = j

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        costo = 0 if a[i - 1] == b[j - 1] else 1
        dp[i][j] = min(dp[i - 1][j] + 1,  # eliminar
                       dp[i][j - 1] + 1,  # insertar
                       dp[i - 1][j - 1] + costo)  # reemplazar

print("Distancia de edición:", dp[len(a)][len(b)])
```

## Complejidad temporal y espacial

La complejidad de un algoritmo es una medida que permite estimar su eficiencia en términos del tiempo que tarda en ejecutarse (complejidad temporal) y la cantidad de memoria que requiere (complejidad espacial).
Estas medidas se expresan habitualmente usando la notación Big-O ($$O$$), que describe el comportamiento del algoritmo en función del tamaño de la entrada $n$.

---

### 1. Complejidad temporal

La complejidad temporal mide cuántas operaciones realiza un algoritmo según el tamaño de entrada.
Es importante especialmente cuando se diseñan algoritmos que deben ejecutarse en tiempos razonables incluso con entradas grandes.
Para algoritmos recursivos, se puede estimar multiplicando el tiempo por llamada por el número total de llamadas.

**Fórmula general (para recursión):**

```
Tiempo por llamada × Número de llamadas
```

#### Clases de Complejidad Temporal

1. $$O(1)$$: Tiempo constante.

   * El tiempo no depende del tamaño de entrada.
   * Ejemplo: acceder al valor de un índice en una lista: `x = arr[5]`

2. $$O(\log{n})$$: Tiempo logarítmico.

   * Reduce a la mitad la entrada en cada paso.
   * Ejemplo: búsqueda binaria en una lista ordenada.

3. $$O(\sqrt{n})$$: Tiempo raíz cuadrada.

   * Se usa, por ejemplo, en verificaciones hasta $$\sqrt{n}$$, como en tests de primalidad.
   * Ejemplo: comprobar si un número es primo dividiendo hasta $$\sqrt{n}$$.

4. $$O(n)$$: Tiempo lineal.

   * Recorre la entrada una vez.
   * Ejemplo: encontrar el mínimo en un arreglo.

5. $$O(n \log{n})$$: Tiempo log-lineal.

   * Algoritmo eficiente de ordenamiento como `merge sort` o `heap sort`.

6. $$O(n^2)$$: Tiempo cuadrático.

   * Dos ciclos anidados.
   * Ejemplo: bubble sort o comprobar todos los pares posibles.

7. $$O(n^3)$$: Tiempo cúbico.

   * Tres ciclos anidados.
   * Ejemplo: multiplicación de matrices con triple bucle.

8. $$O(2^n)$$: Tiempo exponencial.

   * Itera sobre todos los subconjuntos posibles.
   * Ejemplo: resolver el problema de la mochila con backtracking.

9. $$O(n!)$$*: Tiempo factorial.

   * Considera todas las permutaciones posibles.
   * Ejemplo: resolver el problema del viajante (TSP) por fuerza bruta.

---

### 2. Complejidad Espacial

La complejidad espacial se refiere a la cantidad de memoria adicional que necesita un algoritmo en función del tamaño de entrada.
Esto incluye estructuras de datos auxiliares, variables temporales, llamadas recursivas, entre otros.

Un algoritmo puede ser rápido pero utilizar mucha memoria, o puede ser más lento pero más eficiente en espacio.
A menudo, hay un compromiso entre tiempo y espacio.

#### Clases de Complejidad Espacial

1. $$O(1)$$: Espacio constante.

   * Usa una cantidad fija de memoria, independientemente del tamaño de entrada.
   * Ejemplo: invertir una cadena en el mismo arreglo sin estructuras auxiliares.

2. $$O(\log{n})$$: Espacio logarítmico.

   * Aparece en recursión como en la búsqueda binaria recursiva.

3. $$O(n)$$: Espacio lineal.

   * Almacena datos proporcionales a la entrada.
   * Ejemplo: copiar un arreglo o calcular suma de prefijos.

4. $$O(n^2)$$: Espacio cuadrático.

   * Utiliza una matriz o tabla de tamaño $$n \times n$$.
   * Ejemplo: algoritmo de programación dinámica como distancia de edición o Floyd-Warshall.

5. $$O(2^n)$$: Espacio exponencial.

   * Guarda todos los subconjuntos o ramas posibles.
   * Ejemplo: resolver problemas de decisión con memoización sin poda.

