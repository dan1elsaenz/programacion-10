# Programación Dinámica <!-- omit from toc -->

<details> 
  <summary>Tabla de contenidos</summary>

- [¿Qué es la programación dinámica?](#qué-es-la-programación-dinámica)
- [¿Cuándo se debe usar programación dinámica?](#cuándo-se-debe-usar-programación-dinámica)
- [Tipos de programación dinámica](#tipos-de-programación-dinámica)
- [Ejemplo: Fibonacci](#ejemplo-fibonacci)
  - [1. Memoización automática con `@lru_cache`](#1-memoización-automática-con-lru_cache)
  - [2. Memoización manual (_Top-Down_)](#2-memoización-manual-top-down)
  - [3. Tabulación (_Bottom-Up_)](#3-tabulación-bottom-up)
- [Ejemplo: Mochila 0/1](#ejemplo-mochila-01)
- [Ejemplo: Longest Common Subsequence (LCS)](#ejemplo-longest-common-subsequence-lcs)

</details>

---

## ¿Qué es la programación dinámica?

La **Programación Dinámica (DP)** es una técnica de diseño algorítmico utilizada para resolver **problemas que pueden dividirse en subproblemas más pequeños**, donde estos subproblemas **se repiten una y otra vez**.

En muchos algoritmos (como la recursión directa), se **vuelven a calcular los mismos resultados múltiples veces**, lo cual puede provocar un aumento exponencial de tiempo de ejecución.
La programación dinámica resuelve esta ineficiencia guardando los resultados de subproblemas ya resueltos, para evitar recomputaciones innecesarias.

## ¿Cuándo se debe usar programación dinámica?

- Cuando el problema presenta **subestructura óptima**, es decir, se puede construir una solución óptima a partir de soluciones óptimas de subproblemas.
- Cuando existe **superposición de subproblemas**, es decir, se resuelven los mismos subproblemas muchas veces.
- Son comunes en problemas de conteo, caminos óptimos, secuencias, subconjuntos, entre otros.

## Tipos de programación dinámica

| Característica      | Top-Down (Memoización)                            | Bottom-Up (Tabulación)                             |
| ------------------- | ------------------------------------------------- | -------------------------------------------------- |
| Estrategia          | Divide y vencerás con recursividad                | Construcción iterativa desde los casos base        |
| Implementación      | Recursiva + almacenamiento de resultados (_memo_) | Iterativa usando una tabla o vector                |
| Desventaja          | Consume pila (riesgo de stack overflow)           | Puede ser más difícil de escribir                  |
| Orden de resolución | Del problema original hacia los subproblemas      | De los subproblemas más pequeños hacia el original |

---

## Ejemplo: Fibonacci

A continuación se presentan tres formas de resolver el problema de Fibonacci utilizando Programación Dinámica:

- Memoización automática
- Memoización manual (_top-down_)
- Tabulación iterativa (_bottom-up_).

### 1. Memoización automática con `@lru_cache`

```python
from functools import lru_cache

# Decorador que almacena automáticamente los resultados previos
@lru_cache(maxsize=None)
def fibonacci(n):
    # Caso base: fib(0) = 0
    if n == 0:
        return 0
    # Caso base: fib(1) = 1
    if n == 1:
        return 1
    # Llamadas recursivas optimizadas por caché
    print(f"Calculando fib({n})")
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**Explicación del algoritmo:**

- Se utiliza el decorador `@lru_cache` para guardar automáticamente los resultados previos.
- Al hacer una llamada con un valor ya calculado, se devuelve directamente sin volver a ejecutar la función.
- Evita recomputaciones y reduce la complejidad de tiempo de exponencial a lineal.
- Es práctico y conciso, ideal para prototipos o problemas sencillos.

### 2. Memoización manual (_Top-Down_)

```python
def fibonacci_top_down(n, memo=None):
    # Se crea el diccionario memo solo en la primera llamada
    if memo is None:
        memo = {}

    # Reutilizar resultado ya calculado
    if n in memo:
        return memo[n]

    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Guardar el resultado calculado en memo
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    return memo[n]
```

**Explicación del algoritmo:**

- Utiliza recursividad con un diccionario explícito (`memo`) para guardar subresultados.
- Solo se calcula cada valor de Fibonacci una vez.
- Se puede adaptar fácilmente a problemas con múltiples parámetros.
- Requiere un poco más de código, pero da mayor control.

### 3. Tabulación (_Bottom-Up_)

```python
def fibonacci_bottom_up(n):
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Inicializar la tabla con valores base
    fib = [0] * (n + 1)
    fib[1] = 1

    # Llenar la tabla de abajo hacia arriba
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]
```

**Explicación del algoritmo:**

- Se construye una lista `fib` para almacenar todos los resultados desde 0 hasta `n`.
- Se inicializan los casos base (`fib[0] = 0`, `fib[1] = 1`).
- Cada nuevo valor se calcula iterativamente a partir de los dos anteriores.
- No usa recursión, por lo que es más seguro para `n` grandes y evita desbordamientos de pila.

---

## Ejemplo: Mochila 0/1

Dado un conjunto de objetos, cada uno con un **peso** y un **valor**, y una mochila con una capacidad máxima, determinar el **valor máximo** que se puede obtener **sin exceder la capacidad**. Cada objeto se puede tomar **una sola vez**.

```python
def mochila(pesos, valores, capacidad):
    n = len(pesos)  # Número de objetos

    # Crear una tabla (n+1) x (capacidad+1) inicializada en 0
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    # Llenar la tabla iterativamente
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i - 1] <= w:
                # Opción 1: no tomar el objeto
                # Opción 2: tomar el objeto y sumar su valor
                dp[i][w] = max(
                    dp[i - 1][w],
                    valores[i - 1] + dp[i - 1][w - pesos[i - 1]]
                )
            else:
                # No cabe el objeto, se mantiene el valor anterior
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidad]

# Ejemplo de prueba
pesos = [1, 3, 4]
valores = [15, 20, 30]
capacidad = 4
print(mochila(pesos, valores, capacidad))  # Salida esperada: 35
```

**Explicación del algoritmo:**

- Se usa una tabla `dp[i][w]` donde:
  - `i` representa el número de objetos considerados.
  - `w` representa la capacidad actual.
- Para cada objeto y para cada capacidad:
  - Si el objeto **cabe**, se elige entre tomarlo o no, según qué opción da mayor valor.
  - Si **no cabe**, se mantiene el valor anterior.
- La respuesta está en `dp[n][capacidad]`, usando todos los objetos disponibles.

---

## Ejemplo: Longest Common Subsequence (LCS)

Dadas dos cadenas, encontrar la longitud de la subsecuencia común más larga que aparece en ambas. Una subsecuencia es una secuencia que aparece en el mismo orden, pero no necesariamente de forma contigua.

```python
def lcs(cadena1, cadena2):
    n = len(cadena1)
    m = len(cadena2)

    # Crear una tabla (n+1) x (m+1) inicializada en 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Llenar la tabla comparando caracteres
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if cadena1[i - 1] == cadena2[j - 1]:
                # Si los caracteres coinciden, se extiende la subsecuencia
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Si no coinciden, se toma el máximo de excluir uno u otro
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

# Ejemplo de prueba
cadena1 = "abcde"
cadena2 = "ace"
print(lcs(cadena1, cadena2))  # Salida esperada: 3
```

**Explicación del algoritmo:**

- Se usa una tabla `dp[i][j]` donde:
  - `i` representa los primeros `i` caracteres de `cadena1`.
  - `j` representa los primeros `j` caracteres de `cadena2`.
- Si los caracteres coinciden, se **extiende la subsecuencia**.
- Si no, se elige el mejor resultado entre:
  - Excluir el carácter actual de `cadena1`.
  - Excluir el carácter actual de `cadena2`.
- La respuesta final se encuentra en `dp[n][m]`, que representa la longitud del LCS entre ambas cadenas completas.

---