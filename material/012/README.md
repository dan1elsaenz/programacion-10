# Clase 12: Algoritmos sobre números (OCI)  <!-- omit from toc -->

<details>
  <summary>Tabla de contenidos</summary>

- [1. Mínimo y Máximo en un Arreglo](#1-mínimo-y-máximo-en-un-arreglo)
  - [Lógica:](#lógica)
  - [Código por elemento:](#código-por-elemento)
  - [Código por índice:](#código-por-índice)
- [2. Sumas de Prefijos](#2-sumas-de-prefijos)
  - [Lógica lineal:](#lógica-lineal)
  - [Lógica bidimensional:](#lógica-bidimensional)
- [3. Búsqueda Binaria](#3-búsqueda-binaria)
  - [Lógica:](#lógica-1)
  - [Iterativa:](#iterativa)
  - [Recursiva:](#recursiva)
- [4. Algoritmo de Euclides](#4-algoritmo-de-euclides)
  - [Lógica:](#lógica-2)
- [5. Exponenciación Binaria](#5-exponenciación-binaria)
  - [Lógica:](#lógica-3)
- [6. Test de Primalidad O(√n)](#6-test-de-primalidad-on)
  - [Lógica:](#lógica-4)
- [7. Factorización](#7-factorización)
  - [Lógica:](#lógica-5)
- [8. Criba de Eratóstenes](#8-criba-de-eratóstenes)
  - [Lógica:](#lógica-6)
  - [Parte 1: Generar la lista de primos](#parte-1-generar-la-lista-de-primos)
  - [Parte 2: Verificar si un número es primo con criba](#parte-2-verificar-si-un-número-es-primo-con-criba)
- [9. Cálculo de distancia entre puntos](#9-cálculo-de-distancia-entre-puntos)
  - [Lógica:](#lógica-7)
  - [Código:](#código)
- [10. Suma Máxima de un Subarreglo (Algoritmo de Kadane)](#10-suma-máxima-de-un-subarreglo-algoritmo-de-kadane)
  - [Lógica:](#lógica-8)
  - [Código:](#código-1)

</details>

---

## 1. Mínimo y Máximo en un Arreglo

### Lógica:

Buscar el valor mínimo o máximo en un arreglo consiste en recorrer todos los elementos y comparar cada uno con el actual mínimo o máximo registrado.

Al inicio, se toma como referencia el primer elemento del arreglo.
A medida que se avanza, si se encuentra un valor menor al mínimo registrado, se actualiza.
De igual forma con el máximo.
Esta operación es útil para encontrar extremos en conjuntos de datos, como temperaturas más altas, precios mínimos, entre otros.
El algoritmo es lineal porque analiza todos los elementos una sola vez.

### Código por elemento:

```python
minimo = maximo = arreglo[0]

for valor in arreglo:
    if valor < minimo:
        minimo = valor
    if valor > maximo:
        maximo = valor
```

### Código por índice:

```python
indice_min = indice_max = 0
for i in range(1, len(arreglo)):
    if arreglo[i] < arreglo[indice_min]:
        indice_min = i
    if arreglo[i] > arreglo[indice_max]:
        indice_max = i
```

---

## 2. Sumas de Prefijos

### Lógica lineal:

La suma de prefijos es una técnica que permite calcular rápidamente la suma de cualquier subarreglo en tiempo constante, una vez se ha hecho un preprocesamiento en tiempo lineal.

Consiste en crear un arreglo auxiliar donde cada posición guarda la suma acumulada desde el inicio hasta esa posición.
Esto es útil para responder muchas consultas de suma de rangos en arreglos de forma eficiente.

```python
prefijos = [0] * len(numeros)
prefijos[0] = numeros[0]
for i in range(1, len(numeros)):
    prefijos[i] = prefijos[i-1] + numeros[i]
```

### Lógica bidimensional:

En el caso de matrices, la suma de prefijos bidimensional extiende esta idea para permitir obtener la suma de cualquier submatriz.

Se usa una matriz acumulada donde cada celda representa la suma de la submatriz desde (0,0) hasta esa celda.
Esta técnica es muy poderosa en procesamiento de imágenes o análisis de datos en cuadrículas.

```python
filas, columnas = len(matriz), len(matriz[0])
p = [[0]*columnas for _ in range(filas)]

# Primera fila y columna
p[0][0] = matriz[0][0]
for i in range(1, filas):
    p[i][0] = p[i-1][0] + matriz[i][0]
for j in range(1, columnas):
    p[0][j] = p[0][j-1] + matriz[0][j]

# Resto de la matriz
for i in range(1, filas):
    for j in range(1, columnas):
        p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + matriz[i][j]

def suma_submatriz(f1, c1, f2, c2):
    suma = p[f2][c2]
    if f1 > 0: suma -= p[f1-1][c2]
    if c1 > 0: suma -= p[f2][c1-1]
    if f1 > 0 and c1 > 0: suma += p[f1-1][c1-1]
    return suma
```

---

## 3. Búsqueda Binaria

### Lógica:

La búsqueda binaria es una técnica eficiente para encontrar un elemento dentro de una lista ordenada.

En lugar de revisar todos los elementos, divide el arreglo a la mitad y decide en qué mitad continuar la búsqueda según si el objetivo es menor o mayor que el valor medio.
Este enfoque reduce el tamaño del problema a la mitad en cada paso, lo cual da una complejidad logarítmica O(log n).
Es fundamental que el arreglo esté ordenado para que esta estrategia funcione.

### Iterativa:

```python
def busqueda_binaria(arr, objetivo):
    izq, der = 0, len(arr) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
```

### Recursiva:

```python
def busqueda_binaria_rec(arr, objetivo, izq, der):
    if izq > der:
        return -1
    medio = (izq + der) // 2
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_rec(arr, objetivo, medio + 1, der)
    else:
        return busqueda_binaria_rec(arr, objetivo, izq, medio - 1)
```

---

## 4. Algoritmo de Euclides

### Lógica:

El algoritmo de Euclides es un método clásico para encontrar el máximo común divisor (MCD) de dos números enteros. Se basa en el principio de que el MCD de dos números no cambia si el número mayor se reemplaza por su diferencia con el menor. La versión moderna usa el residuo de la división: `gcd(a, b) = gcd(b, a % b)`. Este proceso se repite hasta que el residuo sea cero, y el último valor distinto de cero es el MCD. Es un algoritmo muy eficiente, con complejidad logarítmica.

```python
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

---

## 5. Exponenciación Binaria

### Lógica:

La exponenciación binaria permite calcular potencias de forma muy eficiente, especialmente en contextos donde el exponente es muy grande, como en criptografía o teoría de números. En lugar de multiplicar `a` por sí mismo `b` veces, divide el problema usando que `a^b = (a^(b//2))^2` si `b` es par, o `a * a^(b-1)` si es impar. Esta estrategia reduce el número de multiplicaciones a O(log b), aprovechando la representación binaria del exponente.

```python
def exponenciacion_binaria(a, b, mod):
    resultado = 1
    a %= mod
    while b:
        if b % 2:
            resultado = (resultado * a) % mod
        a = (a * a) % mod
        b //= 2
    return resultado
```

---

## 6. Test de Primalidad O(√n)

### Lógica:

Un número `n` es primo si tiene exactamente dos divisores: 1 y él mismo. Para verificar esto, basta con probar si `n` es divisible por algún número entre 2 y √n. Si `n` tiene un divisor en ese rango, no es primo. Este método es eficiente porque cualquier divisor mayor que √n implicaría uno menor que ya se habría encontrado.

```python
from math import isqrt

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
```

---

## 7. Factorización

### Lógica:

La factorización consiste en descomponer un número en sus factores primos, es decir, en los números primos que multiplicados entre sí dan como resultado el número original.

El método más común es dividir el número `n` por todos los posibles divisores desde 2 hasta $$\sqrt{n}$$, y repetir mientras sea divisible.
Si al final queda un número mayor que 1, también es primo. Esta técnica se usa en criptografía y análisis de números.

```python
from math import isqrt

def factorizar(n):
    resultado = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            resultado.add(i)
            resultado.add(n // i)
    return sorted(resultado)
```

---

## 8. Criba de Eratóstenes

### Lógica:

La Criba de Eratóstenes es un algoritmo antiguo y muy eficiente para encontrar todos los números primos hasta un número dado `n`.

Permite encontrar todos los números primos menores o iguales a un número `n`.
Se parte de una lista donde todos son considerados primos.
Luego, se eliminan los múltiplos de cada número primo empezando desde 2.

### Parte 1: Generar la lista de primos

```python
def criba_lista(n):
    lista_criba = [0] * (n - 1)  # de 2 a n
    for i in range(2, n + 1):
        if lista_criba[i - 2] != 0:
            continue
        for j in range(2 * i, n + 1, i):
            lista_criba[j - 2] = i
    print(lista_criba)  # 0 si es primo, o su menor divisor primo
```

### Parte 2: Verificar si un número es primo con criba

```python
def criba_verificar_primo(n):
    es_primo = [True for _ in range(n + 1)]
    menor_primo = [-1 for _ in range(n + 1)]
    es_primo[0] = es_primo[1] = False
    for i in range(2, n + 1):
        if es_primo[i]:
            for j in range(i * i, n + 1, i):
                es_primo[j] = False
                if menor_primo[j] == -1:
                    menor_primo[j] = i
    print(es_primo[n], menor_primo[n])
```

---

## 9. Cálculo de distancia entre puntos

### Lógica:

La distancia entre dos puntos en el plano se calcula con el teorema de Pitágoras: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

### Código:

```python
from math import sqrt

def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

---

## 10. Suma Máxima de un Subarreglo (Algoritmo de Kadane)

### Lógica:

El algoritmo de Kadane permite encontrar la suma más alta posible de una secuencia continua dentro de un arreglo.

### Código:

```python
def algoritmo_kadane(arr):
    max_actual = max_total = arr[0]
    for num in arr[1:]:
        max_actual = max(num, max_actual + num)
        max_total = max(max_total, max_actual)
    return max_total
```

