---
icon: material/lambda
---

# :material-lambda: Clase 6

No toda función necesita un nombre. Cuando una función es corta y se usa una sola vez, escribirla con `def` no es necesario.
Esta clase presenta dos formas de escribir esas funciones cortas de manera más directa: las expresiones lambda y las comprensiones de listas.

## Expresiones lambda

Un ejemplo típico es una función como `es_par` o `elevar_al_cuadrado`: se usa una sola vez, como argumento de `map()`, `filter()` o `sorted()`, y después se descarta.

Una **expresión lambda** es una función sin nombre, escrita en una sola línea, pensada exactamente para ese caso.

```python
cuadrado = lambda numero: numero ** 2

print(cuadrado(5))   # (1)!
```

1. `25` – `lambda numero: numero ** 2` construye una función que recibe `numero` y retorna `numero ** 2`, igual que lo haría un `def`, pero sin nombre ni la palabra `return`.

La sintaxis es `lambda parámetros: expresión`. A diferencia de un `def`, el cuerpo de una lambda es una única expresión, cuyo resultado se retorna automáticamente; no puede contener varias líneas, ni sentencias como `if` con bloques, ni un `return` explícito.

!!! note "Una lambda casi nunca se guarda en una variable"

    El ejemplo anterior asigna la lambda a `cuadrado` solo para mostrar cómo se llama. En la práctica, una lambda se escribe directamente donde se necesita, sin asignarla a ningún nombre.

Su uso más común es como argumento de otra función, justo donde antes hacía falta definir una función aparte:

```python
numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda numero: numero ** 2, numeros))
pares = list(filter(lambda numero: numero % 2 == 0, numeros))

print(cuadrados)   # (1)!
print(pares)       # (2)!
```

1. `[1, 4, 9, 16, 25]` – la misma transformación de `map()`, sin necesidad de definir `elevar_al_cuadrado` aparte.
2. `[2, 4]` – lo mismo con `filter()`: la lambda retorna `True` o `False`, igual que hacía `es_par`.

`sorted()`, `min()` y `max()` reciben una lambda en `key` de la misma forma:

```python
palabras = ["kiwi", "mora", "arándano", "uva", "granadilla"]
ordenadas_por_longitud = sorted(palabras, key=lambda palabra: len(palabra))

print(ordenadas_por_longitud)
```

```title="Salida"
['uva', 'kiwi', 'mora', 'arándano', 'granadilla']
```

`reduce()` también acepta una lambda, aunque ahí la función necesita dos parámetros: el acumulado y el siguiente elemento.

```python
from functools import reduce

numeros = [1, 2, 3, 4]
total = reduce(lambda acumulado, numero: acumulado + numero, numeros)

print(total)   # (1)!
```

1. `10` – la misma idea de `reduce()`, con la función de combinación escrita inline en vez de definida por separado.

!!! warning "`def` sigue siendo la mejor opción casi siempre"

    Una lambda solo debería usarse cuando la función es realmente corta y se usa una única vez, como argumento de otra función. Si la lógica ocupa más de una línea, se reutiliza en varios lugares, o su nombre ayudaría a entender el código, un `def` sigue siendo más claro que una lambda.

## Comprensiones de listas

Con lambda ya no hace falta nombrar cada función, pero encadenar `filter()` y `map()` sigue leyéndose de afuera hacia adentro, en el orden contrario a como ocurren las cosas.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

cuadrados_de_pares = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numeros)))

print(cuadrados_de_pares)
```

Una **comprensión de listas** expresa la misma idea, transformar y filtrar, en una sola construcción que se lee de izquierda a derecha: primero qué se produce, después de dónde sale cada elemento.

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

cuadrados_de_pares = [n ** 2 for n in numeros if n % 2 == 0]

print(cuadrados_de_pares)   # (1)!
```

1. `[4, 16, 36, 64]` – el mismo resultado que el `map()`/`filter()` encadenado de arriba, en una sola expresión.

La sintaxis general es `[expresión for elemento in iterable]`; sin condición, equivale a un `map()`. Agregar `if elemento_cumple_condicion` al final filtra los elementos antes de transformarlos, igual que hacía `filter()`. La tabla siguiente compara ambos estilos sobre el mismo ejemplo:

