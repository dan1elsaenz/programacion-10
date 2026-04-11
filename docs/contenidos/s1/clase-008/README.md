---
icon: material/table
---

# :material-table: Clase 8

## ¿Por qué necesitamos más de una dimensión?

Las listas permiten almacenar una colección de datos en una sola variable.
Pero hay situaciones donde los datos no se organizan en una fila, sino en una **tabla**: filas y columnas.

Suponga que se quieren guardar las notas de tres estudiantes en cuatro materias distintas:

| Estudiante | Matemática | Español | Ciencias | Historia |
| ---------- | ---------- | ------- | -------- | -------- |
| Ana        | 92         | 85      | 78       | 90       |
| Luis       | 74         | 68      | 81       | 72       |
| Sofía      | 88         | 95      | 91       | 87       |

Con listas separadas, el código quedaría así:

```python
notas_ana   = [92, 85, 78, 90]
notas_luis  = [74, 68, 81, 72]
notas_sofia = [88, 95, 91, 87]
```

!!! question "¿Qué pasa cuando los datos crecen?"

    Con treinta estudiantes y seis materias, habría que declarar treinta listas por separado. Cualquier operación sobre todos los datos requeriría repetir el mismo código treinta veces.

Lo que se necesita es una estructura que agrupe _todas las filas en una sola variable_ y permita recorrerlas de forma sistemática.
Esa estructura es la **matriz**.

## ¿Qué es una matriz?

Una **matriz** es una lista de listas. Cada elemento de la lista exterior representa una **fila**, y cada elemento dentro de esa fila representa una **columna**.

En Python, la tabla de notas anterior se puede representar así:

```python
notas = [
    [92, 85, 78, 90],  # (1)!
    [74, 68, 81, 72],  # (2)!
    [88, 95, 91, 87],  # (3)!
]
```

1. Fila 0 — notas de Ana.
2. Fila 1 — notas de Luis.
3. Fila 2 — notas de Sofía.

Ahora todos los datos viven en **una sola variable**. Para acceder a un elemento específico se usan dos índices: primero la fila y luego la columna.

```python
print(notas[0][2])  # (1)!
print(notas[2][1])  # (2)!
```

1. Fila 0, columna 2 → `78` (nota de Ana en Ciencias).
2. Fila 2, columna 1 → `95` (nota de Sofía en Español).

La notación `matriz[i][j]` se lee: **fila `i`, columna `j`**.

!!! note "Las filas no tienen que ser del mismo tamaño"

    Python no obliga a que todas las filas tengan la misma cantidad de elementos, pero usualmente se diseña para que sea así, pues resulta más fácil recorrerlos con `for` loops.

## Declaración e inicialización

### Manual

La forma más directa de crear una matriz es escribir todos sus valores explícitamente, fila por fila:

```python
tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

### Con ciclos

Cuando la matriz es grande o sus valores siguen un patrón, es más práctico generarla con ciclos.
El caso más común es crear una matriz **vacía** (rellena de ceros) para luego llenarla con datos:

```python
filas    = 3
columnas = 4
matriz   = []

for i in range(filas):          # (1)!
    fila = []
    for j in range(columnas):   # (2)!
        fila.append(0)
    matriz.append(fila)         # (3)!
```

1. El ciclo exterior recorre cada fila que se va a crear.
2. El ciclo interior llena esa fila con el valor inicial (en este caso, `0`).
3. La fila completa se agrega a la matriz.

El resultado es una matriz de 3 filas y 4 columnas, con todos sus elementos en cero:

```
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
```

!!! warning "Trampa común al inicializar matrices"

    Puede parecer tentador usar multiplicación de listas para crear la matriz:

    ```python
    matriz = [[0] * 4] * 3  # (1)!
    ```

    1. Esto parece crear 3 filas independientes, pero en realidad crea **3 referencias a la misma lista**. Modificar un elemento cambia la misma fila en las tres posiciones.

    La forma correcta siempre es usar el doble ciclo, que garantiza que cada fila sea una lista independiente.

### Acceso y modificación de elementos

Para leer un elemento se indica su fila y columna:

```python
print(matriz[1][2])  # (1)!
```

1. Lee el valor en fila 1, columna 2.

Modificar un elemento usa la misma notación en el lado izquierdo de una asignación:

```python
matriz[1][2] = 99  # (1)!
```

1. Reemplaza el valor en fila 1, columna 2 con `99`.

## Recorrido de una matriz

### Recorrido completo

Para visitar todos los elementos de una matriz se usan **dos ciclos anidados**: el exterior avanza por las filas y el interior recorre cada columna dentro de esa fila.

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for i in range(len(matriz)):            # (1)!
    for j in range(len(matriz[i])):     # (2)!
        print(matriz[i][j], end=" ")    # (3)!
    print()                             # (4)!
```

