
# Clase 1: Conceptos básicos de Python

Antes de avanzar en la programación con Python, es fundamental comprender algunos conceptos básicos que afectan la estructura y legibilidad del código. Estos incluyen la indentación, la declaración y definición de variables, y los comentarios.

## 1. Indentación en Python

Python utiliza la indentación para definir bloques de código, en lugar de llaves `{}` como en otros lenguajes. La indentación se refiere a los espacios o tabulaciones (_tabs_) que se añaden al inicio de una línea para indicar su nivel de jerarquía dentro del código.

### Reglas clave de la indentación en Python

- Todos los bloques de código dentro de estructuras como `if`, `for`, `while`, `def` y `class` deben estar indentados uniformemente.
    - Esto se realiza para indicar que un bloque de código pertenece a una jerarquía específica.
- Se recomienda utilizar 4 espacios por nivel de indentación.
- Una indentación incorrecta generará un error de sintaxis (`IndentationError`).

### Ejemplo de indentación correcta

```python
def saludar():
    nombre = "Ana"
    print("Hola,", nombre)  # La línea está indentada correctamente

saludar()
```

### Ejemplo de indentación incorrecta

El siguiente código generará un error porque la línea `nombre = "Ana"` no está correctamente indentada:

```python
def saludar():
nombre = "Ana" # Parece que la función saludar() está vacía
    print("Hola,", nombre) # Esta indentación no tiene sentido porque la línea anterior no posee

saludar()
```

**Salida esperada:**

```plaintext
IndentationError: expected an indented block
```

## 2. Declaración y Definición de Variables

Una variable es un espacio de memoria donde se almacena un valor.
En Python, no es necesario declarar explícitamente el tipo de dato de una variable, puesto que el lenguaje usa tipado dinámico (asigna automáticamente el tipo de dato).

### Reglas para declarar variables

- Los nombres de las variables no pueden comenzar con un número.
- Sólo pueden contener letras, números y guiones bajos (`_`)
- **NO** pueden contener espacios ni caracteres especiales.
- Convenciones para nombrar variables:
    - `snake_case`
    - `camelCase`
    - `PascalCase`
- Distinción entre mayúsculas y minúsculas (`edad` y `Edad` son variables diferentes).
- Se pueden definir múltiples variables en una sola línea.

#### Ejemplo de declaración y asignación de variables

```python
nombre = "Carlos"  # Variable tipo string
edad = 25  # Variable tipo entero
altura = 1.75  # Variable tipo flotante
es_estudiante = True  # Variable tipo booleano

print(nombre, edad, altura, es_estudiante)
```

**Salida esperada:**

```plaintext
Carlos 25 1.75 True
```

#### Ejemplo de asignación múltiple

Python permite asignar valores a varias variables en una sola línea:

```python
x, y, z = 10, 20, 30
print(x, y, z)  # Salida: 10 20 30
```

También es posible asignar el mismo valor a varias variables a la vez:

```python
a = b = c = "Python"
print(a, b, c)  # Salida: Python Python Python
```

### Variables constantes en Python

No existe una palabra clave `const` como en otros lenguajes de programación, pero por convención, se utilizan nombres en mayúsculas para representar constantes:

```python
PI = 3.1416
URL_BASE = "https://ejemplo.com"
```

Aunque estos valores pueden cambiarse, se espera que permanezcan constantes durante la ejecución del programa.
Sirven para indicarle al programador que no modifique estas variables.

## 3. Comentarios en Python

Los comentarios son líneas de texto dentro del código que no afectan su ejecución. Se utilizan para mejorar la legibilidad del código y explicar su funcionamiento.

### Comentarios de una línea

Se crean utilizando el símbolo `#`. Todo lo que se escriba después en la **misma línea** será ignorado por el intérprete.

```python
# Esto es un comentario de una línea
nombre = "Luis"  # Se puede colocar un comentario al final de una línea de código
```

### Comentarios multilínea

Python no tiene un símbolo específico para comentarios multilínea, pero se puede lograr utilizando comillas triples (`""" """` o `''' '''`). Aunque en realidad se usan para _docstrings_ (documentación de funciones y clases), el intérprete ignora su contenido cuando no están asignados a ninguna variable.

```python
"""
Este es un comentario de múltiples líneas.
Se usa para documentar el código.
"""
print("Hola, mundo")  # El comentario anterior es ignorado
```

Otra opción es utilizar `#` en varias líneas consecutivas:

```python
# Este es un comentario largo
# que ocupa varias líneas
# y explica el código en detalle.
```

## 4. Tipos de Datos en Python

Python maneja diferentes tipos de datos, organizados en categorías.

