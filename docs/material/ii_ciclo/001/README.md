# Clase 1: Clase de Repaso de Python

## Strings

Los **strings** (cadenas de texto) son secuencias de caracteres inmutables.
Pueden incluir letras, símbolos, números y espacios.
Se declaran con comillas simples `'texto'`, dobles `"texto"` o triples `'''texto'''` para varias líneas.

Se pueden manipular con operaciones como:

- **Concatenación**: unir dos strings. Ejemplo: `"Hola" + " Mundo"`
- **Repetición**: repetir un string varias veces. Ejemplo: `"a" * 3` → `"aaa"`
- **Acceso a caracteres**: con índices. Ejemplo: `"Hola"[1] # 'o'`
- **Slicing**: subcadenas. Ejemplo: `"Hola"[1:3] # "ol"`

=== "Mayúsculas y minúsculas"

    ```python
    s = "Hola Mundo"
    print(s.upper())   # 'HOLA MUNDO'
    print(s.lower())   # 'hola mundo'
    ```

=== "Espacios y limpieza"

    ```python
    s = "  texto con espacios  "
    print(s.strip())  # 'texto con espacios'
    print(s.lstrip()) # elimina izquierda
    print(s.rstrip()) # elimina derecha
    ```

=== "Buscar y reemplazar"

    ```python
    s = "banana"
    print(s.replace("a", "o"))   # 'bonono'
    print("ana" in s)            # True
    print(s.count("a"))          # 3
    ```

=== "Dividir y unir"

    ```python
    s = "uno,dos,tres"
    partes = s.split(",")       # ['uno', 'dos', 'tres']
    print("-".join(partes))     # 'uno-dos-tres'
    ```

### Ejercicio

Escribir un programa que reciba una frase, elimine los signos de puntuación, pase todo a minúsculas y cuente cuántas veces aparece cada palabra.

```python
frase = "Hola, hola. ¿Qué tal? Tal vez sí, tal vez no."

# Resultado esperado:
# hola -> 2
# tal -> 2
# vez -> 2
# sí -> 1
# qué -> 1
# no -> 1
```

---

## Listas

Las **listas** son estructuras de datos ordenadas, mutables y heterogéneas, es decir, pueden almacenar elementos de distintos tipos (enteros, strings, booleanos, otras listas, entre otros.).
Se definen usando corchetes `[]` o el constructor `list()` y los elementos están separados por comas.

=== "Agregar elementos"

    ```python
    numeros = [1, 2, 3]
    numeros.append(4)      # [1, 2, 3, 4]
    numeros.insert(1, 99)  # [1, 99, 2, 3, 4]
    ```

=== "Eliminar elementos"

    ```python
    lista = [1, 2, 3, 2]
    lista.remove(2)    # elimina el primer 2 → [1, 3, 2]
    lista.pop()        # elimina el último → [1, 3]
    ```

=== "Ordenar y contar"

    ```python
    valores = [4, 1, 3, 2]
    valores.sort()             # [1, 2, 3, 4]
    valores.reverse()          # [4, 3, 2, 1]
    print(valores.count(3))    # 1
    ```

=== "Otras operaciones útiles"

    ```python
    lista = [10, 20, 30]
    suma = sum(lista)       # 60
    maximo = max(lista)     # 30
    minimo = min(lista)     # 10
    ```

### Ejercicio

Convertir una lista de temperaturas en grados Celsius a Fahrenheit.
Eliminar duplicados, redondear a un decimal y ordenar de mayor a menor.

```python
celsius = [25, 30, 30, 10]

# Resultado esperado:
# [86.0, 77.0, 50.0]
```

---

## Estructura de control `if`

La instrucción `if` permite ejecutar código **sólo si se cumple una condición**.  
Puede complementarse con `elif` (condición alternativa) y `else` (caso por defecto).

Las condiciones se evalúan como **valores booleanos** (`True` o `False`).

**Ejemplo de sintaxis:**

```python
x = 15
if x < 10:
    print("Menor que 10")
elif x == 10:
    print("Es 10")
else:
    print("Mayor que 10")
```

