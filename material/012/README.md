# Clase 12: Algoritmos sobre números para la OCI

<details> 
  <summary>Tabla de contenidos</summary>

</details> 


---

## 1. Suma Máxima de un Subarreglo (Algoritmo de Kadane)

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

---

## 2. Mínimo y Máximo en un Arreglo

### Lógica:

Se puede encontrar el valor mínimo o máximo directamente, o también identificar en qué índice se encuentra.
Ambos enfoques recorren el arreglo una sola vez.

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

## 3. Sumas de Prefijos

### Lógica lineal:

Se calcula la suma acumulada de izquierda a derecha.

```python
prefijos = [0] * len(numeros)
prefijos[0] = numeros[0]
for i in range(1, len(numeros)):
    prefijos[i] = prefijos[i-1] + numeros[i]
```

### Lógica bidimensional:

Permite calcular la suma de submatrices dentro de una matriz original.

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

# Consulta entre (f1, c1) y (f2, c2)
def suma_submatriz(f1, c1, f2, c2):
    suma = p[f2][c2]
    if f1 > 0: suma -= p[f1-1][c2]
    if c1 > 0: suma -= p[f2][c1-1]
    if f1 > 0 and c1 > 0: suma += p[f1-1][c1-1]
    return suma
```

---

## 4. Búsqueda Binaria

### Lógica:

Funciona únicamente sobre listas ordenadas. Se puede implementar de forma iterativa o recursiva.

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

## 5. Cálculo de Distancia entre Puntos

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

## 6. Cálculo de Divisores

### Lógica:

Para encontrar todos los divisores de un número `n`, se prueba cada número `i` desde 1 hasta √n. Si divide a `n`, se guarda tanto `i` como `n // i`.

### Código:

```python
from math import sqrt

def divisores(n):
    resultado = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            resultado.add(i)
            resultado.add(n // i)
    return sorted(resultado)
```

---

## 7. Criba de Eratóstenes

### Lógica:

Permite encontrar todos los números primos menores o iguales a un número `n`. Se parte de una lista donde todos son considerados primos. Luego, se eliminan los múltiplos de cada número primo empezando desde 2.

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