| Con `map()` / `filter()`                                             | Con comprensión de listas                 |
| -------------------------------------------------------------------- | ----------------------------------------- |
| `list(map(lambda n: n ** 2, numeros))`                               | `[n ** 2 for n in numeros]`               |
| `list(filter(lambda n: n % 2 == 0, numeros))`                        | `[n for n in numeros if n % 2 == 0]`      |
| `list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numeros)))` | `[n ** 2 for n in numeros if n % 2 == 0]` |

!!! tip "La comprensión no siempre es la mejor opción"

    Una comprensión de listas es más clara cuando cabe cómodamente en una línea. Si la condición o la transformación se vuelven complejas, un `for` explícito, o una función con nombre pasada a `map()`/`filter()`, puede seguir siendo más fácil de leer que una comprensión larga y anidada.

## Expresiones generadoras

Una comprensión de listas construye la lista completa en memoria antes de poder usarla. Eso es razonable cuando la lista se va a recorrer varias veces o se necesita completa, pero es trabajo de más cuando el resultado solo se va a recorrer una vez, por ejemplo para sumarlo.

```python
numeros = range(1_000_000)

suma_de_cuadrados = sum([n ** 2 for n in numeros])   # (1)!
```

1. La comprensión entre corchetes construye una lista de un millón de elementos completa, solo para que `sum()` la recorra una vez y la descarte de inmediato.

Una **expresión generadora** usa exactamente la misma sintaxis que una comprensión de listas, pero con paréntesis en vez de corchetes, y no construye ninguna lista: produce cada valor uno a la vez, a medida que se necesita.

```python
numeros = range(1_000_000)

suma_de_cuadrados = sum(n ** 2 for n in numeros)   # (1)!

print(suma_de_cuadrados)
```

1. `sum()` recibe la expresión generadora directamente, sin corchetes ni paréntesis extra; en este caso, ni siquiera hacen falta los paréntesis del generador porque ya está dentro de los paréntesis de `sum(...)`.

```python
cuadrados_lista = [n ** 2 for n in range(5)]
cuadrados_generador = (n ** 2 for n in range(5))

print(type(cuadrados_lista))       # (1)!
print(type(cuadrados_generador))   # (2)!
```

1. `<class 'list'>` – la comprensión de listas ya tiene todos los valores calculados y guardados en memoria.
2. `<class 'generator'>` – el generador todavía no calculó ningún valor; solo sabe cómo producirlos cuando se le pidan.

!!! danger "Un generador solo se recorre una vez"

    A diferencia de una lista, un objeto generador se agota al recorrerlo. Iterarlo una segunda vez no produce ningún elemento, porque ya no quedan valores pendientes por generar.

    ```python
    cuadrados_generador = (n ** 2 for n in range(5))

    print(list(cuadrados_generador))   # (1)!
    print(list(cuadrados_generador))   # (2)!
    ```

    1. `[0, 1, 4, 9, 16]` – la primera vez, el generador produce todos sus valores.
    2. `[]` – la segunda vez, el generador ya está agotado y no queda nada por producir.

| Aspecto                    | Comprensión de listas `[...]`         | Expresión generadora `(...)`                                                          |
| -------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------- |
| Cuándo calcula los valores | Todos de inmediato, al crearse        | Uno por uno, solo cuando se piden                                                     |
| Memoria usada              | Toda la lista de una vez              | Un solo valor a la vez                                                                |
| Se puede recorrer          | Tantas veces como se quiera           | Una sola vez; después queda vacío                                                     |
| Se puede indexar (`[0]`)   | Sí                                    | No                                                                                    |
| Uso típico                 | Se necesita la lista completa después | El resultado se recorre o se agrega una sola vez, con `sum()`, `any()`, `all()`, etc. |

## Funciones `any()` y `all()`

Verificar si todas las notas de un curso aprueban, o si al menos una lectura supera un límite, son preguntas que también se resuelven sin `for` explícito, con dos funciones integradas que trabajan sobre valores booleanos.

- `all(iterable)` retorna `True` solo si todos los elementos son verdaderos.
- `any(iterable)` retorna `True` si al menos uno de los elementos es verdadero.

