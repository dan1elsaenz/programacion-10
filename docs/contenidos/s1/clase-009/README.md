---
icon: material/book-open-variant
---

# :material-book-open-variant: Clase 9

## Diccionarios en Python

### Concepto de diccionario y pares clave–valor

Hasta ahora, las listas y matrices almacenan datos accesibles por su **posición numérica**: `notas[0]`, `matriz[2][1]`.
Eso funciona bien cuando el orden importa, pero hay situaciones donde lo natural es buscar por un **nombre**, no por un número.

Para guardar la información de un estudiante: nombre, edad, nota promedio y carné, con una lista, habría que recordar que el índice `0` es el nombre, el `1` es la edad y así sucesivamente.
El código pierde claridad y se vuelve frágil si el orden cambia.

Un **diccionario** resuelve esto.
Es una estructura que asocia cada dato con una **clave** descriptiva, formando pares **clave–valor**.
La clave es el nombre con el que se identifica el dato; el valor es el dato en sí.

```
clave      ->  valor
"nombre"   ->  "Ana"
"edad"     ->  17
"promedio" ->  91.5
```

!!! note "Los diccionarios no tienen un orden de posición"

    A diferencia de las listas, los elementos de un diccionario no se acceden por índice numérico.
    Se acceden por su clave, que puede ser cualquier texto o número.

### Creación, acceso y modificación de elementos

#### Creación

Un diccionario se declara con llaves `{}`.
Cada par clave–valor se escribe como `clave: valor` y los pares se separan con comas:

```python
estudiante = {
    "nombre":   "Ana",      # (1)!
    "edad":     17,         # (2)!
    "promedio": 91.5,       # (3)!
}
```

1. La clave `"nombre"` apunta al valor `"Ana"`.
2. La clave `"edad"` apunta al entero `17`.
3. Las claves suelen ser cadenas de texto; los valores pueden ser de cualquier tipo.

Para crear un diccionario vacío y llenarlo después se usa `{}` o `dict()`:

```python
inventario = {}
```

#### Acceso por clave

Para leer el valor asociado a una clave se usan corchetes, igual que con las listas, pero con la clave en lugar de un índice:

```python
print(estudiante["nombre"])    # (1)!
print(estudiante["promedio"])  # (2)!
```

1. Imprime `Ana`.
2. Imprime `91.5`.

!!! warning "Clave inexistente"

    Si se accede a una clave que no existe en el diccionario, Python lanza un `KeyError`.
    Para evitarlo se puede usar el método `.get()`, que retorna `None` (o un valor por defecto) si la clave no existe:

    ```python
    print(estudiante.get("carnet"))          # Retorna None sin error.
    print(estudiante.get("carnet", "N/A"))   # Retorna "N/A" como valor por defecto.
    ```

    > Esta es considerada mejor práctica que el acceso directo con `[]`.

#### Modificación y adición de elementos

Modificar un valor existente o añadir un par nuevo usa la misma sintaxis de asignación:

```python
estudiante["edad"] = 18              # (1)!
estudiante["carnet"] = "2024-0042"   # (2)!
```

1. Actualiza el valor de la clave `"edad"` de `17` a `18`.
2. Como `"carnet"` no existía, Python la crea y le asigna el valor.

#### Eliminación de elementos

Para eliminar un par clave–valor se usa `del`:

```python
del estudiante["carnet"]  # (1)!
```

1. Elimina la clave `"carnet"` y su valor del diccionario.

### Recorrido de diccionarios

Un diccionario puede recorrerse de tres formas distintas dependiendo de qué se necesite: solo las claves, solo los valores, o ambos al mismo tiempo.

#### Solo claves

```python
calificaciones = {
    "Matemática": 88,
    "Español":    75,
    "Ciencias":   92,
}

for materia in calificaciones:          # (1)!
    print(materia)
```

1. Recorrer un diccionario directamente entrega sus **claves**, una por iteración.

```
Matemática
Español
Ciencias
```

#### Solo valores

```python
for nota in calificaciones.values():    # (1)!
    print(nota)
```

1. `.values()` entrega únicamente los valores del diccionario.

```
88
75
92
```

#### Claves y valores juntos

La forma más útil en la mayoría de los casos es recorrer ambos al mismo tiempo con `.items()`:

```python
for materia, nota in calificaciones.items():    # (1)!
    print(f"{materia}: {nota}")
```

1. `.items()` entrega cada par como una tupla `(clave, valor)`, que se puede desempacar directamente en dos variables.

```
Matemática: 88
Español: 75
Ciencias: 92
```

!!! tip "Verificar si una clave existe"

    Antes de acceder a una clave, se puede comprobar si existe con el operador `in`:

    ```python
    if "Historia" in calificaciones:
        print(calificaciones["Historia"])
    else:
        print("La materia no está registrada.")
    ```

### Métodos principales

Python incluye un conjunto de métodos integrados para trabajar con diccionarios. La siguiente tabla presenta los más utilizados:

| Método / Operación      | Descripción                                                                 |
| ----------------------- | --------------------------------------------------------------------------- |
| `d[clave]`              | Accede al valor. Lanza `KeyError` si la clave no existe.                    |
| `d.get(clave, defecto)` | Accede al valor. Retorna `defecto` (o `None`) si no existe.                 |
| `d[clave] = valor`      | Agrega o actualiza un par clave–valor.                                      |
| `del d[clave]`          | Elimina el par con esa clave.                                               |
| `d.pop(clave)`          | Elimina y **retorna** el valor asociado a la clave.                         |
| `d.keys()`              | Retorna una vista con todas las claves.                                     |
| `d.values()`            | Retorna una vista con todos los valores.                                    |
| `d.items()`             | Retorna una vista con todos los pares `(clave, valor)`.                     |
| `d.update(otro)`        | Copia los pares de `otro` en `d`, sobreescribiendo si hay claves repetidas. |
| `d.clear()`             | Elimina todos los pares del diccionario.                                    |
| `clave in d`            | Retorna `True` si la clave existe en el diccionario.                        |
| `len(d)`                | Retorna el número de pares clave–valor.                                     |

A continuación se muestra cada método en uso:

```python
alumno = {"nombre": "Luis", "edad": 16, "nota": 78}

# get: acceso seguro
print(alumno.get("carnet", "sin carnet"))   # (1)!

# pop: eliminar y obtener el valor
edad = alumno.pop("edad")                   # (2)!
print(edad)

# update: incorporar nuevos pares
alumno.update({"edad": 17, "carnet": "2024-0011"})  # (3)!
print(alumno)

# keys, values, items
print(list(alumno.keys()))    # (4)!
print(list(alumno.values()))  # (5)!

# in y len
print("nota" in alumno)       # (6)!
print(len(alumno))            # (7)!

# clear
alumno.clear()
print(alumno)                 # (8)!
```

1. `"carnet"` no existe, así que retorna el valor por defecto `"sin carnet"`.
2. Elimina la clave `"edad"` del diccionario y guarda su valor (`16`) en la variable `edad`.
3. `update` agrega `"carnet"` y sobreescribe `"edad"` con el nuevo valor `17`.
4. Lista de claves: `['nombre', 'nota', 'edad', 'carnet']`.
5. Lista de valores: `['Luis', 78, 17, '2024-0011']`.
6. `True`, porque `"nota"` sí existe como clave.
7. El diccionario tiene 4 pares en este momento.
8. El diccionario queda vacío `{}`.

```
sin carnet
16
{'nombre': 'Luis', 'nota': 78, 'edad': 17, 'carnet': '2024-0011'}
['nombre', 'nota', 'edad', 'carnet']
['Luis', 78, 17, '2024-0011']
True
4
{}
```

### Casos de uso frecuentes

Los diccionarios son la herramienta natural cuando los datos tienen **nombre propio** y no dependen de su posición.
A continuación se presentan los patrones más comunes.

#### Conteo de frecuencias

Contar cuántas veces aparece cada elemento en una lista es una operación muy frecuente: letras en una palabra, respuestas en una encuesta, productos en una venta.

```python
respuestas = ["A", "B", "A", "C", "A", "B", "C", "C", "C"]

conteo = {}
for respuesta in respuestas:
    if respuesta in conteo:         # (1)!
        conteo[respuesta] += 1
    else:
        conteo[respuesta] = 1       # (2)!

for opcion, cantidad in conteo.items():
    print(f"Opción {opcion}: {cantidad} voto(s)")
```