1. El ciclo exterior recorre el índice de fila `i`, de `0` hasta el número de filas menos uno.
2. El ciclo interior recorre el índice de columna `j`, de `0` hasta el número de columnas de esa fila menos uno.
3. Se imprime el elemento en la posición `[i][j]` seguido de un espacio, sin saltar de línea.
4. Al terminar cada fila, se imprime un salto de línea para pasar a la siguiente.

```
1 2 3
4 5 6
7 8 9
```

### Recorrido por filas

En ocasiones se necesita trabajar con una fila completa como si fuera una lista independiente. Python permite acceder directamente a ella con un solo índice:

```python
for fila in matriz:         # (1)!
    print(sum(fila))        # (2)!
```

1. En cada iteración, `fila` es la lista completa de esa fila: `[1, 2, 3]`, luego `[4, 5, 6]`, entre otros.
2. Se puede aplicar cualquier operación de lista, como `sum`, `max`, `min` o `len`.

```
6
15
24
```

### Recorrido por columnas

Recorrer columnas requiere fijar el índice de columna `j` y variar el de fila `i`:

```python
for j in range(len(matriz[0])):         # (1)!
    for i in range(len(matriz)):        # (2)!
        print(matriz[i][j], end=" ")
    print()
```

1. El ciclo exterior fija la columna `j`.
2. El ciclo interior recorre todas las filas para esa columna.

```
1 4 7
2 5 8
3 6 9
```

!!! tip "¿Cuándo recorrer por columnas?"

    El recorrido por columnas es útil cuando cada columna representa una categoría o materia y se quiere calcular un resultado por categoría: el promedio de cada materia, el máximo de cada columna, entre otros casos.

## Operaciones elementales

### Suma de todos los elementos

Para sumar todos los valores de una matriz se recorre elemento por elemento con el doble ciclo, acumulando en una variable:

```python
matriz = [
    [3, 7, 2],
    [8, 1, 5],
    [4, 6, 9],
]

total = 0
for fila in matriz:         # (1)!
    for elemento in fila:   # (2)!
        total += elemento

print(f"Suma total: {total}")
```

1. Cada `fila` es una lista; no se necesita el índice cuando solo se quiere el valor.
2. Cada `elemento` es un número de esa fila.

```
Suma total: 45
```

### Buscar el valor máximo y su posición

Encontrar el máximo requiere guardar no solo el valor, sino también su **posición** `(i, j)` dentro de la matriz:

```python
max_val = matriz[0][0]  # (1)!
max_i = 0
max_j = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > max_val:      # (2)!
            max_val = matriz[i][j]
            max_i = i
            max_j = j

print(f"Máximo: {max_val} en posición ({max_i}, {max_j})")
```

1. Se asume que el máximo inicial es el primer elemento. Así siempre hay un valor de comparación válido.
2. Si se encuentra un valor mayor, se actualiza el máximo y se guarda su posición.

```
Máximo: 9 en posición (2, 2)
```

### Promedio por fila

Calcular el promedio de cada fila de forma independiente es un caso muy frecuente: notas por estudiante, ventas por sucursal, temperaturas por día.

```python
for i in range(len(matriz)):
    promedio = sum(matriz[i]) / len(matriz[i])  # (1)!
    print(f"Fila {i}: promedio = {promedio:.1f}")
```

1. `sum` y `len` reciben la fila completa `matriz[i]`, que es una lista normal.

```
Fila 0: promedio = 4.0
Fila 1: promedio = 4.7
Fila 2: promedio = 6.3
```

## La matriz transpuesta

La **transpuesta** de una matriz es una nueva matriz donde las filas originales se convierten en columnas. El elemento que estaba en la posición `[i][j]` pasa a estar en la posición `[j][i]`.

=== "Original"

    ```
    1  2  3
    4  5  6
    ```

=== "Transpuesta"

    ```
    1  4
    2  5
    3  6
    ```

