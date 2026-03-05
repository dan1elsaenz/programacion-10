---
icon: material/format-list-bulleted
---

# :material-format-list-bulleted: Clase 4

## ¿Por qué necesitamos listas?

Hasta este momento, cada dato que el programa necesita recordar se almacena en una **variable independiente**.

Suponga que se desea guardar las notas de cinco estudiantes:

```python
nota1 = 85
nota2 = 90
nota3 = 72
nota4 = 88
nota5 = 95
```

Esto funciona, pero presenta varios problemas:

- Cada nota requiere una variable distinta.
- Si se necesitan 30 notas, se necesitan 30 variables.
- No hay forma de tratarlas como un conjunto.
- Realizar operaciones sobre todas ellas se vuelve tedioso y repetitivo.

!!! question "¿Qué pasaría con 100 estudiantes?"

    Declarar 100 variables individualmente no es práctico.
    El programa necesita una forma de agrupar datos relacionados bajo un mismo nombre.

## ¿Qué es una lista?

Una **lista** es una estructura de datos que permite almacenar **múltiples valores en una sola variable**, organizados en orden.

```python
notas = [85, 90, 72, 88, 95]
```

Con esta única línea se reemplaza el bloque de cinco variables anterior.

Una lista en Python tiene las siguientes características:

- Está **ordenada**: los elementos mantienen el orden en que fueron ingresados.
- Es **indexada**: cada elemento tiene una posición numérica.
- Es **mutable**: sus elementos pueden modificarse después de crearla.
- Puede contener **cualquier tipo de dato**.

### Declaración de una lista vacía

Cuando aún no se conocen los valores que va a contener, se puede declarar una lista vacía:

```python
estudiantes = []
```

Esto crea una lista sin ningún elemento, lista para recibir datos más adelante.

!!! note "Una lista vacía sigue siendo una lista"

    `[]` es una estructura válida en Python.
    Su longitud es `0` y no contiene ningún elemento todavía.

### Inicialización con valores

Cuando los valores ya se conocen desde el inicio, se pueden declarar directamente:

```python
frutas = ["manzana", "pera", "uva", "mango"]
temperaturas = [36.5, 37.0, 36.8, 38.2]
aprobados = [True, False, True, True]
```

Los elementos se separan por comas y se encierran entre corchetes `[ ]`.

### Listas con distintos tipos de datos

Python permite mezclar diferentes tipos de datos dentro de una misma lista:

```python
registro = ["Ana", 17, 9.5, True]
```

!!! warning "Mezclar tipos con cuidado"

    Aunque Python lo permite, mezclar tipos de datos en una lista puede dificultar el procesamiento posterior.
    Por ejemplo, al utilizar _loops_ (que se verán después).

    > En la mayoría de los casos, una lista contiene elementos del **mismo tipo**.

### Representación en memoria

Cuando Python crea una lista, reserva un espacio en memoria para cada elemento
y los organiza en posiciones consecutivas. Cada posición tiene un **índice** que comienza en `0`.

```python
colores = ["rojo", "verde", "azul"]
```

| Índice | Valor     |
| ------ | --------- |
| `0`    | `"rojo"`  |
| `1`    | `"verde"` |
| `2`    | `"azul"`  |

!!! abstract "El índice siempre comienza en cero"

    Una lista con 3 elementos tiene índices `0`, `1` y `2`.
    El último índice siempre es igual a la longitud de la lista menos uno.

## Acceso y modificación de elementos

### Acceso por índice positivo

Una vez creada una lista, se puede acceder a cualquier elemento indicando su **posición entre corchetes**.

```python
frutas = ["manzana", "pera", "uva", "mango"]

print(frutas[0]) # (1)!
print(frutas[1]) # (2)!
print(frutas[3]) # (3)!
```

1. `manzana`
2. `pera`
3. `mango`

> La posición siempre comienza en `0`, por lo que el primer elemento es `frutas[0]` y no `frutas[1]`.