1. Si la clave ya existe, se incrementa su contador.
2. Si la clave no existe todavía, se inicializa en `1`.

```
Opción A: 3 voto(s)
Opción B: 2 voto(s)
Opción C: 4 voto(s)
```

#### Agrupación de datos

Un diccionario puede almacenar listas como valores, lo que permite agrupar múltiples datos bajo una misma clave:

```python
grupos = {
    "Grupo A": ["Ana", "Luis", "María"],
    "Grupo B": ["Carlos", "Sofía"],
    "Grupo C": ["Pedro", "Elena", "Tomás"],
}

for grupo, integrantes in grupos.items():
    print(f"{grupo} ({len(integrantes)} personas): {', '.join(integrantes)}")
```

```
Grupo A (3 personas): Ana, Luis, María
Grupo B (2 personas): Carlos, Sofía
Grupo C (3 personas): Pedro, Elena, Tomás
```

#### Lista de diccionarios

Cuando se maneja una colección de entidades del mismo tipo (varios estudiantes, varios productos, varios contactos) se usa una **lista de diccionarios**.
Cada diccionario representa un registro completo:

```python
productos = [
    {"nombre": "Cuaderno", "precio": 850,  "stock": 40},
    {"nombre": "Lápiz",    "precio": 200,  "stock": 120},
    {"nombre": "Borrador", "precio": 150,  "stock": 75},
]

for producto in productos:  # (1)!
    print(f"{producto['nombre']:10} ₡{producto['precio']:>6}  ({producto['stock']} unidades)")
```

1. Cada `producto` es un diccionario; se accede a sus campos por nombre.

```
Cuaderno   ₡   850  (40 unidades)
Lápiz      ₡   200  (120 unidades)
Borrador   ₡   150  (75 unidades)
```

## Ejercicio integrador

=== "Enunciado"

    El kiosco del colegio necesita un sistema para controlar su inventario de productos.
    El encargado debe poder registrar artículos, procesar ventas y detectar cuáles se han agotado.

    El programa debe cumplir con los siguientes requisitos:

    1. Definir una función `agregar_producto(inventario, nombre, precio, stock)` que agregue o actualice un producto en el inventario. Cada producto se representa como un diccionario con las claves `"precio"` y `"stock"`.
    2. Definir una función `realizar_venta(inventario, nombre, cantidad)` que verifique si el producto existe y tiene stock suficiente. Si la venta es posible, debe descontar la cantidad del stock y retornar el total cobrado (precio × cantidad). Si no es posible, debe retornar `None`.
    3. Definir una función `productos_agotados(inventario)` que retorne una lista con los nombres de los productos cuyo stock sea `0`.
    4. Definir una función `mostrar_inventario(inventario)` que imprima una tabla con el nombre, precio y stock de cada producto. Los productos con stock `0` deben mostrar `"AGOTADO"` en lugar del número.
    5. El programa principal debe cargar al menos cuatro productos, procesar varias ventas (algunas válidas y otras no), mostrar los productos agotados y desplegar el inventario final.