Ambas reciben típicamente una expresión generadora, y se detienen apenas conocen la respuesta: `all()` se detiene en el primer elemento falso, y `any()` en el primer elemento verdadero, sin recorrer el resto del iterable.

```python
notas = [85, 92, 74, 88, 70]

todas_aprueban = all(nota >= 70 for nota in notas)
alguna_es_perfecta = any(nota == 100 for nota in notas)

print(todas_aprueban)        # (1)!
print(alguna_es_perfecta)    # (2)!
```

1. `True` – ninguna nota es menor a 70, así que `all()` recorre la expresión generadora completa antes de confirmar el resultado.
2. `False` – ninguna nota vale 100, así que `any()` también debe recorrerla completa para descartar cada una.

## Ejercicios prácticos

### Palabras cortas con lambda

=== "Enunciado"
    Reescriba el filtro de palabras cortas usando `filter()` con una expresión lambda, sin definir ninguna función con `def`.

    1. Dada una lista de palabras, use `filter()` con una lambda que conserve solo las palabras de 4 caracteres o menos.
    2. Imprima la lista resultante convertida a `list`.

=== "Solución"
    ```python
    palabras = ["sol", "montaña", "río", "biblioteca", "paz", "computadora"]
    palabras_cortas = list(filter(lambda palabra: len(palabra) <= 4, palabras))

    print(palabras_cortas)
    ```

    !!! example "Caso de ejecución"

        ```
        ['sol', 'río', 'paz']
        ```

### Videos aptos para la lista de reproducción

=== "Enunciado"
    Una lista de reproducción para la clase solo debe incluir videos con una duración de entre 3 y 10 minutos, ambos incluidos.

    1. Escriba una comprensión de listas que produzca solo las duraciones (en minutos) dentro de ese rango.
    2. Imprima la lista resultante.

=== "Solución"
    ```python
    duraciones = [2, 5, 12, 8, 3, 15, 7]
    aptos = [duracion for duracion in duraciones if 3 <= duracion <= 10]

    print(aptos)
    ```

    !!! example "Caso de ejecución"

        ```
        [5, 8, 3, 7]
        ```

### ¿Todas las notas aprueban?

=== "Enunciado"
    Un curso aprueba una evaluación grupal solo si **todas** las notas individuales son mayores o iguales a 70.

    1. Use `all()` junto con una expresión generadora para verificar si todas las notas de una lista cumplen esa condición, sin construir ninguna lista intermedia.
    2. Imprima `True` o `False` según corresponda.

=== "Solución"
    ```python
    notas = [85, 92, 74, 88, 70]
    todas_aprueban = all(nota >= 70 for nota in notas)

    print(todas_aprueban)   # (1)!
    ```

    1. `True` – ninguna nota es menor a 70.

    !!! example "Caso de ejecución"

        ```
        True
        ```

## Ejercicio integrador — Catálogo de una tienda escolar

La tienda escolar necesita un programa para administrar su catálogo de productos: agregar productos, encontrar el más barato, filtrar los que ya casi no tienen existencias y calcular el valor total del inventario, sin escribir un `for` distinto para cada operación.

**Cada producto se representa como un diccionario:**

| Campo         | Descripción                           |
| ------------- | ------------------------------------- |
| `nombre`      | Texto con el nombre del producto      |
| `precio`      | Número, en colones                    |
| `existencias` | Número entero de unidades disponibles |

**Menú principal:**

```
=== CATÁLOGO DE LA TIENDA ===
1. Registrar producto
2. Ver catálogo ordenado por precio
3. Ver productos con pocas existencias (5 o menos)
4. Ver si todos los productos tienen existencias
5. Ver el valor total del inventario
6. Salir
```

**Requisitos:**

1. La opción 1 solicita nombre, precio y existencias, y valida con `try-except` que precio y existencias sean números; además, ambos deben ser mayores o iguales a cero.
2. La opción 2 usa `sorted()` con una expresión lambda en `key` para ordenar los productos por precio, de menor a mayor, y los muestra.
3. La opción 3 usa una comprensión de listas con condición para obtener solo los productos con 5 unidades o menos, y los muestra.
4. La opción 4 usa `all()` con una expresión generadora para verificar si **todos** los productos registrados tienen al menos una unidad disponible, sin construir ninguna lista intermedia.
5. La opción 5 usa una expresión generadora junto con `sum()` para calcular el valor total del inventario, multiplicando precio por existencias de cada producto.

