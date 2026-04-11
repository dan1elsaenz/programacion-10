---
icon: material/bus
---

# :material-bus: Tarea 2

## Enunciado

La empresa Autobuses Puriscal S.A. necesita un sistema digital para gestionar las reservas de asientos en su ruta San José — Puriscal.

Se debe desarrollar un programa en Python que simule el sistema de reservas de un autobús con **5 filas y 4 columnas** de asientos (20 asientos en total).
El programa debe representar el bus como una **matriz de 5x4**, donde cada celda indica si el asiento está disponible (`0`) u ocupado (`1`).

El sistema debe cumplir con los siguientes requisitos:

1. Definir una función `crear_bus(filas, columnas)` que retorne una matriz de ceros del tamaño indicado.
2. Definir una función `mostrar_bus(bus)` que imprima la matriz visualmente con encabezados de fila y columna, distinguiendo asientos libres (`[ ]`) de ocupados (`[X]`).
3. Definir una función `reservar_asiento(bus, fila, columna)` que marque el asiento como ocupado. Si ya estaba ocupado, debe retornar `False`; si la reserva es exitosa, debe realizarla y retornar `True`.
4. Definir una función `cancelar_reserva(bus, fila, columna)` que libere el asiento. Si ya estaba disponible, debe retornar `False`; si la cancelación es exitosa, debe realizarla y retornar `True`.
5. Definir una función `disponibles_por_fila(bus)` que muestre cuántos asientos libres hay en cada fila y el total general.
6. El programa principal debe inicializar el bus con los datos predefinidos, luego mostrar un menú en ciclo `while` con las cinco opciones descritas abajo.

## Datos iniciales

Al iniciar el programa, el bus ya tiene los siguientes asientos reservados:

| Fila | Columna |
| ---- | ------- |
| 1    | 2       |
| 2    | 1       |
| 2    | 4       |
| 3    | 3       |
| 4    | 2       |
| 5    | 1       |
| 5    | 3       |

## Menú principal

Al iniciar, el programa debe mostrar el siguiente menú en cada iteración del ciclo:

```
=== Servicio de Autobuses Puriscal ===
1. Ver estado del bus
2. Reservar un asiento
3. Cancelar una reserva
4. Ver disponibilidad por fila
5. Salir
```

> El usuario elige una opción digitando su número.
> Si digita una opción inválida, el programa debe mostrar un mensaje de error y volver al menú.

## Descripción

### Opción 1: Ver estado del bus

- Llamar a `mostrar_bus(bus)` para imprimir el estado actual de la matriz.
- Los asientos libres se muestran como `[ ]` y los ocupados como `[X]`.
- Debe incluir encabezados de fila (`Fila 1`, `Fila 2`, ...) y de columna (`Col 1`, `Col 2`, …).

### Opción 2: Reservar un asiento

- Solicitar la fila y la columna del asiento a reservar (valores entre 1 y 5 para fila, 1 y 4 para columna).
- Si la posición está fuera del rango válido, mostrar un mensaje de error.
- Llamar a `reservar_asiento`. Si retorna `True`, confirmar la reserva. Si retorna `False`, indicar que el asiento ya estaba ocupado.

!!! warning "Validación de entrada"

    Tanto la fila como la columna deben ser números enteros dentro del rango válido.
    Si el usuario ingresa letras u otro tipo de dato, el programa debe mostrar un mensaje de error sin cerrarse.

### Opción 3: Cancelar una reserva

- Solicitar la fila y la columna del asiento a cancelar (mismos rangos que la opción anterior).
- Si la posición está fuera del rango válido, mostrar un mensaje de error.
- Llamar a `cancelar_reserva`. Si retorna `True`, confirmar la cancelación. Si retorna `False`, indicar que el asiento ya estaba disponible.

### Opción 4: Ver disponibilidad por fila

- Llamar a `disponibles_por_fila(bus)`, que debe imprimir, por cada fila, cuántos asientos están libres.
- Al final, mostrar el total general de asientos disponibles en todo el bus.

### Opción 5: Salir

- Mostrar un mensaje de despedida y terminar el programa.

