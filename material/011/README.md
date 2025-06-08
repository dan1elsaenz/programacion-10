# Clase 11: Recursión y Estructuras de Datos en C++ (OCI) <!-- omit from toc -->

<details> 
  <summary>Tabla de contenidos</summary>

- [Recursión](#recursión)
  - [Ejemplo 1: Factorial](#ejemplo-1-factorial)
  - [Ejemplo 2: Fibonacci](#ejemplo-2-fibonacci)
  - [Ejemplo 3: Suma de lista](#ejemplo-3-suma-de-lista)
- [Estructuras de datos en C++](#estructuras-de-datos-en-c)
  - [1. Arreglos Dinámicos (`vector`)](#1-arreglos-dinámicos-vector)
  - [2. Cadenas (`string`)](#2-cadenas-string)
  - [3. Conjuntos](#3-conjuntos)
    - [`set`](#set)
    - [`unordered_set`](#unordered_set)
    - [`multiset`](#multiset)
  - [4. Mapas](#4-mapas)
    - [`map`](#map)
    - [`unordered_map`](#unordered_map)
  - [5. Bitset](#5-bitset)
  - [6. Deque](#6-deque)
  - [7. Pila (`stack`)](#7-pila-stack)
  - [8. Cola (`queue`)](#8-cola-queue)
  - [9. Cola de Prioridad](#9-cola-de-prioridad)
  - [Comparación de Usos](#comparación-de-usos)

</details> 

---

## Recursión

La **recursión** ocurre cuando una función se llama a sí misma.
Requiere una **condición base** que finalice la recursión, de lo contrario se produce un error de recursión infinita.

<div align="center">
    <p>
        <img src="img/recursion.png" width="500px" alt="Ejemplo visual de recursión">
    </p>
</div>
<div align="right">
    <a href="https://www.edureka.co/blog/recursion-in-python/">Edureka</a>
</div>

### Ejemplo 1: Factorial
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Ejemplo 2: Fibonacci
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

### Ejemplo 3: Suma de lista
```python
def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])
```

> [!NOTE]
> La recursión es elegante, pero puede ser menos eficiente que un bucle en términos de memoria y tiempo. No es recomendable usar recursión si se pueden generar muchas funciones llamadas.


## Estructuras de datos en C++

### 1. Arreglos Dinámicos (`vector`)

**Uso:** Listas con acceso rápido por índice, inserción al final.

```cpp
vector<int> v = {1, 2, 3};
v.push_back(4); // [1, 2, 3, 4]
cout << v[2];   // 3
```

---

### 2. Cadenas (`string`)

**Uso:** Manipulación de texto con funciones útiles.

```cpp
string a = "hola";
string b = a + " mundo"; // "hola mundo"
cout << b.substr(0, 4);  // "hola"
```

---

### 3. Conjuntos

#### `set`
**Uso:** Elementos únicos, ordenados.

```cpp
set<int> s = {3, 1, 4};
s.insert(2); // {1, 2, 3, 4}
```

#### `unordered_set`
**Uso:** Elementos únicos, sin orden, búsquedas rápidas.

```cpp
unordered_set<int> s = {1, 3, 5};
if (s.count(3)) cout << "Existe";
```

#### `multiset`
**Uso:** Elementos duplicados permitidos.

```cpp
multiset<int> ms;
ms.insert(5); ms.insert(5); // count(5) = 2
```

---

### 4. Mapas

#### `map`
**Uso:** Claves ordenadas.

```cpp
map<string, int> m;
m["clave"] = 5;
cout << m["clave"]; // 5
```

#### `unordered_map`

**Uso:** Claves sin orden, búsqueda rápida.

```cpp
unordered_map<string, int> m;
m["banana"] = 7;
```

---

### 5. Bitset

**Uso:** Arreglo compacto de bits, ideal para conjuntos pequeños.

```cpp
bitset<8> b(string("10101010"));
cout << b.count(); // 4
```

---

### 6. Deque

**Uso:** Acceso eficiente al frente y fondo.

```cpp
deque<int> d;
d.push_front(3); d.push_back(5); // [3, 5]
d.pop_front(); // [5]
```

---

### 7. Pila (`stack`)

**Uso:** Último en entrar, primero en salir (LIFO).

```cpp
stack<int> s;
s.push(1); s.push(2);
s.pop(); // top = 1
```

---

### 8. Cola (`queue`)

**Uso:** Primero en entrar, primero en salir (FIFO).

```cpp
queue<int> q;
q.push(1); q.push(2);
q.pop(); // front = 2
```

---

### 9. Cola de Prioridad

**Uso:** Recuperar y eliminar el mayor (por defecto) o menor.

```cpp
priority_queue<int> pq;
pq.push(4); pq.push(10);
cout << pq.top(); // 10
```

---

### Comparación de Usos

| Necesidad                        | Estructura recomendada        |
|----------------------------------|-------------------------------|
| Acceso por índice                | `vector`                      |
| Verificar pertenencia            | `unordered_set`              |
| Elementos únicos ordenados       | `set`                         |
| Asociar claves a valores         | `map` / `unordered_map`      |
| LIFO / FIFO                      | `stack` / `queue`            |
| Recuperar máximo/mínimo rápido  | `priority_queue`             |
| Representar bits                 | `bitset`                      |
| Acceso a ambos extremos          | `deque`                       |

