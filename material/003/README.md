# Clase 3: Listas y Bucles `for` en Python

**Tabla de contenidos**

- [Clase 3: Listas y Bucles `for` en Python](#clase-3-listas-y-bucles-for-en-python)
  - [1. Listas en Python](#1-listas-en-python)
    - [1.1 Concepto y Creación de Listas](#11-concepto-y-creación-de-listas)
    - [1.2 Uso del Operador `in`](#12-uso-del-operador-in)
      - [Ejemplo en listas](#ejemplo-en-listas)
      - [Ejemplo en strings](#ejemplo-en-strings)
    - [1.3 Propiedades de las Listas](#13-propiedades-de-las-listas)
    - [1.4 Largo de una Lista](#14-largo-de-una-lista)
    - [1.5 Acceso y Modificación de Elementos](#15-acceso-y-modificación-de-elementos)
    - [1.6 Métodos para Modificar Listas](#16-métodos-para-modificar-listas)
      - [1.6.1 Agregar Elementos](#161-agregar-elementos)
        - [`append(x)`: Agregar un elemento al final de la lista](#appendx-agregar-un-elemento-al-final-de-la-lista)
        - [`insert(i, x)`: Insertar un elemento en una posición específica](#inserti-x-insertar-un-elemento-en-una-posición-específica)
      - [1.6.2 Eliminar Elementos](#162-eliminar-elementos)
        - [`remove(x)`: Eliminar la primera ocurrencia de un elemento](#removex-eliminar-la-primera-ocurrencia-de-un-elemento)
        - [`pop(i)`: Eliminar un elemento en una posición específica](#popi-eliminar-un-elemento-en-una-posición-específica)
      - [1.6.3 Ordenar y Revertir Listas](#163-ordenar-y-revertir-listas)
        - [`sort()`: Ordenar la lista en orden ascendente](#sort-ordenar-la-lista-en-orden-ascendente)
        - [`reverse()`: Invertir el orden de los elementos de la lista](#reverse-invertir-el-orden-de-los-elementos-de-la-lista)
      - [1.6.4 Copiar y Unir Listas](#164-copiar-y-unir-listas)
        - [`copy()`: Crear una copia de la lista](#copy-crear-una-copia-de-la-lista)
        - [`extend(iterable)`: Agregar los elementos de otro iterable](#extenditerable-agregar-los-elementos-de-otro-iterable)
  - [2. Bucles `for` en Python](#2-bucles-for-en-python)
    - [2.1 Iteración sobre Listas y Strings](#21-iteración-sobre-listas-y-strings)
    - [2.2 Iteración con `range()`](#22-iteración-con-range)
    - [2.3 Uso de `break`, `continue`, `pass`](#23-uso-de-break-continue-pass)
    - [2.4 Bucles `for` Anidados](#24-bucles-for-anidados)
    - [2.5 `else` en un `for`](#25-else-en-un-for)

## 1. Listas en Python

### 1.1 Concepto y Creación de Listas

Una lista es una estructura de datos en Python que permite almacenar múltiples valores en un solo contenedor. A diferencia de otros tipos de datos, las listas pueden contener elementos de diferentes tipos y permiten duplicados.

Las listas son útiles cuando se necesita manejar colecciones de datos, como nombres de usuarios, precios de productos o resultados de cálculos.

Se pueden crear listas de dos maneras:

```python
# Usando corchetes []
mi_lista = [1, 2, 3, 4, 5]

# Usando list()
otra_lista = list(("rojo", "verde", "azul"))
```

Ambas formas crean una lista, aunque `list()` también puede usarse para convertir otros tipos de datos en listas.

### 1.2 Uso del Operador `in`

El operador `in` permite verificar si un elemento se encuentra dentro de una lista o string. Es una forma sencilla y eficiente de comprobar pertenencia.

#### Ejemplo en listas

```python
frutas = ["manzana", "banana", "cereza"]
if "banana" in frutas:
    print("La banana está en la lista de frutas.")
```

#### Ejemplo en strings

```python
mensaje = "Bienvenidos a la clase de Python"
if "Python" in mensaje:
    print("El mensaje menciona Python.")
```

Este operador se usa frecuentemente en estructuras de control como `if`, y también en bucles `for` para iterar sobre listas o strings.

### 1.3 Propiedades de las Listas

Las listas en Python tienen varias características clave:

- **Mutabilidad**: Se pueden modificar después de su creación.
- **Permiten duplicados**: Se pueden almacenar valores repetidos.
- **Almacenan diferentes tipos de datos**: Una lista puede contener elementos de distintos tipos.

Ejemplo:

```python
lista_mixta = [10, "Python", 3.14, True]
print(lista_mixta)
```

Esta característica de aceptar múltiples tipos de datos hace que las listas sean extremadamente flexibles.

### 1.4 Largo de una Lista

Se usa la función `len()` para obtener la cantidad de elementos en una lista. También se puede utilizar para contar caracteres en un string.

```python
lista = [1, 2, 3, 4, 5]
print(len(lista))  # Salida: 5

cadena = "Hola mundo"
print(len(cadena))  # Salida: 10
```

Esta función es útil para determinar la cantidad de elementos presentes en una colección de datos.

### 1.5 Acceso y Modificación de Elementos

Los elementos de una lista se acceden mediante índices, comenzando desde `0`.

```python
mi_lista = ["manzana", "banana", "cereza"]
print(mi_lista[0])  # manzana

mi_lista[1] = "uva"
print(mi_lista)  # ['manzana', 'uva', 'cereza']
```

También es posible acceder a elementos desde el final usando índices negativos:

```python
print(mi_lista[-1])  # Último elemento: cereza
```

### 1.6 Métodos para Modificar Listas

#### 1.6.1 Agregar Elementos

##### `append(x)`: Agregar un elemento al final de la lista

Agrega un elemento `x` al final de la lista.

```python
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)  # [1, 2, 3, 4]
```

##### `insert(i, x)`: Insertar un elemento en una posición específica

Inserta un elemento en el índice `i` y con el valor de `x`.

```python
colores = ["rojo", "azul", "verde"]
colores.insert(1, "amarillo")
print(colores)  # ['rojo', 'amarillo', 'azul', 'verde']
```

#### 1.6.2 Eliminar Elementos

##### `remove(x)`: Eliminar la primera ocurrencia de un elemento

Elimina un elemento basado en su valor `x`.

```python
frutas = ["manzana", "banana", "cereza", "banana"]
frutas.remove("banana")
print(frutas)  # ['manzana', 'cereza', 'banana']
```

##### `pop(i)`: Eliminar un elemento en una posición específica

Elimina un elemento basado en su índice en la lista.

```python
numeros = [10, 20, 30, 40]
ultimo = numeros.pop()
print(numeros)  # [10, 20, 30]
print("Elemento eliminado:", ultimo)  # 40
```

#### 1.6.3 Ordenar y Revertir Listas

##### `sort()`: Ordenar la lista en orden ascendente

```python
numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()
print(numeros)  # [1, 1, 3, 4, 5, 9]
```

##### `reverse()`: Invertir el orden de los elementos de la lista

```python
letras = ["a", "b", "c", "d"]
letras.reverse()
print(letras)  # ['d', 'c', 'b', 'a']
```

#### 1.6.4 Copiar y Unir Listas

##### `copy()`: Crear una copia de la lista

```python
original = [1, 2, 3]
copia = original.copy()
print(copia)  # [1, 2, 3]
```

##### `extend(iterable)`: Agregar los elementos de otro iterable

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]
```

Estos métodos permiten modificar listas de manera eficiente sin necesidad de reescribir todos los valores manualmente.