### Acceso por índice negativo

Python también permite acceder a los elementos desde el final de la lista utilizando índices negativos.

```python
frutas = ["manzana", "pera", "uva", "mango"]

print(frutas[-1]) # (1)!
print(frutas[-2]) # (2)!
```

1. `mango`
2. `uva`

El índice `-1` siempre apunta al último elemento, sin importar el tamaño de la lista.

| Índice positivo | Índice negativo | Valor       |
| --------------- | --------------- | ----------- |
| `0`             | `-4`            | `"manzana"` |
| `1`             | `-3`            | `"pera"`    |
| `2`             | `-2`            | `"uva"`     |
| `3`             | `-1`            | `"mango"`   |

### Error por índice inválido

Si se intenta acceder a una posición que no existe, Python genera un `IndexError`.

```python
frutas = ["manzana", "pera", "uva", "mango"]

print(frutas[10]) # (1)!
```

1. `IndexError: list index out of range`

Para conocer la cantidad de elementos de una lista se utiliza la función `len()`:

```python
frutas = ["manzana", "pera", "uva", "mango"]

print(len(frutas)) # (1)!
```

1. `4`

### Modificación de elementos

A diferencia de los strings, las listas son **mutables**. Esto significa que sus elementos pueden cambiarse después de haber sido creados.

Para modificar un elemento, se accede por su índice y se asigna un nuevo valor:

```python
frutas = ["manzana", "pera", "uva", "mango"]

frutas[1] = "kiwi"

print(frutas) # (1)!
```

1. `["manzana", "kiwi", "uva", "mango"]`

El elemento en la posición `1` fue reemplazado. El resto de la lista permanece igual.

!!! note "Comparación con strings"

    Los strings son **inmutables**: no se puede cambiar un carácter directamente.
    Las listas son **mutables**: cualquier elemento puede modificarse en cualquier momento.

=== "String (inmutable)"

    ```python
    texto = "Hola"
    texto[0] = "h"  # (1)!
    ```

    1. Esto genera un `TypeError`

=== "Lista (mutable)"

    ```python
    letras = ["H", "o", "l", "a"]
    letras[0] = "h"  # (1)!
    ```

    1. Esto sí funciona

## Operaciones comunes

### Verificación de existencia con operador `in`

Para verificar si un elemento existe dentro de una lista, Python ofrece el operador `in`.
Este devuelve `True` si el elemento está en la lista, o `False` si no lo está.

> También funciona para **strings**.

```python
frutas = ["manzana", "pera", "uva", "mango"]

print("pera" in frutas)    # (1)!
print("sandía" in frutas)  # (2)!
```

1. `True`
2. `False`

El operador `in` puede combinarse con una estructura condicional para tomar decisiones:

```python
frutas = ["manzana", "pera", "uva", "mango"]
fruta_buscada = input("¿Qué fruta desea buscar? ")

if fruta_buscada in frutas:
    print(f"{fruta_buscada} está en la lista.")
else:
    print(f"{fruta_buscada} no está en la lista.")
```

!!! tip "Búsqueda sin distinguir mayúsculas"

    Si la lista contiene strings, es recomendable normalizar el texto antes de buscar.

    ```python
    if fruta_buscada.lower().strip() in frutas:
        print("Encontrada.")
    ```

### Suma de elementos

Cuando una lista contiene valores numéricos, es posible calcular su suma accediendo a cada elemento por su índice y acumulando el resultado.

```python
notas = [85, 90, 72, 88, 95]

suma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4]

print(f"La suma total es: {suma}") # (1)!
```

1. `La suma total es: 430`

Python también ofrece la función integrada `sum()` que realiza esta operación directamente:

```python
notas = [85, 90, 72, 88, 95]

suma = sum(notas)

print(f"La suma total es: {suma}") # (1)!
```

1. `La suma total es: 430`