| Categoría        | Tipo         | Descripción                               | Ejemplo                          | _Type casting_         |
|-----------------|-------------|-------------------------------------------|----------------------------------|--------------------------|
| **Texto**       | `str`       | Cadenas de caracteres                     | `"Hola, Python!"`               | `str(valor)`             |
| **Numéricos**   | `int`       | Números enteros                           | `5, -3, 100`                     | `int(valor)`             |
|                | `float`     | Números decimales                         | `3.14, -0.5, 2.71`               | `float(valor)`           |
|                | `complex`   | Números complejos                         | `3+5j, -1j`                      | `complex(valor)`         |
| **Secuencias**  | `list`      | Lista de valores modificables             | `[1, 2, 3]`                      | `list(valor)`            |
|                | `tuple`     | Lista de valores inmutables               | `(10, 20, 30)`                   | `tuple(valor)`           |
|                | `range`     | Rango de números                          | `range(5)` (0,1,2,3,4)           | `range(inicio, fin, paso)` |
| **Mapas**      | `dict`      | Almacena pares clave-valor                | `{"nombre": "Ana", "edad": 17}`  | `dict(valor)`            |
| **Conjuntos**   | `set`       | Conjunto de valores únicos                | `{1, 2, 3}`                      | `set(valor)`             |
|                | `frozenset` | Conjunto inmutable                        | `frozenset([1, 2, 3])`           | `frozenset(valor)`       |
| **Booleanos**   | `bool`      | Valores lógicos `True` o `False`          | `True, False`                    | `bool(valor)`            |
| **Binarios**    | `bytes`     | Secuencia de bytes inmutable              | `b"Hola"`                        | `bytes(valor)`           |
|                | `bytearray` | Secuencia de bytes modificable            | `bytearray(5)`                   | `bytearray(valor)`       |
|                | `memoryview` | Vista de memoria de un objeto binario     | `memoryview(b"Hola")`            | `memoryview(valor)`      |
| **Nulo**        | `NoneType`  | Representa ausencia de valor              | `None`                           | No aplica                |

A continuación se muestra la definición de variables de cada uno de los tipos de datos anteriores:

```python
texto = "Hola, mundo"  # str
numero = 42  # int
decimal = 3.14  # float
complejo = 2 + 3j  # complex
lista = [1, 2, 3]  # list
tupla = (10, 20, 30)  # tuple
rango = range(5)  # range
diccionario = {"nombre": "Luis", "edad": 22}  # dict
conjunto = {1, 2, 3}  # set
conjunto_fijo = frozenset([1, 2, 3])  # frozenset
booleano = True  # bool
binario = b"Hola"  # bytes
mutable_binario = bytearray(5)  # bytearray
vista_memoria = memoryview(b"Hola")  # memoryview
nulo = None  # NoneType

print(texto, numero, decimal, complejo, lista, tupla, rango, diccionario, conjunto, conjunto_fijo, booleano, binario, mutable_binario, vista_memoria, nulo)
```

### Función `type`

Esta función sirve para determinar el tipo de dato de una variable que se ingrese como parámetro.

```python
var = "Hola mundo!"
tipo = type(var)
print(tipo)
```

**Salida esperada**

```plaintext
<class 'str'>
```

## 5. Funciones de Entrada y Salida (I/O) en Python

### `print()`: Mostrar información en pantalla

La función `print()` permite imprimir valores en la terminal.

```python
nombre = "Ana"
print("Hola,", nombre)
```

Se pueden imprimir múltiples valores separados por comas:

```python
print("Nombre:", "Juan", "Edad:", 20)
```

También se puede cambiar el separador (`sep`) o el final de línea (`end`):

```python
print("Python", "es", "genial", sep="-")  # Salida: Python-es-genial
print("Hola", end=" ")
print("Mundo")  # Salida: Hola Mundo
```

> [!NOTE]
> De forma predeterminada, `sep=" "` y `end="\n"`.

### `input()`: Leer información del usuario

La función `input()` permite recibir información desde el teclado y siempre devuelve un string.

```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola,", nombre)
```

Si se necesita un número, debe convertirse explícitamente:

```python
edad = int(input("Ingresa tu edad: "))  # Conversión a entero
precio = float(input("Ingresa un precio: "))  # Conversión a flotante

print("Edad:", edad, "Precio:", precio)
```

## 3. Concatenación de Strings

La **concatenación** de strings es la unión de dos o más cadenas de texto.

### Métodos de concatenación

#### Uso del operador `+`
Se puede usar `+` para unir dos cadenas de texto. Se debe agregar un espacio manualmente si es necesario.

```python
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print("Tu nombre completo es: " + nombre_completo)
```

#### Uso de `f-strings` (Python 3.6 en adelante)
Permite insertar variables dentro de un string de manera más sencilla.

```python
nombre = "Ana"
edad = 17
string_completo = f"Hola, {nombre}, tienes {edad} años."
print(string_completo)
```