La matriz original tiene 2 filas y 3 columnas; su transpuesta tiene 3 filas y 2 columnas.

Para construirla se recorre la matriz original y se coloca cada elemento en su posición invertida:

```python
original = [
    [1, 2, 3],
    [4, 5, 6],
]

filas    = len(original)        # (1)!
columnas = len(original[0])     # (2)!

transpuesta = []
for j in range(columnas):       # (3)!
    fila_nueva = []
    for i in range(filas):      # (4)!
        fila_nueva.append(original[i][j])
    transpuesta.append(fila_nueva)

for fila in transpuesta:
    print(fila)
```

1. La matriz original tiene 2 filas.
2. La matriz original tiene 3 columnas.
3. El ciclo exterior itera sobre las **columnas** de la original, que se convierten en las **filas** de la transpuesta.
4. El ciclo interior toma el elemento `[i][j]` de la original y lo coloca en la nueva fila.

```
[1, 4]
[2, 5]
[3, 6]
```

## Ejercicio integrador

=== "Enunciado"

    Dos jugadores se turnan para jugar una partida de gato (tic-tac-toe).
    El programa debe gestionar el tablero, validar jugadas y determinar el resultado final.

    El programa debe cumplir con los siguientes requisitos:

    1. Definir una función `crear_tablero()` que retorne una matriz 3×3 inicializada con espacios vacíos.
    2. Definir una función `mostrar_tablero(tablero)` que imprima el tablero con separadores entre celdas y entre filas.
    3. Definir una función `hacer_jugada(tablero, fila, columna, ficha)` que coloque la ficha del jugador en la posición indicada. Si la celda ya está ocupada, debe retornar `False`; si la jugada es válida, debe realizarla y retornar `True`.
    4. Definir una función `hay_ganador(tablero, ficha)` que verifique si la ficha dada ocupa una fila completa, una columna completa o alguna de las dos diagonales. Retorna `True` si hay ganador, `False` en caso contrario.
    5. Definir una función `tablero_lleno(tablero)` que retorne `True` si no quedan celdas vacías.
    6. El programa principal debe alternar los turnos entre el jugador `"X"` y el jugador `"O"`, pedir fila y columna en cada turno (valores entre 1 y 3), validar la jugada, mostrar el tablero actualizado y anunciar el resultado al terminar.

