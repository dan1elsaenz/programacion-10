---
icon: material/pencil
---

# :material-pencil: Quiz 3

!!! abstract "Instrucciones generales"

    - El ejercicio debe resolverse en un archivo `quiz3_NombreApellido.py`.
    - El programa debe ejecutarse sin errores y producir exactamente la salida indicada.
    - La entrada siempre será válida; no es necesario validar datos.

## Ejercicio: Vagones del tren

Un tren tiene **N vagones** numerados del 1 al N, todos vacíos al inicio.
A lo largo del viaje se realizan dos tipos de operaciones:

- **Operación `A p v`**: Agregar `v` unidades de carga a cada uno de los vagones del 1 al `p`.
- **Operación `C p`**: Consultar cuántas unidades de carga tiene actualmente el vagón `p`.

El programa debe leer todas las operaciones y, por cada operación `C`, imprimir en una línea el resultado de la consulta.

Se debe implementar un enfoque basado en funciones de Python.

### Entrada

- Primera línea: entero `N` (cantidad de vagones, 1 ≤ N ≤ 100).
- Segunda línea: entero `Q` (cantidad de operaciones, 1 ≤ Q ≤ 50).
- Las siguientes `Q` líneas contienen una operación cada una:
    - `A p v` con 1 ≤ p ≤ N y 1 ≤ v ≤ 1000.
    - `C p` con 1 ≤ p ≤ N.

### Salida

Una línea por cada operación `C` con el valor de carga del vagón consultado.

### Ejemplos de ejecución esperada

=== "Caso 1"

    ```title="Entrada"
    5
    8
    A 3 2
    C 2
    A 4 1
    C 2
    C 4
    A 2 3
    C 1
    C 5
    ```

    ```title="Salida"
    2
    3
    1
    6
    0
    ```

    !!! example "Guía de ejecución"

        El tren tiene 5 vagones. El estado inicial es `[0, 0, 0, 0, 0]`.

        | Operación | Vagón 1 | Vagón 2 | Vagón 3 | Vagón 4 | Vagón 5 | Salida |
        | --------- | ------- | ------- | ------- | ------- | ------- | ------ |
        | Inicio    | 0       | 0       | 0       | 0       | 0       |        |
        | `A 3 2`   | 2       | 2       | 2       | 0       | 0       |        |
        | `C 2`     | 2       | 2       | 2       | 0       | 0       | **2**  |
        | `A 4 1`   | 3       | 3       | 3       | 1       | 0       |        |
        | `C 2`     | 3       | 3       | 3       | 1       | 0       | **3**  |
        | `C 4`     | 3       | 3       | 3       | 1       | 0       | **1**  |
        | `A 2 3`   | 6       | 6       | 3       | 1       | 0       |        |
        | `C 1`     | 6       | 6       | 3       | 1       | 0       | **6**  |
        | `C 5`     | 6       | 6       | 3       | 1       | 0       | **0**  |

=== "Caso 2"

    ```title="Entrada"
    4
    5
    A 4 10
    C 1
    A 2 5
    C 3
    C 4
    ```

    ```title="Salida"
    10
    10
    10
    ```

    !!! example "Guía de ejecución"

        El tren tiene 4 vagones. El estado inicial es `[0, 0, 0, 0]`.

        | Operación | Vagón 1 | Vagón 2 | Vagón 3 | Vagón 4 | Salida |
        | --------- | ------- | ------- | ------- | ------- | ------ |
        | Inicio    | 0       | 0       | 0       | 0       |        |
        | `A 4 10`  | 10      | 10      | 10      | 10      |        |
        | `C 1`     | 10      | 10      | 10      | 10      | **10** |
        | `A 2 5`   | 15      | 15      | 10      | 10      |        |
        | `C 3`     | 15      | 15      | 10      | 10      | **10** |
        | `C 4`     | 15      | 15      | 10      | 10      | **10** |

=== "Caso 3"

    ```title="Entrada"
    3
    3
    C 1
    A 3 7
    C 2
    ```

    ```title="Salida"
    0
    7
    ```

    !!! example "Guía de ejecución"

        El tren tiene 3 vagones. El estado inicial es `[0, 0, 0]`.

        | Operación | Vagón 1 | Vagón 2 | Vagón 3 | Salida |
        | --------- | ------- | ------- | ------- | ------ |
        | Inicio    | 0       | 0       | 0       |        |
        | `C 1`     | 0       | 0       | 0       | **0**  |
        | `A 3 7`   | 7       | 7       | 7       |        |
        | `C 2`     | 7       | 7       | 7       | **7**  |

### Rúbrica

| Criterio                                                                       | Puntaje |
| ------------------------------------------------------------------------------ | ------- |
| Crea la lista e inicializa los N vagones en cero                               | 10      |
| Lee e identifica correctamente la operación (`A` o `C`) en cada línea         | 15      |
| `cargar`: usa un ciclo para agregar `v` a cada vagón del 1 al `p`             | 35      |
| `consultar`: retorna la carga del vagón `p`                                   | 25      |
| Imprime una línea por cada operación `C` con el valor correcto                | 15      |
| **Total**                                                                      | **100** |