!!! note "¿Cuándo usar cada enfoque?"

    - La suma manual posición por posición es útil para entender el concepto.
    - En la práctica, `sum()` es más limpia y directa.
    - Eventualmente, vamos a ver cómo hacerlo con _loops_.

### Promedio

El promedio se obtiene dividiendo la suma de los elementos entre la cantidad de elementos.
Para conocer la cantidad de elementos se utiliza `len()`.

```python
notas = [85, 90, 72, 88, 95]

suma = sum(notas)
cantidad = len(notas)
promedio = suma / cantidad

print(f"El promedio es: {promedio}") # (1)!
```

1. `El promedio es: 86.0`

!!! warning "División entre cero"

    Si la lista está vacía, `len()` devuelve `0` y la división generará un `ZeroDivisionError`.
    Es una buena práctica verificar que la lista no esté vacía antes de calcular el promedio.

    ```python
    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
        print(f"El promedio es: {promedio}")
    else:
        print("La lista no contiene elementos.")
    ```

### Valor mínimo y máximo

Python ofrece dos funciones integradas para encontrar el valor más pequeño y el más grande dentro de una lista:

```python
notas = [85, 90, 72, 88, 95]

print(min(notas)) # (1)!
print(max(notas)) # (2)!
```

1. `72`
2. `95`

Estas funciones también funcionan con strings, en cuyo caso utilizan el orden alfabético:

```python
frutas = ["manzana", "pera", "uva", "mango"]

print(min(frutas)) # (1)!
print(max(frutas)) # (2)!
```

1. `manzana`
2. `uva`

### Resumen de funciones integradas para listas

|      Función | Descripción                       |
| -----------: | --------------------------------- |
| `len(lista)` | Cantidad de elementos             |
| `sum(lista)` | Suma de todos los elementos       |
| `min(lista)` | Elemento con el valor más pequeño |
| `max(lista)` | Elemento con el valor más grande  |

## Métodos de listas

Además de las operaciones básicas, las listas poseen **métodos integrados** que permiten agregar, eliminar, buscar y transformar elementos.

Un método se invoca utilizando la notación:

```python
lista.metodo()
```

> A diferencia de los strings, varios métodos de listas **modifican la lista original** en lugar de devolver una nueva.

### Agregar un elemento al final

El método `append()` agrega un nuevo elemento al final de la lista.

```python
frutas = ["manzana", "pera", "uva"]

frutas.append("mango") # (1)!

print(frutas) # (2)!
```

1. Agrega `"mango"` al final de la lista.
2. `['manzana', 'pera', 'uva', 'mango']`

Este es el método más común para construir una lista elemento por elemento.

### Eliminar el último elemento

El método `pop()` elimina el último elemento de la lista y lo **devuelve** como resultado.

```python
notas = [85, 90, 72, 88]

ultima = notas.pop() # (1)!

print(ultima) # (2)!
print(notas)  # (3)!
```

1. Elimina `88` de la lista y lo guarda en `ultima`.
2. `88`
3. `[85, 90, 72]`

!!! note "El valor eliminado puede guardarse"

    Como `pop()` devuelve el elemento eliminado, se puede asignar a una variable para usarlo después.

### Contar apariciones de un elemento

El método `count()` devuelve cuántas veces aparece un valor dentro de la lista.

```python
votos = ["sí", "no", "sí", "sí", "no"]

print(votos.count("sí")) # (1)!
print(votos.count("no")) # (2)!
```

1. `3`
2. `2`

### Buscar el índice de un elemento

El método `index()` devuelve la posición de la primera aparición de un valor.

```python
frutas = ["manzana", "pera", "uva", "mango"]

print(frutas.index("uva")) # (1)!
```

1. `2`

!!! warning "El valor debe existir en la lista"

    Si el valor no se encuentra, Python genera un `ValueError`.
    Se recomienda verificar primero con `in` antes de usar `index()`.

    ```python
    if "uva" in frutas:
        print(frutas.index("uva"))
    ```

### Insertar un elemento en una posición específica