=== "Solución"

    #### Paso 1: Agregar un producto

    Cada producto se almacena como un diccionario anidado dentro del inventario principal:

    ```python
    def agregar_producto(inventario, nombre, precio, stock):
        inventario[nombre] = {"precio": precio, "stock": stock}  # (1)!
    ```

    1. Si `nombre` ya existe como clave, sobreescribe sus datos. Si no existe, lo crea. El diccionario interno agrupa los atributos del producto bajo una misma clave.

    #### Paso 2: Procesar una venta

    Antes de descontar del stock se validan dos condiciones: que el producto exista y que haya suficiente cantidad.

    ```python
    def realizar_venta(inventario, nombre, cantidad):
        if nombre not in inventario:            # (1)!
            return None
        producto = inventario[nombre]
        if producto["stock"] < cantidad:        # (2)!
            return None
        producto["stock"] -= cantidad           # (3)!
        return producto["precio"] * cantidad
    ```

    1. Se verifica la existencia de la clave antes de acceder para evitar un `KeyError`.
    2. Si el stock disponible es menor que la cantidad solicitada, la venta no puede realizarse.
    3. Se descuenta la cantidad vendida directamente del diccionario anidado.

    #### Paso 3: Detectar productos agotados

    Se recorre el inventario con `.items()` y se acumulan los nombres con stock igual a `0`:

    ```python
    def productos_agotados(inventario):
        agotados = []
        for nombre, datos in inventario.items():    # (1)!
            if datos["stock"] == 0:
                agotados.append(nombre)
        return agotados
    ```

    1. `datos` es el diccionario interno `{"precio": ..., "stock": ...}` de cada producto.

    #### Paso 4: Mostrar el inventario

    ```python
    def mostrar_inventario(inventario):
        print(f"\n{'Producto':<12} {'Precio':>8} {'Stock':>8}")
        print("-" * 30)
        for nombre, datos in inventario.items():
            stock = "AGOTADO" if datos["stock"] == 0 else str(datos["stock"])  # (1)!
            print(f"{nombre:<12} ₡{datos['precio']:>7} {stock:>8}")
    ```

    1. Una expresión condicional decide si mostrar el número de unidades o la etiqueta `"AGOTADO"`.

    #### Programa completo

    ```python
    def agregar_producto(inventario, nombre, precio, stock):
        inventario[nombre] = {"precio": precio, "stock": stock}


    def realizar_venta(inventario, nombre, cantidad):
        if nombre not in inventario:
            return None
        producto = inventario[nombre]
        if producto["stock"] < cantidad:
            return None
        producto["stock"] -= cantidad
        return producto["precio"] * cantidad


    def productos_agotados(inventario):
        agotados = []
        for nombre, datos in inventario.items():
            if datos["stock"] == 0:
                agotados.append(nombre)
        return agotados


    def mostrar_inventario(inventario):
        print(f"\n{'Producto':<12} {'Precio':>8} {'Stock':>8}")
        print("-" * 30)
        for nombre, datos in inventario.items():
            stock = "AGOTADO" if datos["stock"] == 0 else str(datos["stock"])
            print(f"{nombre:<12} ₡{datos['precio']:>7} {stock:>8}")


    # Programa principal
    inventario = {}

    agregar_producto(inventario, "Refresco", 500, 20)
    agregar_producto(inventario, "Empanada", 350, 15)
    agregar_producto(inventario, "Galletas", 200,  8)
    agregar_producto(inventario, "Agua",     300,  5)

    total = realizar_venta(inventario, "Refresco", 3)
    print(f"Venta de Refresco: ₡{total}")

    total = realizar_venta(inventario, "Agua", 5)
    print(f"Venta de Agua: ₡{total}")

    total = realizar_venta(inventario, "Agua", 2)
    if total is None:
        print("Venta de Agua: stock insuficiente.")

    total = realizar_venta(inventario, "Jugo", 1)
    if total is None:
        print("Venta de Jugo: producto no encontrado.")

    agotados = productos_agotados(inventario)
    if agotados:
        print(f"\nProductos agotados: {', '.join(agotados)}")

    mostrar_inventario(inventario)
    ```

    !!! example "Ejemplos de ejecución"

        === "Ejecución normal"

            ```
            Venta de Refresco: ₡1500
            Venta de Agua: ₡1500
            Venta de Agua: stock insuficiente.
            Venta de Jugo: producto no encontrado.

            Productos agotados: Agua

            Producto      Precio    Stock
            ------------------------------
            Refresco      ₡    500       17
            Empanada      ₡    350       15
            Galletas      ₡    200        8
            Agua          ₡    300  AGOTADO
            ```

        === "Sin productos agotados"

            Si todas las ventas tienen stock suficiente, no se imprime la sección de agotados:

            ```
            Venta de Refresco: ₡500

            Producto      Precio    Stock
            ------------------------------
            Refresco      ₡    500       19
            Empanada      ₡    350       15
            Galletas      ₡    200        8
            Agua          ₡    300        5
            ```

## Ejercicios

### 1. Anagramas

Dos palabras son **anagramas** si contienen exactamente los mismos caracteres con la misma frecuencia.
Dado dos palabras, determinar si son anagramas entre sí.

=== "Enunciado"

    **Entrada:** dos palabras en minúsculas, una por línea.

    **Salida:** `SI` si son anagramas, `NO` en caso contrario.

    | Entrada | Salida |
    |---------|--------|
    | `listen` <br> `silent` | `SI` |
    | `amor` <br> `roma` | `SI` |
    | `hola` <br> `mundo` | `NO` |

