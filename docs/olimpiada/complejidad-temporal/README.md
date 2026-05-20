---
icon: material/chart-line
---

<!-- Colocar formato matemático -->
<script id="MathJax-script" async src="https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
  window.MathJax = {
    tex: {
      inlineMath: [["$", "$"], ["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
</script>

# :material-chart-line: Complejidad Temporal

## Eficiencia de un algoritmo

Para resolver un problema, casi siempre existe más de una forma de hacerlo.
Todas las soluciones pueden dar la respuesta correcta, pero no todas lo hacen con la misma rapidez ni con la misma cantidad de memoria.
La **eficiencia** de un algoritmo mide cuántos recursos consume al ejecutarse: principalmente tiempo y memoria.

Como ejemplo, para buscar un nombre en una lista de un millón de personas se puede revisar la lista de principio a fin (lo que puede tomar hasta un millón de pasos), o, si la lista está ordenada, usar búsqueda binaria y encontrarlo en apenas 20 pasos.
Ambos algoritmos son correctos, pero uno es drásticamente más eficiente.

!!! note "La eficiencia importa más con entradas grandes"
    Para entradas pequeñas, cualquier algoritmo termina casi instantáneamente.
    Las diferencias de eficiencia se vuelven críticas cuando la entrada tiene miles o millones de elementos.

## Complejidad temporal y espacial

La eficiencia de un algoritmo se analiza en dos dimensiones: cuánto **tiempo** tarda y cuánta **memoria** necesita.

### Complejidad temporal

La **complejidad temporal** describe cómo crece el tiempo de ejecución del algoritmo conforme aumenta el tamaño de la entrada.
No mide segundos exactos (eso depende del hardware y del lenguaje), sino el número de operaciones que realiza en función del tamaño de la entrada, representado por la variable `n`.

Por ejemplo, si un algoritmo recorre una lista de `n` elementos una sola vez, realiza `n` operaciones.
Si tiene dos ciclos anidados, realiza aproximadamente $n^2$ operaciones.

### Complejidad espacial

La **complejidad espacial** describe cuánta memoria adicional necesita el algoritmo en función de `n`.
Un algoritmo que trabaja con unas pocas variables, sin importar el tamaño de la entrada, usa espacio constante.
Uno que guarda una copia de la lista de entrada usa espacio proporcional a `n`.

=== "Ejemplos de complejidad temporal"

    | Situación | Complejidad |
    |-----------|-------------|
    | Calcular una fórmula directa | $O(1)$ |
    | Un ciclo de `n` iteraciones | $O(n)$ |
    | Dos ciclos anidados | $O(n^2)$ |
    | Reducir el problema a la mitad en cada paso | $O(\log n)$ |

=== "Ejemplos de complejidad espacial"

    | Situación | Complejidad |
    |-----------|-------------|
    | Usar solo algunas variables fijas | $O(1)$ |
    | Guardar una lista de `n` elementos | $O(n)$ |
    | Guardar una matriz de $n \times n$ | $O(n^2)$ |
    | Recursión que divide a la mitad en cada nivel | $O(\log n)$ |

## Análisis asintótico

El **análisis asintótico** estudia el comportamiento de un algoritmo para entradas grandes.
La idea central es que cuando `n` crece mucho, lo que importa es el **orden de magnitud** del número de operaciones, no los detalles exactos.

Esto lleva a dos reglas fundamentales:

**Regla 1: se ignoran los factores constantes.**
Si un ciclo se ejecuta `3n`, `n + 5` o `n/2` veces, todos tienen el mismo orden de magnitud: crecen linealmente con `n`.
Las constantes dependen del hardware y del lenguaje, no del diseño del algoritmo.

```python
for i in range(3 * n):    # 3n iteraciones
    pass

for i in range(n + 5):    # n+5 iteraciones
    pass

for i in range(0, n, 2):  # n/2 iteraciones
    pass
```

Los tres fragmentos tienen la misma complejidad porque todos crecen de forma lineal con `n`.

**Regla 2: solo se conserva el término dominante.**
Si un algoritmo realiza $n^2 + n$ operaciones, el término `n` se vuelve insignificante comparado con $n^2$ cuando `n` es grande.
Se conserva solo $n^2$.

!!! note "El objetivo del análisis asintótico"
    No se busca saber cuántas operaciones exactas realiza el algoritmo, sino cómo _crece_ ese número con la entrada.
    Esto permite comparar algoritmos de forma independiente al hardware.

## Notación O grande

La **notación O grande** es la herramienta formal para expresar complejidad.
Se escribe O seguido de una función: $O(n)$, $O(n^2)$, $O(\log n)$, etc.
La función dentro del paréntesis describe cómo crece el número de operaciones en el peor caso posible.

Para calcular la complejidad de un código, se aplican cuatro reglas:

### Un ciclo

Un ciclo que recorre `n` elementos tiene complejidad $O(n)$.
Con `k` ciclos anidados, la complejidad es $O(n^k)$.

```python
# O(n)
for i in range(n):
    pass  # (1)!

# O(n²)
for i in range(n):
    for j in range(n):
        pass  # (2)!

# O(n³)
for i in range(n):
    for j in range(n):
        for k in range(n):
            pass  # (3)!
```

1. El ciclo realiza exactamente `n` iteraciones.
2. El ciclo interior se ejecuta `n` veces por cada vuelta del exterior: $n \times n = n^2$.
3. Con tres ciclos: $n \times n \times n = n^3$.

!!! tip "El ciclo interior no siempre empieza en 0"
    Si el ciclo interior empieza en `i + 1` en lugar de `0`, el número de iteraciones totales es $\frac{n(n-1)}{2}$, que sigue siendo $O(n^2)$.

    ```python
    for i in range(n):
        for j in range(i + 1, n):  # j comienza después de i
            pass
    # Complejidad: O(n²)
    ```

### Fases consecutivas

Si un algoritmo tiene varias etapas que se ejecutan una tras otra, la complejidad total es la de la etapa más lenta (el **cuello de botella**), porque las etapas rápidas quedan eclipsadas por ella.

```python
for i in range(n):          # Fase 1: O(n)
    pass

for i in range(n):          # Fase 2: O(n²)
    for j in range(n):
        pass

for i in range(n):          # Fase 3: O(n)
    pass

# Complejidad total: O(n²)
```

### Varias variables

Cuando el algoritmo depende de más de un tamaño de entrada, la complejidad incluye todas las variables.

```python
for i in range(n):
    for j in range(m):
        pass
# Complejidad: O(n · m)
```

La complejidad del ejemplo anterior es $O(n \cdot m)$.

### Recursión

La complejidad de una función recursiva es el producto entre el número de llamadas que genera y el trabajo que hace cada llamada.

=== "Recursión lineal: $O(n)$"

    ```python
    def f(n):
        if n == 1:
            return
        f(n - 1)  # (1)!
    ```

    1. Cada llamada genera exactamente una más, hasta llegar a `n = 1`. En total hay `n` llamadas, cada una con trabajo $O(1)$.

=== "Recursión exponencial: $O(2^n)$"

    ```python
    def g(n):
        if n == 1:
            return
        g(n - 1)  # (1)!
        g(n - 1)  # (2)!
    ```

    1. Primera llamada recursiva. Duplica el trabajo en este nivel.
    2. Segunda llamada recursiva. Duplica el trabajo nuevamente.

    Cada nivel duplica el número de llamadas activas:

    | Llamada | Número de llamadas |
    |---------|--------------------|
    | `g(n)` | 1 |
    | `g(n-1)` | 2 |
    | `g(n-2)` | 4 |
    | ... | ... |
    | `g(1)` | $2^{n-1}$ |

    Total: $1 + 2 + 4 + ... + 2^{n-1} = 2^n - 1 \Rightarrow O(2^n)$

## Clases de complejidad comunes

La siguiente tabla resume las complejidades más frecuentes, ordenadas de más a menos eficiente:

| Complejidad   | Nombre             | Ejemplo típico                             |
| ------------- | ------------------ | ------------------------------------------ |
| $O(1)$        | Constante          | Acceder a un elemento por índice           |
| $O(\log n)$   | Logarítmica        | Búsqueda binaria                           |
| $O(\sqrt{n})$ | Raíz cuadrada      | Verificar si un número es primo            |
| $O(n)$        | Lineal             | Recorrer una lista una vez                 |
| $O(n \log n)$ | Lineal-logarítmica | Ordenamiento eficiente                     |
| $O(n^2)$      | Cuadrática         | Ordenamiento de burbuja                    |
| $O(n^3)$      | Cúbica             | Floyd-Warshall, multiplicación de matrices |
| $O(2^n)$      | Exponencial        | Generar todos los subconjuntos             |
| $O(n!)$       | Factorial          | Generar todas las permutaciones            |

!!! abstract "Guía de estimación práctica"
    Una computadora moderna realiza aproximadamente 100 a 500 millones de operaciones simples por segundo.
    Esta tabla muestra qué complejidad se necesita para terminar en menos de un segundo según el tamaño de la entrada:

    | Tamaño de la entrada | Complejidad esperada |
    |----------------------|----------------------|
    | $n \leq 10$ | $O(n!)$ |
    | $n \leq 20$ | $O(2^n)$ |
    | $n \leq 500$ | $O(n^3)$ |
    | $n \leq 5\,000$ | $O(n^2)$ |
    | $n \leq 10^6$ | $O(n \log n)$ o $O(n)$ |
    | `n` muy grande | $O(\log n)$ o $O(1)$ |

    Por ejemplo, si la entrada tiene $n = 10^5$, un algoritmo $O(n^2)$ realizaría $10^{10}$ operaciones (varias decenas de segundos), mientras que uno $O(n)$ termina al instante.

### $O(1)$: tiempo constante

Un algoritmo de **tiempo constante** realiza siempre el mismo número de operaciones, sin importar el tamaño de la entrada.
Se reconoce cuando el código no tiene ciclos ni recursión que dependan de `n`.

```python
# Acceder a un elemento por índice
valor = arreglo[5]  # (1)!

# Suma de los primeros n números (fórmula de Gauss)
suma = n * (n + 1) // 2  # (2)!

# Verificar si un número es par
if n % 2 == 0:
    pass  # (3)!

# Apilar o desapilar en una pila
pila.append(x)
pila.pop()
```

1. Sin importar que el arreglo tenga 10 o 10 millones de elementos, acceder por índice siempre toma el mismo tiempo.
2. La fórmula calcula la respuesta directamente, sin recorrer ningún elemento.
3. El módulo es una operación aritmética simple: $O(1)$.

### $O(\log n)$: tiempo logarítmico

Un algoritmo **logarítmico** reduce el tamaño del problema a la mitad en cada paso.
Se reconoce porque hay un ciclo o recursión donde el rango se divide (generalmente entre 2) en cada iteración.

```python
# Búsqueda binaria en una lista ordenada: O(log n)
izq, der = 0, len(arreglo) - 1
while izq <= der:
    mid = (izq + der) // 2  # (1)!
    if arreglo[mid] == objetivo:
        break
    elif arreglo[mid] < objetivo:
        izq = mid + 1       # (2)!
    else:
        der = mid - 1

# Calcular la potencia n de un número de forma eficiente: O(log n)
def potencia(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        mitad = potencia(base, exp // 2)  # (3)!
        return mitad * mitad
    return base * potencia(base, exp - 1)
```

1. En cada iteración se calcula el punto medio.
2. El rango de búsqueda se reduce a la mitad: con `n = 1 000 000`, bastan solo 20 iteraciones.
3. El exponente se divide a la mitad en cada llamada recursiva.

!!! note "Por qué $\log_2(1\,000\,000) \approx 20$"
    La búsqueda binaria divide el rango a la mitad en cada paso.
    Para una lista de un millón de elementos, el proceso es $1\,000\,000 \rightarrow 500\,000 \rightarrow 250\,000 \rightarrow ... \rightarrow 1$.
    Eso equivale a apenas 20 divisiones.

### $O(\sqrt{n})$: tiempo de raíz cuadrada

Un algoritmo de **raíz cuadrada** aparece cuando el rango de búsqueda o la cantidad de trabajo se limita a $\sqrt{n}$.
El ejemplo más reconocible es la verificación de números primos. No es necesario probar todos los divisores hasta `n`, sino solo hasta $\sqrt{n}$.

```python
# Verificar si n es primo: O(√n)
def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:  # (1)!
        if n % i == 0:
            return False
        i += 1
    return True

# Encontrar todos los divisores de n: O(√n)
def divisores(n):
    resultado = []
    i = 1
    while i * i <= n:          # (2)!
        if n % i == 0:
            resultado.append(i)
            if i != n // i:
                resultado.append(n // i)
        i += 1
    return sorted(resultado)
```

1. El ciclo se detiene cuando $i^2$ supera a `n`, lo que ocurre después de $\sqrt{n}$ iteraciones.
2. Si `i` divide a `n`, entonces `n // i` también es un divisor. Basta con llegar hasta $\sqrt{n}$ para encontrarlos todos.

### $O(n)$: tiempo lineal

Un algoritmo **lineal** recorre la entrada un número constante de veces.
Se reconoce por un único ciclo que depende de `n`.
Esta es, en general, la mejor complejidad temporal posible para problemas donde es necesario inspeccionar al menos una vez cada elemento.

```python
# Encontrar el máximo de una lista: O(n)
maximo = arreglo[0]
for x in arreglo:  # (1)!
    if x > maximo:
        maximo = x

# Sumar todos los elementos: O(n)
total = sum(arreglo)

# Contar cuántos elementos son positivos: O(n)
cantidad = sum(1 for x in arreglo if x > 0)

# Verificar si un elemento existe (en lista desordenada): O(n)
if objetivo in arreglo:
    pass
```

1. Cada elemento se visita exactamente una vez.

### $O(n \log n)$: tiempo lineal-logarítmico

Esta complejidad aparece típicamente en los **algoritmos de ordenamiento eficientes** y en algoritmos que aplican una operación $O(\log n)$ para cada uno de los `n` elementos.
En Python, `list.sort()` y `sorted()` tienen complejidad $O(n \log n)$.

```python
# Ordenamiento eficiente (Timsort en Python): O(n log n)
arreglo.sort()

# Equivalente sin modificar el arreglo original:
ordenado = sorted(arreglo)

# Aplicar búsqueda binaria para cada elemento de otra lista: O(n log n)
import bisect

arreglo_b.sort()                                  # O(n log n)
for x in arreglo_a:                               # n iteraciones
    pos = bisect.bisect_left(arreglo_b, x)        # O(log n) cada una
    if pos < len(arreglo_b) and arreglo_b[pos] == x:
        print(x, "está en ambas listas")
```

### $O(n^2)$: tiempo cuadrático

Un algoritmo **cuadrático** contiene dos ciclos anidados que dependen de `n`.
Se reconoce inmediatamente por ese patrón de doble ciclo.
Es práctico para $n \leq 5\,000$ aproximadamente.

```python
# Ordenamiento de burbuja: O(n²)
for i in range(n):
    for j in range(n - i - 1):                              # (1)!
        if arreglo[j] > arreglo[j + 1]:
            arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

# Verificar si existe algún par que sume un objetivo: O(n²)
objetivo = 10
for i in range(n):
    for j in range(i + 1, n):
        if arreglo[i] + arreglo[j] == objetivo:
            print(arreglo[i], arreglo[j])

# Construir una matriz de distancias entre todos los pares: O(n²)
distancia = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distancia[i][j] = abs(puntos[i] - puntos[j])
```

1. El ciclo exterior itera `n` veces y el interior hasta `n - i - 1` veces. En total, hay aproximadamente $\frac{n^2}{2}$ comparaciones.

### $O(n^3)$: tiempo cúbico

Un algoritmo **cúbico** contiene tres ciclos anidados que dependen de `n`.
Los ejemplos más reconocibles son la multiplicación de matrices y el algoritmo de Floyd-Warshall para encontrar los caminos más cortos entre todos los pares de nodos.

```python
# Multiplicación de matrices n×n: O(n³)
C = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]  # (1)!

# Floyd-Warshall (caminos mínimos entre todos los pares): O(n³)
for k in range(n):        # (2)!
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

1. Por cada par `(i, j)` de la matriz resultado, se itera sobre todos los `k` elementos intermedios.
2. `k` representa el nodo intermedio que se prueba como punto de paso entre `i` y `j`.

### $O(2^n)$: tiempo exponencial

Un algoritmo **exponencial** aparece cuando se generan o exploran todos los subconjuntos posibles de `n` elementos.
Otro patrón típico es la recursión donde cada llamada genera dos llamadas del mismo tamaño, como ocurre con Fibonacci sin memoización.
Solo es práctico para $n \leq 20$ aproximadamente.

```python
# Fibonacci sin memoización: O(2ⁿ)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)  # (1)!

# Generar todos los subconjuntos de una lista: O(2ⁿ)
def subconjuntos(arreglo, i=0, actual=[]):
    if i == len(arreglo):
        print(actual)
        return
    subconjuntos(arreglo, i + 1, actual + [arreglo[i]])  # (2)!
    subconjuntos(arreglo, i + 1, actual)                  # (3)!
```

1. Cada llamada a `fib(n)` genera dos llamadas más y produce un árbol de llamadas con $2^n$ nodos en el peor caso.
2. Se incluye el elemento en la posición `i` dentro del subconjunto actual.
3. Se excluye el elemento en la posición `i`. En total hay $2^n$ subconjuntos posibles para un arreglo de `n` elementos.

### $O(n!)$: tiempo factorial

Un algoritmo **factorial** aparece cuando se generan o evalúan todas las permutaciones posibles de `n` elementos.
Con `n = 10` hay 3 628 800 permutaciones; con `n = 15` hay más de un billón.
Solo es práctico para $n \leq 10$ aproximadamente.

```python
# Generar todas las permutaciones: O(n!)
from itertools import permutations
for perm in permutations(arreglo):  # (1)!
    print(perm)

# Equivalente recursivo con backtracking: O(n!)
def permutar(arreglo, inicio=0):
    if inicio == len(arreglo):
        print(arreglo[:])
        return
    for i in range(inicio, len(arreglo)):
        arreglo[inicio], arreglo[i] = arreglo[i], arreglo[inicio]  # (2)!
        permutar(arreglo, inicio + 1)
        arreglo[inicio], arreglo[i] = arreglo[i], arreglo[inicio]  # (3)!
```

1. `permutations` genera las `n!` permutaciones del arreglo.
2. Se intercambia el elemento en la posición `inicio` con el elemento en `i`, con lo cual queda fijado un elemento nuevo al inicio.
3. Se deshace el intercambio (backtracking) para probar la siguiente combinación posible.

### Un mismo problema, tres complejidades distintas

El siguiente ejemplo muestra cómo la elección del algoritmo cambia drásticamente el rendimiento.
El problema es el siguiente. Dado un arreglo de `n` números, que pueden ser negativos, hay que encontrar la **suma máxima de un subarreglo contiguo**.

Por ejemplo, en el arreglo `[-1, 2, 4, -3, 5, 2, -5, 2]`, el subarreglo `[2, 4, -3, 5, 2]` produce la suma máxima de **10**.

=== "Algoritmo 1: $O(n^3)$"

    Se prueban todos los subarreglos posibles y se calcula la suma de cada uno desde cero.

    ```python
    def suma_maxima_v1(arreglo):
        n = len(arreglo)
        mejor = 0
        for a in range(n):
            for b in range(a, n):
                suma = 0
                for k in range(a, b + 1):  # (1)!
                    suma += arreglo[k]
                mejor = max(mejor, suma)
        return mejor
    ```

    1. Este tercer ciclo recalcula la suma completa en cada par `(a, b)`, lo que vuelve cúbico el algoritmo.

=== "Algoritmo 2: $O(n^2)$"

    Se mantiene la suma acumulada mientras el extremo derecho avanza, lo que elimina el ciclo interior.

    ```python
    def suma_maxima_v2(arreglo):
        n = len(arreglo)
        mejor = 0
        for a in range(n):
            suma = 0
            for b in range(a, n):  # (1)!
                suma += arreglo[b]
                mejor = max(mejor, suma)
        return mejor
    ```

    1. La suma se extiende en cada paso en lugar de recalcularse desde cero.

=== "Algoritmo 3: $O(n)$ (Algoritmo de Kadane)"

    Se realiza un solo recorrido.
    La clave es la siguiente. La mejor suma que termina en la posición `k` es el elemento solo, o ese elemento sumado a la mejor suma que terminaba en `k - 1`.

    ```python
    def suma_maxima_v3(arreglo):
        mejor = 0
        suma = 0
        for k in range(len(arreglo)):                  # (1)!
            suma = max(arreglo[k], suma + arreglo[k])  # (2)!
            mejor = max(mejor, suma)
        return mejor
    ```

    1. Un único ciclo de izquierda a derecha es suficiente para resolver el problema.
    2. Se decide si conviene extender el subarreglo anterior o empezar uno nuevo desde la posición `k`.

!!! example "Comparación de tiempos reales"

    La siguiente tabla muestra tiempos de ejecución para los tres algoritmos en una computadora moderna.

    | Tamaño `n` | $O(n^3)$ | $O(n^2)$ | $O(n)$ |
    |------------|-------|-------|------|
    | 100 | 0.0 s | 0.0 s | 0.0 s |
    | 1 000 | 0.1 s | 0.0 s | 0.0 s |
    | 10 000 | > 10 s | 0.1 s | 0.0 s |
    | 100 000 | > 10 s | 5.3 s | 0.0 s |
    | 1 000 000 | > 10 s | > 10 s | 0.0 s |

    Solo el Algoritmo 3 puede procesar entradas grandes al instante.
    Elegir el algoritmo correcto no es un detalle menor. Es la diferencia entre una solución que funciona y una que se cuelga.

!!! warning "La notación O oculta los factores constantes"
    Un algoritmo $O(n)$ puede realizar $\frac{n}{2}$ o $5n$ operaciones reales.
    Para entradas pequeñas, un algoritmo $O(n^2)$ con constantes pequeñas puede ser más rápido que uno $O(n)$ con constantes grandes.
    La notación O es una guía para entradas grandes, no una medida exacta del tiempo de ejecución.