El método `insert()` agrega un elemento en el índice indicado, desplazando los elementos siguientes.

```python
frutas = ["manzana", "pera", "uva"]

frutas.insert(1, "kiwi") # (1)!

print(frutas) # (2)!
```

1. Inserta `"kiwi"` en la posición `1`. Los elementos desde esa posición se desplazan hacia la derecha.
2. `['manzana', 'kiwi', 'pera', 'uva']`

### Eliminar un valor específico

El método `remove()` elimina la **primera aparición** de un valor en la lista.

```python
frutas = ["manzana", "pera", "uva", "pera"]

frutas.remove("pera") # (1)!

print(frutas) # (2)!
```

1. Elimina solo la primera `"pera"` encontrada.
2. `['manzana', 'uva', 'pera']`

!!! warning "Solo elimina la primera aparición"

    Si el valor aparece varias veces, únicamente se elimina la primera ocurrencia.
    Si el valor no existe, Python genera un `ValueError`.

### Invertir el orden de la lista

El método `reverse()` invierte la lista, sin devolver una nueva lista.

```python
numeros = [1, 2, 3, 4, 5]

numeros.reverse()

print(numeros) # (1)!
```

1. `[5, 4, 3, 2, 1]`

### Ordenar la lista

El método `sort()` ordena los elementos de la lista, de menor a mayor por defecto.

```python
notas = [88, 72, 95, 65, 90]

notas.sort()

print(notas) # (1)!
```

1. `[65, 72, 88, 90, 95]`

Para ordenar de mayor a menor se utiliza el parámetro `reverse=True`:

```python
notas.sort(reverse=True)

print(notas) # (1)!
```

1. `[95, 90, 88, 72, 65]`

### Concatenar listas

El operador `+` une dos listas y produce una **nueva lista** con todos los elementos de ambas.

```python
l1 = [1, 2]
l2 = [3, 4]

l3 = l1 + l2

print(l3) # (1)!
```

1. `[1, 2, 3, 4]`

### Repetir una lista

El operador `*` repite los elementos de una lista un número determinado de veces.

```python
l1 = [1, 2]

l3 = l1 * 3

print(l3) # (1)!
```

1. `[1, 2, 1, 2, 1, 2]`

### Copiar una lista

Asignar una lista a otra variable **no crea una copia independiente**: ambas variables apuntan a la misma lista en memoria.

```python
l1 = [1, 2, 3]
l2 = l1        # l2 apunta a la misma lista que l1

l2.append(4)

print(l1) # (1)!
print(l2) # (2)!
```

1. `[1, 2, 3, 4]`
2. `[1, 2, 3, 4]`

Para crear una copia verdaderamente independiente se utiliza el método `copy()`:

```python
l1 = [1, 2, 3]
l2 = l1.copy()  # l2 es una copia independiente

l2.append(4)

print(l1) # (1)!
print(l2) # (2)!
```

1. `[1, 2, 3]`
2. `[1, 2, 3, 4]`

!!! warning "Diferencia con los números"

    Con variables numéricas, la asignación sí crea una copia independiente:

    ```python
    n1 = 10
    n2 = n1
    n2 *= 3

    print(n1) # 10
    print(n2) # 30
    ```

    Con listas, en cambio, la asignación simple crea un *alias*, no una copia.
    Siempre use `.copy()` si necesita trabajar con versiones separadas de una misma lista.

### Resumen de métodos de listas

|                   Método | Descripción                                         |
| -----------------------: | --------------------------------------------------- |
|      `lista.append(val)` | Agrega `val` al final de la lista                   |
|            `lista.pop()` | Elimina y devuelve el último elemento               |
|       `lista.count(val)` | Devuelve cuántas veces aparece `val`                |
|       `lista.index(val)` | Devuelve el índice de la primera aparición de `val` |
| `lista.insert(idx, val)` | Inserta `val` en la posición `idx`                  |
|      `lista.remove(val)` | Elimina la primera aparición de `val`               |
|        `lista.reverse()` | Invierte el orden de los elementos                  |
|           `lista.sort()` | Ordena los elementos de menor a mayor               |
|                `l1 + l2` | Concatena dos listas en una nueva                   |
|                 `l1 * n` | Repite los elementos de la lista `n` veces          |
|           `lista.copy()` | Devuelve una copia independiente de la lista        |