=== "Solución"

    Se construye un diccionario de frecuencias para cada palabra y se comparan directamente.
    Si son iguales, las palabras son anagramas.

    ```python
    def frecuencias(palabra):
        conteo = {}
        for letra in palabra:
            conteo[letra] = conteo.get(letra, 0) + 1  # (1)!
        return conteo

    a = input()
    b = input()

    if frecuencias(a) == frecuencias(b):  # (2)!
        print("SI")
    else:
        print("NO")
    ```

    1. `.get(letra, 0)` evita el `KeyError` cuando la letra aparece por primera vez.
    2. Comparar dos diccionarios en Python verifica que tengan exactamente las mismas claves y valores.

    !!! example "Ejecución"

        === "Son anagramas"

            ```
            listen
            silent
            SI
            ```

        === "No son anagramas"

            ```
            hola
            mundo
            NO
            ```

### 2. Dos sumas

Dado una lista de N enteros y un objetivo T, encontrar dos números en la lista que sumen exactamente T e imprimir sus **índices** (el menor primero).
Se garantiza que siempre existe exactamente una solución.

=== "Enunciado"

    **Entrada:**

    - Primera línea: N (cantidad de números) y T (objetivo), separados por espacio.
    - Segunda línea: N enteros separados por espacio.

    **Salida:** los dos índices separados por espacio.

    | Entrada | Salida |
    |---------|--------|
    | `4 9` <br> `2 7 11 15` | `0 1` |
    | `3 6` <br> `3 2 4` | `1 2` |
    | `2 6` <br> `3 3` | `0 1` |

=== "Solución"

    Para cada número `x`, el complemento necesario es `T - x`.
    El diccionario guarda `valor → índice` de los números ya procesados. Si el complemento ya está registrado, se encontró la pareja.

    ```python
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))

    vistos = {}  # (1)!

    for i, x in enumerate(nums):
        complemento = t - x
        if complemento in vistos:       # (2)!
            print(vistos[complemento], i)
            break
        vistos[x] = i                   # (3)!
    ```

    1. `vistos` mapea cada número a su índice a medida que se recorre la lista.
    2. Si el complemento necesario ya fue visto, la pareja es `(índice del complemento, índice actual)`.
    3. Si no se encontró complemento aún, se registra el número actual para consultas futuras.

    !!! example "Ejecución"

        === "Caso 1"

            ```
            4 9
            2 7 11 15
            0 1
            ```

        === "Caso 2"

            ```
            3 6
            3 2 4
            1 2
            ```

### 3. Diccionario inverso

Dado N pares clave–valor, construir el diccionario inverso (intercambiar claves por valores).
Si algún valor se repite en el original, el inverso no es posible: imprimir `NO INVERTIBLE`.

=== "Enunciado"

    **Entrada:**

    - Primera línea: N (cantidad de pares).
    - Las siguientes N líneas: cada una con una clave y un valor separados por espacio.

    **Salida:** Si es invertible, los pares del diccionario inverso ordenados alfabéticamente por clave (nuevo), uno por línea con formato `clave: valor`. Si no, imprimir `NO INVERTIBLE`.

    | Entrada | Salida |
    |---------|--------|
    | `3` <br> `a 1` <br> `b 2` <br> `c 3` | `1: a` <br> `2: b` <br> `3: c` |
    | `3` <br> `x rojo` <br> `y azul` <br> `z rojo` | `NO INVERTIBLE` |

=== "Solución"

    Se recorre la lista de pares y se va construyendo el diccionario inverso. Si un valor ya fue usado como clave en el inverso, significa que está repetido y no se puede invertir.

    ```python
    n = int(input())

    inverso = {}
    invertible = True

    for _ in range(n):
        clave, valor = input().split()
        if valor in inverso:            # (1)!
            invertible = False
            break
        inverso[valor] = clave          # (2)!

    if not invertible:
        print("NO INVERTIBLE")
    else:
        for k in sorted(inverso):       # (3)!
            print(f"{k}: {inverso[k]}")
    ```

    1. Si el valor ya existe como clave en el inverso, hay una colisión: el diccionario no es invertible.
    2. Se intercambian los roles: el valor original se convierte en la nueva clave y viceversa.
    3. `sorted` ordena las claves alfabéticamente para una salida consistente.

    !!! example "Ejecución"

        === "Invertible"

            ```
            3
            a 1
            b 2
            c 3
            1: a
            2: b
            3: c
            ```

        === "No invertible"

            ```
            3
            x rojo
            y azul
            z rojo
            NO INVERTIBLE
            ```