=== "Solución"

    #### Paso 1: Crear y mostrar el tablero

    El tablero es una matriz 3×3 de espacios. La función de visualización agrega separadores para que sea legible.

    ```python
    def crear_tablero():
        tablero = []
        for i in range(3):          # (1)!
            fila = []
            for j in range(3):
                fila.append(" ")
            tablero.append(fila)
        return tablero


    def mostrar_tablero(tablero):
        print()
        for i in range(3):
            print(f" {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]} ")  # (2)!
            if i < 2:
                print("---+---+---")
        print()
    ```

    1. Cada celda se inicializa con un espacio `" "` para que el tablero se vea alineado al imprimirse.
    2. Las celdas de cada fila se separan con `|`; entre filas se imprime una línea de guiones.

    #### Paso 2: Validar y registrar una jugada

    ```python
    def hacer_jugada(tablero, fila, columna, ficha):
        if tablero[fila][columna] != " ":   # (1)!
            return False
        tablero[fila][columna] = ficha      # (2)!
        return True
    ```

    1. Si la celda no está vacía, la jugada es inválida y se retorna `False`.
    2. Se coloca la ficha directamente en la posición de la matriz y se retorna `True`.

    #### Paso 3: Verificar si hay ganador

    Se revisan las tres filas, las tres columnas y las dos diagonales:

    ```python
    def hay_ganador(tablero, ficha):
        for i in range(3):
            if all(tablero[i][j] == ficha for j in range(3)):  # (1)!
                return True
            if all(tablero[j][i] == ficha for j in range(3)):  # (2)!
                return True

        if all(tablero[i][i] == ficha for i in range(3)):      # (3)!
            return True
        if all(tablero[i][2 - i] == ficha for i in range(3)): # (4)!
            return True

        return False
    ```

    1. Revisa la fila `i`: las tres columnas deben tener la misma ficha.
    2. Revisa la columna `i`: las tres filas en esa columna deben tener la misma ficha.
    3. Diagonal principal: posiciones `[0][0]`, `[1][1]`, `[2][2]`.
    4. Diagonal secundaria: posiciones `[0][2]`, `[1][1]`, `[2][0]`.

    #### Paso 4: Verificar tablero lleno

    ```python
    def tablero_lleno(tablero):
        for fila in tablero:
            if " " in fila:     # (1)!
                return False
        return True
    ```

    1. Si alguna fila contiene al menos un espacio vacío, el tablero no está lleno.

    #### Paso 5: Programa principal

    El ciclo principal alterna turnos, pide la jugada, la valida y verifica el estado del juego tras cada movimiento:

    ```python
    def jugar():
        tablero = crear_tablero()
        turno   = 0
        fichas  = ["X", "O"]

        while True:
            ficha = fichas[turno % 2]           # (1)!
            mostrar_tablero(tablero)
            print(f"Turno del jugador {ficha}")

            while True:                         # (2)!
                try:
                    fila    = int(input("Fila (1-3): ")) - 1
                    columna = int(input("Columna (1-3): ")) - 1
                    if fila not in range(3) or columna not in range(3):
                        print("Posición fuera del tablero. Intente de nuevo.")
                    elif not hacer_jugada(tablero, fila, columna, ficha):
                        print("Esa celda ya está ocupada. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero.")

            if hay_ganador(tablero, ficha):     # (3)!
                mostrar_tablero(tablero)
                print(f"¡El jugador {ficha} gana!")
                break

            if tablero_lleno(tablero):          # (4)!
                mostrar_tablero(tablero)
                print("¡Empate!")
                break

            turno += 1
    ```

    1. El módulo `% 2` alterna entre `0` y `1`, seleccionando `"X"` o `"O"` en cada turno.
    2. El ciclo interno repite el pedido de jugada hasta que el dato ingresado sea válido y la celda esté libre.
    3. Se verifica el ganador inmediatamente después de cada jugada válida.
    4. Si no hay ganador pero el tablero está lleno, el juego termina en empate.

    #### Programa completo

    ```python
    def crear_tablero():
        tablero = []
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append(" ")
            tablero.append(fila)
        return tablero


    def mostrar_tablero(tablero):
        print()
        for i in range(3):
            print(f" {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]} ")
            if i < 2:
                print("---+---+---")
        print()


    def hacer_jugada(tablero, fila, columna, ficha):
        if tablero[fila][columna] != " ":
            return False
        tablero[fila][columna] = ficha
        return True


    def hay_ganador(tablero, ficha):
        for i in range(3):
            if all(tablero[i][j] == ficha for j in range(3)):
                return True
            if all(tablero[j][i] == ficha for j in range(3)):
                return True

        if all(tablero[i][i] == ficha for i in range(3)):
            return True
        if all(tablero[i][2 - i] == ficha for i in range(3)):
            return True

        return False


    def tablero_lleno(tablero):
        for fila in tablero:
            if " " in fila:
                return False
        return True


    def jugar():
        tablero = crear_tablero()
        turno   = 0
        fichas  = ["X", "O"]

        while True:
            ficha = fichas[turno % 2]
            mostrar_tablero(tablero)
            print(f"Turno del jugador {ficha}")

            while True:
                try:
                    fila    = int(input("Fila (1-3): ")) - 1
                    columna = int(input("Columna (1-3): ")) - 1
                    if fila not in range(3) or columna not in range(3):
                        print("Posición fuera del tablero. Intente de nuevo.")
                    elif not hacer_jugada(tablero, fila, columna, ficha):
                        print("Esa celda ya está ocupada. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero.")

            if hay_ganador(tablero, ficha):
                mostrar_tablero(tablero)
                print(f"¡El jugador {ficha} gana!")
                break

            if tablero_lleno(tablero):
                mostrar_tablero(tablero)
                print("¡Empate!")
                break

            turno += 1


    jugar()
    ```

    !!! example "Ejemplos de ejecución"

        === "Victoria de X"

            ```
             X | O | O
            ---+---+---
               | X |
            ---+---+---
               |   | X

            ¡El jugador X gana!
            ```

        === "Empate"

            ```
             X | O | X
            ---+---+---
             X | X | O
            ---+---+---
             O | X | O

            ¡Empate!
            ```

        === "Celda ocupada"

            ```
            Turno del jugador O
            Fila (1-3): 1
            Columna (1-3): 1
            Esa celda ya está ocupada. Intente de nuevo.
            Fila (1-3): 2
            Columna (1-3): 3
            ```