=== "Operadores relacionales"

    ```python
    ==   # Igualdad
    !=   # Diferente
    >    # Mayor que
    <    # Menor que
    >=   # Mayor o igual
    <=   # Menor o igual
    ```

=== "Operadores lógicos"

    ```python
    and  # Ambas condiciones deben ser verdaderas
    or   # Al menos una condición debe ser verdadera
    not  # Niega una condición
    ```

=== "Ejemplo combinado"

    ```python
    edad = 20
    nota = 85

        if edad >= 18 and nota >= 70:
            print("Aprobado como adulto")
        else:
            print("No cumple los requisitos")
    ```

### Ejercicio

Escribir un programa que reciba tres notas.
El estudiante reprueba si alguna nota es menor que 50 o si el promedio de las tres es menor que 70.

```
Entrada: 80, 45, 90  → Reprobado
Entrada: 60, 70, 75  → Aprobado
```

---

## `for` loop

El bucle `for` permite **recorrer secuencias** como listas, cadenas o rangos, y ejecutar un bloque de código para cada elemento.  
Es una herramienta fundamental para procesar datos en colecciones.

```python title="Ejemplo básico"
for letra in "Hola":
    print(letra)
```

### Ejemplos comunes

```python title="Iterar sobre una lista"
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
```

```python title="Usar range()"
for i in range(3, 8):
    print(i)  # Imprime del 3 al 7
```

```python title="Acceder a índices con enumerate()"
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"{indice}: {color}")
```

```python title="Iterar sobre un string"
nombre = "python"
for caracter in nombre:
    print(caracter.upper())
```

### Ejercicio

Construir un histograma textual. Por cada número en una lista, imprimir una línea con esa cantidad de asteriscos `*`.

```python
# Entrada: [3, 7, 1]
# Salida:
# ***
# *******
# *
```

---

## `while` loop

El bucle `while` permite **repetir instrucciones mientras se cumpla una condición** lógica.
Se utiliza cuando no se conoce de antemano cuántas repeticiones se deben realizar.

```python title="Bucle descendente"
contador = 3
while contador > 0:
    print(contador)
    contador -= 1
```

### Consideraciones importantes

- Si la condición nunca deja de cumplirse, el bucle será **infinito**.
- Se puede usar `break` para salir del bucle en un momento determinado.
- También se puede usar `continue` para saltar a la siguiente iteración sin ejecutar el resto del bloque.

=== "Uso de `break`"

    ```python
    while True:
        entrada = input("Escriba 'fin' para salir: ")
        if entrada == "fin":
            break
    ```

=== "Uso de `continue`"

    ```python
    numero = 0
    while numero < 5:
        numero += 1
        if numero == 3:
            continue  # salta el 3
        print(numero)
    ```

### Ejercicio

Simular una calculadora interactiva.
El programa debe permitir al usuario ingresar una operación (`+`, `-`, `*`, `/`) y dos números.
El ciclo se repite hasta que el usuario escriba `"salir"` como operación.
Debe manejar el caso de división por cero.

```
Entrada:
operación: +
número1: 5
número2: 3
Resultado: 8

operación: salir
Fin del programa
```

---

## Tuplas

Una **tupla** es una estructura de datos similar a una lista, pero **inmutable**.
Sus elementos no pueden ser modificados una vez creada.
Se define con paréntesis `()` o con el constructor `tuple()`.

Las tuplas son útiles para representar **datos agrupados** que no deben cambiar, como coordenadas, fechas o pares clave-valor temporales.

```python title="Ejemplo básico"
punto = (3, 4) # Inmutable
x, y = punto
print(x)  # 3
print(y)  # 4
```

### Propiedades importantes

=== "Acceso por índice"

    ```python
    tupla = ("lunes", "martes", "miércoles")
    print(tupla[0])  # lunes
    ```

=== "Inmutabilidad"

    ```python
    dias = ("lunes", "martes")
    # Error: las tuplas no se pueden modificar
    dias[0] = "domingo"
    ```