### 4. Conexiones directas

Se registran R rutas de vuelo unidireccionales entre ciudades.
Luego llegan Q consultas preguntando si existe un vuelo directo entre dos ciudades.
Responder cada consulta.

=== "Enunciado"

    **Entrada:**

    - Primera línea: R (rutas) y Q (consultas), separados por espacio.
    - Las siguientes R líneas: cada una con dos ciudades `A B` (vuelo directo de A hacia B).
    - Las siguientes Q líneas: cada una con dos ciudades `X Y` (¿hay vuelo directo de X a Y?).

    **Salida:** Q líneas, cada una con `SI` o `NO`.

    **Ejemplo de entrada:**
    ```
    4 3
    SJO MIA
    SJO BOG
    MIA NYC
    BOG LIM
    SJO MIA
    MIA SJO
    BOG LIM
    ```

    **Ejemplo de salida:**
    ```
    SI
    NO
    SI
    ```

=== "Solución"

    Las rutas se almacenan en un diccionario donde cada clave es una ciudad de origen y su valor es el conjunto de destinos directos.
    Para responder cada consulta basta con verificar si el destino está en ese conjunto.

    ```python
    r, q = map(int, input().split())

    rutas = {}                                  # (1)!
    for _ in range(r):
        origen, destino = input().split()
        if origen not in rutas:
            rutas[origen] = set()
        rutas[origen].add(destino)              # (2)!

    for _ in range(q):
        x, y = input().split()
        if x in rutas and y in rutas[x]:        # (3)!
            print("SI")
        else:
            print("NO")
    ```

    1. `rutas` mapea cada ciudad de origen al conjunto de sus destinos directos.
    2. Se usa un `set` para que agregar la misma ruta dos veces no la duplique.
    3. Primero se verifica que la ciudad de origen tenga rutas registradas, luego que el destino específico esté entre ellas.

    !!! example "Ejecución"

        ```
        4 3
        SJO MIA
        SJO BOG
        MIA NYC
        BOG LIM
        SJO MIA
        MIA SJO
        BOG LIM
        SI
        NO
        SI
        ```

### 5. Traductor de oraciones

Dado un diccionario de traducción y una oración, traducir cada palabra que aparezca en el diccionario.
Las palabras que no estén registradas se dejan tal cual.

=== "Enunciado"

    **Entrada:**

    - Primera línea: N (cantidad de pares de traducción).
    - Las siguientes N líneas: cada una con la palabra original y su traducción separadas por espacio.
    - Última línea: la oración a traducir (palabras en minúsculas separadas por espacio).

    **Salida:** La oración traducida en una sola línea.

    **Ejemplo de entrada:**
    ```
    4
    cat gato
    dog perro
    house casa
    sun sol
    the cat and the dog are in the house
    ```

    **Ejemplo de salida:**
    ```
    the gato and the perro are in the casa
    ```

=== "Solución"

    Se carga el diccionario de traducción y luego se recorre la oración palabra por palabra.
    Para cada palabra, `.get()` retorna la traducción si existe o la palabra original si no está registrada.

    ```python
    n = int(input())

    traduccion = {}
    for _ in range(n):
        original, traducida = input().split()
        traduccion[original] = traducida        # (1)!

    oracion = input().split()

    resultado = []
    for palabra in oracion:
        resultado.append(traduccion.get(palabra, palabra))  # (2)!

    print(" ".join(resultado))
    ```

    1. El diccionario asocia cada palabra original con su traducción.
    2. `.get(palabra, palabra)` intenta traducir; si la clave no existe, devuelve la palabra sin cambios como valor por defecto.

    !!! example "Ejecución"

        === "Traducción parcial"

            ```
            4
            cat gato
            dog perro
            house casa
            sun sol
            the cat and the dog are in the house
            the gato and the perro are in the casa
            ```

        === "Sin palabras conocidas"

            ```
            2
            hello hola
            bye adios
            this is a test
            this is a test
            ```