## Ejercicio integrador

=== "Enunciado"

    Una profesora desea un programa que le ayude a consultar el rendimiento de sus estudiantes.
    El programa debe cumplir con los siguientes requisitos:

    1. Almacenar los nombres de **5 estudiantes** y sus respectivas **notas** en dos listas separadas.
    2. Mostrar un **menú** al inicio con las siguientes opciones:
        - Opción `1`: Buscar estudiante
        - Opción `2`: Ver estadísticas del grupo
    3. Según la opción elegida:
        - **Opción 1 — Buscar estudiante:** solicitar el nombre de un estudiante.
            - Si existe, mostrar su nota y un mensaje según su rendimiento:
                - Nota mayor o igual a 90: `Excelente`
                - Nota mayor o igual a 80: `Muy bueno`
                - Nota mayor o igual a 70: `Bueno`
                - Nota menor a 70: `Debe mejorar`
            - Si no existe, mostrar un mensaje indicándolo.
        - **Opción 2 — Ver estadísticas:** mostrar el promedio, la nota más alta y la nota más baja del grupo.
    4. Si el usuario digita una opción inválida, mostrar un mensaje de error.

=== "Solución"

    ### Paso 1: Declarar las listas

    El primer paso es definir las dos listas con los datos de los estudiantes.
    Es importante que el nombre y la nota de cada estudiante ocupen **el mismo índice** en sus respectivas listas.

    ```python
    nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
    notas   = [92, 78, 85, 65, 90]
    ```

    Esto significa que `nombres[0]` corresponde a `notas[0]`, y así sucesivamente.

    | Índice | Nombre     | Nota |
    |--------|------------|------|
    | `0`    | `"Ana"`    | `92` |
    | `1`    | `"Luis"`   | `78` |
    | `2`    | `"María"`  | `85` |
    | `3`    | `"Carlos"` | `65` |
    | `4`    | `"Sofía"`  | `90` |

    ### Paso 2: Mostrar el menú y capturar la opción

    Se imprime el menú y se solicita al usuario que elija una opción.

    ```python
    print("=== Sistema de consulta de estudiantes ===")
    print("1. Buscar estudiante")
    print("2. Ver estadísticas del grupo")

    opcion = input("\nElija una opción: ").strip()
    ```

    ### Paso 3: Ejecutar la opción elegida

    Se utiliza una estructura `if-elif-else` para ejecutar el bloque correspondiente a la opción ingresada.

    ```python
    if opcion == "1":
        # bloque de búsqueda
    elif opcion == "2":
        # bloque de estadísticas
    else:
        print("Opción inválida. Debe digitar 1 o 2.")
    ```

    !!! note "La opción se compara como string"

        El valor devuelto por `input()` siempre es un string.
        Por eso la comparación se hace con `"1"` y `"2"` entre comillas,
        no con los enteros `1` y `2`.

    ### Paso 4: Desarrollar la búsqueda de estudiante

    Dentro del bloque de la opción `1`, se solicita el nombre y se verifica si existe en la lista.

    ```python
    if opcion == "1":
        busqueda = input("Digite el nombre del estudiante: ").strip().title()

        if busqueda in nombres:
            indice = nombres.index(busqueda) # (1)!
            nota_estudiante = notas[indice]

            print(f"\nEstudiante: {busqueda}")
            print(f"Nota: {nota_estudiante}")

            if nota_estudiante >= 90:
                print("Rendimiento: Excelente")
            elif nota_estudiante >= 80:
                print("Rendimiento: Muy bueno")
            elif nota_estudiante >= 70:
                print("Rendimiento: Bueno")
            else:
                print("Rendimiento: Debe mejorar")
        else:
            print(f"\nEl estudiante '{busqueda}' no está registrado.")
    ```

    1. El método `.index()` devuelve la posición de un elemento dentro de la lista.
       Con ese índice se puede acceder a la nota correspondiente en la otra lista.

    !!! tip "¿Por qué `.title()`?"

        El método `.title()` convierte la primera letra de cada palabra a mayúscula.
        Así, si el usuario escribe `"ana"` o `"ANA"`, se convierte a `"Ana"`,
        que es el formato en que están almacenados los nombres en la lista.

    ### Paso 5: Desarrollar las estadísticas del grupo

    Dentro del bloque de la opción `2`, se calculan y muestran las estadísticas.

    ```python
    elif opcion == "2":
        promedio = sum(notas) / len(notas)

        print("\n--- Estadísticas del grupo ---")
        print(f"Promedio: {promedio:.1f}") # (1)!
        print(f"Nota más alta: {max(notas)}")
        print(f"Nota más baja: {min(notas)}")
    ```

    1. El formato `:.1f` dentro del f-string indica que el número flotante
       se debe mostrar con exactamente **un decimal**.

    ### Programa completo

    ```python
    nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
    notas   = [92, 78, 85, 65, 90]

    print("=== Sistema de consulta de estudiantes ===")
    print("1. Buscar estudiante")
    print("2. Ver estadísticas del grupo")

    opcion = input("\nElija una opción: ").strip()

    if opcion == "1":
        busqueda = input("Digite el nombre del estudiante: ").strip().title()

        if busqueda in nombres:
            indice = nombres.index(busqueda)
            nota_estudiante = notas[indice]

            print(f"\nEstudiante: {nombres[indice]}")
            print(f"Nota: {nota_estudiante}")

            if nota_estudiante >= 90:
                print("Rendimiento: Excelente")
            elif nota_estudiante >= 80:
                print("Rendimiento: Muy bueno")
            elif nota_estudiante >= 70:
                print("Rendimiento: Bueno")
            else:
                print("Rendimiento: Debe mejorar")
        else:
            print(f"\nEl estudiante '{busqueda}' no está registrado.")

    elif opcion == "2":
        promedio = sum(notas) / len(notas)

        print("\n--- Estadísticas del grupo ---")
        print(f"Promedio: {promedio:.1f}")
        print(f"Nota más alta: {max(notas)}")
        print(f"Nota más baja: {min(notas)}")

    else:
        print("Opción inválida. Debe digitar 1 o 2.")
    ```

    !!! example "Ejemplos de ejecución"

        === "Opción 1 — Estudiante encontrado"

            ```
            === Sistema de consulta de estudiantes ===
            1. Buscar estudiante
            2. Ver estadísticas del grupo

            Elija una opción: 1
            Digite el nombre del estudiante: ana

            Estudiante: Ana
            Nota: 92
            Rendimiento: Excelente
            ```

        === "Opción 1 — Estudiante no encontrado"

            ```
            === Sistema de consulta de estudiantes ===
            1. Buscar estudiante
            2. Ver estadísticas del grupo

            Elija una opción: 1
            Digite el nombre del estudiante: Pedro

            El estudiante 'Pedro' no está registrado.
            ```

        === "Opción 2 — Estadísticas"

            ```
            === Sistema de consulta de estudiantes ===
            1. Buscar estudiante
            2. Ver estadísticas del grupo

            Elija una opción: 2

            --- Estadísticas del grupo ---
            Promedio: 82.0
            Nota más alta: 92
            Nota más baja: 65
            ```

        === "Opción inválida"

            ```
            === Sistema de consulta de estudiantes ===
            1. Buscar estudiante
            2. Ver estadísticas del grupo

            Elija una opción: 5

            Opción inválida. Debe digitar 1 o 2.
            ```
