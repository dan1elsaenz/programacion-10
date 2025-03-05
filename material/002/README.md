# Clase 2

**Tabla de contenidos**
- [Clase 2](#clase-2)
  - [1. Operadores en Python](#1-operadores-en-python)
    - [Operadores Matemáticos](#operadores-matemáticos)
    - [Operadores de Asignación](#operadores-de-asignación)
    - [Operadores Relacionales](#operadores-relacionales)
    - [Operadores Lógicos](#operadores-lógicos)
  - [2. Uso de Strings en Python](#2-uso-de-strings-en-python)
    - [Métodos de Strings](#métodos-de-strings)
    - [Slicing de Strings](#slicing-de-strings)
    - [Caracteres de Escape en Strings](#caracteres-de-escape-en-strings)
  - [3. Valores Booleanos en Python](#3-valores-booleanos-en-python)
  - [4. Estructura de Control `if-elif-else`](#4-estructura-de-control-if-elif-else)
    - [¿Qué es una estructura condicional?](#qué-es-una-estructura-condicional)
    - [Sintaxis básica de `if`](#sintaxis-básica-de-if)
    - [Uso de `elif` y `else`](#uso-de-elif-y-else)
    - [`if` anidado](#if-anidado)
    - [Operador ternario](#operador-ternario)


## 1. Operadores en Python

Los operadores en Python permiten realizar diversas operaciones, desde cálculos matemáticos hasta comparaciones lógicas. Son fundamentales para la programación, puesto que permiten manipular datos de manera efectiva.

### Operadores Matemáticos

Los operadores matemáticos permiten realizar cálculos entre valores numéricos. Python maneja automáticamente los tipos de datos adecuados en las operaciones.

| Operador | Descripción        | Ejemplo (`a = 10, b = 3`) | Resultado |
|----------|--------------------|---------------------------|-----------|
| `+`      | Suma               | `a + b`                   | `13`      |
| `-`      | Resta              | `a - b`                   | `7`       |
| `*`      | Multiplicación     | `a * b`                   | `30`      |
| `/`      | División (decimal) | `a / b`                   | `3.3333`  |
| `//`     | División entera    | `a // b`                  | `3`       |
| `%`      | Módulo (residuo)   | `a % b`                   | `1`       |
| `**`     | Potencia           | `a ** b`                  | `1000`    |

Python respeta la jerarquía de operaciones matemáticas. Primero ejecuta las potencias, luego multiplicaciones y divisiones, y por último sumas y restas.

**Ejemplo de las operaciones matemáticas:**

```python
a = 10
b = 3

print(a + b)   # Suma: 13
print(a - b)   # Resta: 7
print(a * b)   # Multiplicación: 30
print(a / b)   # División: 3.3333
print(a // b)  # División entera: 3
print(a % b)   # Módulo: 1
print(a ** b)  # Potencia: 1000
```

### Operadores de Asignación

Los operadores de asignación permiten modificar el valor de una variable de manera eficiente.
En lugar de escribir expresiones completas como `x = x + 5`, se puede utilizar `x += 5` para reducir la complejidad del código.

| Operador | Descripción                       | Ejemplo (`a = 5`) | Equivalente   |
|----------|-----------------------------------|-------------------|---------------|
| `=`      | Asigna un valor                   | `a = 5`           | `a = 5`       |
| `+=`     | Suma y asigna                     | `a += 3`          | `a = a + 3`   |
| `-=`     | Resta y asigna                    | `a -= 2`          | `a = a - 2`   |
| `*=`     | Multiplica y asigna               | `a *= 4`          | `a = a * 4`   |
| `/=`     | Divide y asigna                   | `a /= 2`          | `a = a / 2`   |
| `//=`    | División entera y asigna          | `a //= 3`         | `a = a // 3`  |
| `%=`     | Módulo y asigna                   | `a %= 2`          | `a = a % 2`   |
| `**=`    | Exponente y asigna                | `a **= 3`         | `a = a ** 3`  |

### Operadores Relacionales

Estos operadores permiten comparar valores y devuelven un resultado booleano (`True` o `False`).

| Operador | Descripción       | Ejemplo (`a = 10, b = 3`) | Resultado |
|----------|-------------------|---------------------------|-----------|
| `==`     | Igualdad          | `a == b`                  | `False`   |
| `!=`     | Diferente         | `a != b`                  | `True`    |
| `>`      | Mayor que         | `a > b`                   | `True`    |
| `<`      | Menor que         | `a < b`                   | `False`   |
| `>=`     | Mayor o igual que | `a >= b`                  | `True`    |
| `<=`     | Menor o igual que | `a <= b`                  | `False`   |

### Operadores Lógicos

Se usan para combinar expresiones booleanas.

| Operador | Descripción                      | Ejemplo (`a = True, b = False`) | Resultado |
|----------|----------------------------------|---------------------------------|-----------|
| `and`    | `True` si ambas son `True`       | `a and b`                       | `False`   |
| `or`     | `True` si al menos una es `True` | `a or b`                        | `True`    |
| `not`    | Invierte el valor                | `not a`                         | `False`   |

## 2. Uso de Strings en Python

Los strings en Python son secuencias de caracteres y ofrecen una gran variedad de métodos para manipularlos. A continuación, se explican algunas de sus principales funcionalidades.

### Métodos de Strings

Python proporciona diversos métodos para trabajar con cadenas de texto. Se presenta una tabla con los métodos más comunes:

| Método                | Descripción                                                                   |
|-----------------------|-------------------------------------------------------------------------------|
| `capitalize()`        | Convierte el primer carácter en mayúscula.                                    |
| `casefold()`          | Convierte el string a minúsculas (más agresivo que `lower()`).                |
| `center(width)`       | Centra el string dentro de un ancho especificado.                             |
| `count(substring)`    | Devuelve el número de veces que aparece un valor especificado.                |
| `encode()`            | Codifica el string a una versión específica.                                  |
| `endswith(suffix)`    | Devuelve `True` si la cadena termina con el valor especificado.               |
| `expandtabs(size)`    | Establece el tamaño del tabulador en el string.                               |
| `find(substring)`     | Busca una subcadena y devuelve la posición donde se encontró por primera vez. |
| `format()`            | Formatea valores dentro de un string.                                         |
| `index(substring)`    | Similar a `find()`, pero genera error si no se encuentra.                     |
| `isalnum()`           | Devuelve `True` si todos los caracteres son alfanuméricos.                    |
| `isalpha()`           | Devuelve `True` si todos los caracteres son letras.                           |
| `isdigit()`           | Devuelve `True` si todos los caracteres son números.                          |
| `islower()`           | Devuelve `True` si todos los caracteres están en minúscula.                   |
| `isnumeric()`         | Devuelve `True` si el string solo contiene números.                           |
| `isspace()`           | Devuelve `True` si todos los caracteres son espacios en blanco.               |
| `join(iterable)`      | Une elementos de un iterable con la cadena como separador.                    |
| `replace(old, new)`   | Reemplaza un valor por otro dentro de la cadena.                              |
| `split(separator)`    | Divide la cadena en una lista, usando un separador específico.                |
| `startswith(prefix)`  | Devuelve `True` si el string comienza con el valor especificado.              |
| `strip()`             | Elimina espacios en blanco al inicio y al final de la cadena.                 |
| `upper()`             | Convierte todos los caracteres a mayúsculas.                                  |
| `zfill(width)`        | Rellena la cadena con ceros a la izquierda hasta el ancho especificado.       |

La sintaxis para ejecutar un método sobre un string es la siguiente:

```plaintext
[string].[método]([parámetros])
```

**Ejemplo de uso de métodos comunes:**

```python
texto = "hola mundo"
print(texto.capitalize())  # Hola mundo
print(texto.upper())       # HOLA MUNDO
print(texto.replace("mundo", "Python"))  # hola Python
```

### Slicing de Strings

El slicing permite extraer partes específicas de un string mediante índices.

Es importante mencionar que los strings (cadenas de caracteres) permiten acceder a cada uno de sus caracteres por medio de la posición o índice en que se encuentran en el string.
Esta numeración comienza a partir de 0, el cual corresponde al primer caracter.

| Expresión     | Descripción                                                 |
|---------------|-------------------------------------------------------------|
| `cadena[0:n]` | Extrae desde el inicio hasta el índice `n` (sin incluirlo). |
| `cadena[m:]`  | Extrae desde el índice `m` hasta el final.                  |
| `cadena[m:n]` | Extrae desde el índice `m` hasta el `n` (sin incluirlo).    |
| `cadena[-n:]` | Extrae los últimos `n` caracteres.                          |

**Ejemplo de slicing:**

```python
texto = "Python"
print(texto[:4])   # Pyth
print(texto[2:])   # thon
print(texto[1:4])  # yth
print(texto[-3:])  # hon
```

### Caracteres de Escape en Strings

Los caracteres de escape permiten incluir caracteres especiales dentro de un string sin interferencias respecto a sus funciones nativas en Python.

| Caracter | Descripción        |
|----------|--------------------|
| `\'`    | Comilla simple.    |
| `\\`   | Barra invertida.   |
| `\n`    | Nueva línea.       |
| `\r`    | Retorno de carro.  |
| `\t`    | Tabulación.        |
| `\b`    | Retroceso.         |
| `\f`    | Salto de página.   |
| `\ooo`  | Valor octal.       |
| `\xhh`  | Valor hexadecimal. |

**Ejemplo de uso de los caracteres de escape:**

```python
print("Hola\nMundo")  # Salto de línea
print("C:\\Archivos\\Datos")  # Ruta con barra invertida
```

## 3. Valores Booleanos en Python

Python maneja valores booleanos (`True` y `False`) que resultan de comparaciones y operaciones lógicas.

```python
x = 10
y = 5

es_mayor = x > y  # True
es_igual = x == y  # False

print(es_mayor, es_igual)
```

## 4. Estructura de Control `if-elif-else`

### ¿Qué es una estructura condicional?

En programación, una estructura condicional permite tomar decisiones basadas en ciertas condiciones.
En Python, se usa la estructura `if-elif-else` para evaluar diferentes escenarios y ejecutar bloques de código según se cumplan o no determinadas condiciones.

### Sintaxis básica de `if`

```python
if condicion:
    # Código que se ejecuta si la condición es verdadera
```

> [!IMPORTANT]
> Observe la indentación para indicar que el bloque de código pertenece al `if`.

El bloque de código dentro del `if` se ejecuta solo si la condición es `True`. Si la condición es `False`, el bloque se ignora.

Ejemplo:

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
```

### Uso de `elif` y `else`

- **`elif`**: Se utiliza para verificar una condición alternativa respecto a la del `if` inicial. Esta se verifica si el `if` no se ejecutó.
- **`else`**: En el caso en que ninguna condición se cumpla, se ejecuta el bloque de código perteneciente a esta.

```python
edad = 14
if edad >= 18:
    print("Eres adulto.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres un niño.")
```

### `if` anidado

Es posible anidar estructuras `if` dentro de otras para evaluar múltiples condiciones de manera jerárquica.

```python
x = 20
if x > 10:
    print("Mayor que 10")
    if x > 15:
        print("Mayor que 15")
```

### Operador ternario

Python permite simplificar condicionales mediante un operador ternario, que es una expresión compacta equivalente a `if-else`.

```python
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)
```

Este operador es útil cuando se necesita asignar valores en función de una condición de manera concisa.