### Solución

```python
productos = []

while True:
    print("\n=== CATÁLOGO DE LA TIENDA ===")
    print("1. Registrar producto")
    print("2. Ver catálogo ordenado por precio")
    print("3. Ver productos con pocas existencias (5 o menos)")
    print("4. Ver si todos los productos tienen existencias")
    print("5. Ver el valor total del inventario")
    print("6. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()

        try:
            precio = float(input("Precio: "))
            existencias = int(input("Existencias: "))
        except ValueError:
            print("Precio y existencias deben ser numéricos.")
            continue

        if precio < 0 or existencias < 0:
            print("Precio y existencias no pueden ser negativos.")
            continue

        productos.append({"nombre": nombre, "precio": precio, "existencias": existencias})
        print(f"Producto '{nombre}' registrado.")

    elif opcion == "2":
        if not productos:
            print("No hay productos registrados.")
            continue

        print("\n--- Catálogo ordenado por precio ---")
        for producto in sorted(productos, key=lambda p: p["precio"]):   # (1)!
            print(f"{producto['nombre']}: ₡{producto['precio']:,.2f} ({producto['existencias']} unidades)")

    elif opcion == "3":
        if not productos:
            print("No hay productos registrados.")
            continue

        pocas_existencias = [p for p in productos if p["existencias"] <= 5]   # (2)!

        if not pocas_existencias:
            print("Ningún producto tiene pocas existencias.")
            continue

        print("\n--- Productos con pocas existencias ---")
        for producto in pocas_existencias:
            print(f"{producto['nombre']}: {producto['existencias']} unidades")

    elif opcion == "4":
        if not productos:
            print("No hay productos registrados.")
            continue

        hay_existencias = all(p["existencias"] > 0 for p in productos)   # (3)!
        print(f"¿Todos los productos tienen existencias? {hay_existencias}")

    elif opcion == "5":
        if not productos:
            print("No hay productos registrados.")
            continue

        valor_total = sum(p["precio"] * p["existencias"] for p in productos)   # (4)!
        print(f"Valor total del inventario: ₡{valor_total:,.2f}")

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")
```

1. `key=lambda p: p["precio"]` le indica a `sorted()` que compare los diccionarios por su precio, sin necesidad de definir una función aparte solo para eso.
2. La comprensión de listas reemplaza un `filter()` con lambda: se lee de corrido como "cada producto de `productos` cuyas existencias sean 5 o menos".
3. `all()` evalúa la condición de existencias de cada producto, sin construir ninguna lista de verdaderos y falsos.
4. La expresión generadora produce un valor por producto (`precio * existencias`) que `sum()` va acumulando uno a uno, sin guardar la lista completa de esos productos en memoria.

!!! example "Casos de ejecución"

    === "Registro y catálogo"
        ```
        === CATÁLOGO DE LA TIENDA ===
        1. Registrar producto
        ...
        Opción: 1
        Nombre del producto: Cuaderno
        Precio: 1500
        Existencias: 20
        Producto 'Cuaderno' registrado.

        Opción: 1
        Nombre del producto: Lapicero
        Precio: 350
        Existencias: 3
        Producto 'Lapicero' registrado.

        Opción: 1
        Nombre del producto: Mochila
        Precio: 12000
        Existencias: 0
        Producto 'Mochila' registrado.

        Opción: 2

        --- Catálogo ordenado por precio ---
        Lapicero: ₡350.00 (3 unidades)
        Cuaderno: ₡1,500.00 (20 unidades)
        Mochila: ₡12,000.00 (0 unidades)
        ```
    === "Pocas existencias y disponibilidad"
        ```
        Opción: 3

        --- Productos con pocas existencias ---
        Lapicero: 3 unidades
        Mochila: 0 unidades

        Opción: 4
        ¿Todos los productos tienen existencias? False
        ```
    === "Valor del inventario"
        ```
        Opción: 5
        Valor total del inventario: ₡31,050.00
        ```
    === "Precio inválido"
        ```
        Opción: 1
        Nombre del producto: Borrador
        Precio: gratis
        Precio y existencias deben ser numéricos.
        ```