## Requisitos técnicos

- Representar el bus como una **matriz** (lista de listas) de enteros `0` y `1`.
- Implementar cada operación en su propia función con parámetros y valor de retorno definidos.
- Usar f-strings para todos los mensajes de salida.
- Validar entradas con `try/except` en las opciones 2 y 3.
- El menú debe ejecutarse en un ciclo `while continuar` y terminar únicamente con la opción 5.

## Ejemplos de ejecución esperada

=== "Opción 1 — Estado inicial"

    ```
    === Servicio de Autobuses Puriscal ===
    1. Ver estado del bus
    2. Reservar un asiento
    3. Cancelar una reserva
    4. Ver disponibilidad por fila
    5. Salir

    Elija una opción: 1

             Col 1   Col 2   Col 3   Col 4
    Fila 1 |  [ ]  |  [X]  |  [ ]  |  [ ]  |
    Fila 2 |  [X]  |  [ ]  |  [ ]  |  [X]  |
    Fila 3 |  [ ]  |  [ ]  |  [X]  |  [ ]  |
    Fila 4 |  [ ]  |  [X]  |  [ ]  |  [ ]  |
    Fila 5 |  [X]  |  [ ]  |  [X]  |  [ ]  |
    ```

=== "Opción 2 — Reserva exitosa"

    ```
    === Servicio de Autobuses Puriscal ===
    1. Ver estado del bus
    2. Reservar un asiento
    3. Cancelar una reserva
    4. Ver disponibilidad por fila
    5. Salir

    Elija una opción: 2
    Ingrese la fila (1-5): 3
    Ingrese la columna (1-4): 2

    Asiento (3, 2) reservado exitosamente.
    ```

=== "Opción 2 — Asiento ocupado"

    ```
    === Servicio de Autobuses Puriscal ===
    1. Ver estado del bus
    2. Reservar un asiento
    3. Cancelar una reserva
    4. Ver disponibilidad por fila
    5. Salir

    Elija una opción: 2
    Ingrese la fila (1-5): 1
    Ingrese la columna (1-4): 2

    Ese asiento ya está ocupado.
    ```

=== "Opción 3 — Cancelación exitosa"

    ```
    === Servicio de Autobuses Puriscal ===
    1. Ver estado del bus
    2. Reservar un asiento
    3. Cancelar una reserva
    4. Ver disponibilidad por fila
    5. Salir

    Elija una opción: 3
    Ingrese la fila (1-5): 2
    Ingrese la columna (1-4): 1

    Reserva del asiento (2, 1) cancelada.
    ```

=== "Opción 4 — Disponibilidad"

    ```
    === Servicio de Autobuses Puriscal ===
    1. Ver estado del bus
    2. Reservar un asiento
    3. Cancelar una reserva
    4. Ver disponibilidad por fila
    5. Salir

    Elija una opción: 4

    Fila 1: 3 asiento(s) disponible(s)
    Fila 2: 2 asiento(s) disponible(s)
    Fila 3: 3 asiento(s) disponible(s)
    Fila 4: 3 asiento(s) disponible(s)
    Fila 5: 2 asiento(s) disponible(s)

    Total disponibles: 13
    ```

=== "Opción inválida"

    ```
    === Servicio de Autobuses Puriscal ===
    1. Ver estado del bus
    2. Reservar un asiento
    3. Cancelar una reserva
    4. Ver disponibilidad por fila
    5. Salir

    Elija una opción: 9

    Opción inválida. Debe digitar un número del 1 al 5.
    ```

## Rúbrica de evaluación

| Criterio                                                  | Puntos  |
| --------------------------------------------------------- | ------- |
| Bus creado correctamente con datos iniciales predefinidos | 15      |
| `mostrar_bus`: visualización con encabezados y símbolos   | 15      |
| `reservar_asiento`: lógica y validación correctas         | 20      |
| `cancelar_reserva`: lógica y validación correctas         | 15      |
| `disponibles_por_fila`: conteo por fila y total general   | 15      |
| Menú en ciclo `while` con manejo de opción inválida       | 20      |
| **Total**                                                 | **100** |