=== "Tuplas de un sólo elemento"

    ```python
    uno = (5,)  # la coma es necesaria
    print(type(uno))  # <class 'tuple'>
    ```

### Ejercicio

Dada una lista de coordenadas (pares `(x, y)`), determinar cuál está más cerca del origen `(0, 0)`.

```python
coordenadas = [(3, 4), (1, 1), (5, 5)]

# Resultado esperado: (1, 1)
```

---

## Diccionarios

Un **diccionario** es una colección de pares **clave-valor**.
Permite almacenar y acceder a valores usando claves personalizadas, como strings o números.

Se define con llaves `{}`, y cada par clave-valor se separa por `:`.

```python title="Ejemplo básico"
persona = {
    "nombre": "Ana",
    "edad": 30
}

print(persona["edad"])  # 30
```

### Operaciones comunes

=== "Agregar o modificar elementos"

    ```python
    persona["edad"] = 31           # Modifica edad
    persona["correo"] = "a@b.com"  # Agrega nueva clave
    ```

=== "Recorrer claves y valores"

    ```python
    for clave, valor in persona.items():
        print(clave, "->", valor)
    ```

=== "Verificar existencia de una clave"

    ```python
    if "nombre" in persona:
        print("Nombre registrado")
    ```

=== "Eliminar elementos"

    ```python
    del persona["edad"]
    ```

### Ejercicio

Guardar en un diccionario las calificaciones de varios estudiantes.
Cada estudiante tiene una lista de notas.
Se debe calcular el promedio de cada uno y mostrar:

- El estudiante con el **mejor promedio**
- El estudiante con el **peor promedio**

```python
# Entrada:
notas = {
    "Ana": [90, 85, 88],
    "Luis": [100, 100, 90],
    "María": [70, 65, 60]
}

# Resultado esperado:
# Mejor promedio: Luis
# Peor promedio: María
```

---

## Funciones

Una **función** es un bloque de código reutilizable que realiza una tarea específica.
Permite organizar el código, evitar repeticiones y facilitar la lectura.

Se define con la palabra clave `def`, se le da un nombre, se indican los parámetros entre paréntesis y se coloca el bloque indentado.

```python title="Definición básica"
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Luis"))  # 'Hola, Luis'
```

### Otras posibilidades

```python title="Función sin parámetros"
def mostrar_menu():
    print("1. Iniciar")
    print("2. Salir")
```

```python title="Función con varios parámetros"
def sumar(a, b):
    return a + b
```

```python title="Valores por defecto"
def saludar(nombre="invitado"):
    return f"Hola, {nombre}"
```

```python title="Funciones que no retornan (procedimientos)"
def imprimir_saludo(nombre):
    print(f"Hola, {nombre}")
```

### Ejercicio

Escribir una función que determine si una frase es un **pangrama**, es decir, si contiene **todas las letras del abecedario al menos una vez** (no importa el orden).

```python
frase = "El veloz murcielago hindu comia feliz cardillo y kiwi"
# Resultado esperado: True
```

---

## Recursividad

La **recursividad** es una técnica en la que una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas más pequeños.
Cada llamada reduce el problema hasta llegar a un **caso base**, que detiene la recursión.

```python title="Ejemplo clásico"
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Consideraciones importantes

=== "Caso base"

    ```python
    # Toda función recursiva debe tener una condición de salida
    # que evite llamadas infinitas

    def cuenta_regresiva(n):
        if n == 0:
            return
        print(n)
        cuenta_regresiva(n - 1)
    ```

=== "Evitar recursión infinita"

```python
# Olvidar el caso base puede generar un error por límite de recursión

def infinito():
    return infinito()  # Error: RecursionError
```

### Ejercicio

Implementar una función recursiva que reciba un número entero `n` y **genere todas las cadenas binarias posibles de longitud `n`**.
La función debe devolver una lista con todas las combinaciones generadas.

```
Entrada: n = 3
Salida: ['000', '001', '010', '011', '100', '101', '110', '111']
```
