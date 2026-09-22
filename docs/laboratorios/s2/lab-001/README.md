---
icon: material/music
---

# :material-music: Laboratorio 1

## Enunciado

Una aplicación de streaming necesita un módulo para administrar la playlist de un usuario. El sistema debe registrar canciones y luego transformar, filtrar y resumir la playlist sin escribir un bucle distinto para cada operación.

1. Cada canción tiene un título, una duración en minutos y una cantidad de reproducciones.
2. La duración registrada de una canción nunca cambia; los ajustes de duración se calculan aparte, sin modificar la playlist original.
3. Se considera una canción "corta" si dura 3 minutos o menos.

**Menú principal:**

```
=== REPRODUCTOR DE MÚSICA ===
1. Registrar canción
2. Ver duración total de la playlist
3. Ver playlist en modo radio (máximo 3 minutos por canción)
4. Ver solo las canciones cortas
5. Ver si alguna canción supera las 1000 reproducciones
6. Ver la canción más reproducida
7. Salir
```

> Si el usuario ingresa una opción que no está en el menú, el programa debe mostrar un mensaje de error y volver a mostrar el menú.

### Opción 1 — Registrar canción

Solicita título, duración en minutos y cantidad de reproducciones, y agrega la canción a la playlist.

1. Duración y reproducciones deben convertirse con `try-except`, mostrando un mensaje de error si no son numéricas.
2. La duración debe ser mayor que 0; las reproducciones no pueden ser negativas.
3. Si ambos valores son válidos, agregue un diccionario con `titulo`, `duracion` y `reproducciones` a la playlist.

### Opción 2 — Ver duración total de la playlist

Calcula la duración total de la playlist **usando `reduce()`** de `functools`, sin usar `sum()`.

### Opción 3 — Ver playlist en modo radio

Genera, **con `map()` y una expresión lambda**, una versión de la playlist donde ninguna canción dura más de 3 minutos: si la duración original supera ese límite, se recorta a 3; si no, se mantiene igual. La playlist original no debe modificarse.

### Opción 4 — Ver solo las canciones cortas

Muestra, **con `filter()` y una expresión lambda**, únicamente las canciones cuya duración original es de 3 minutos o menos.

!!! warning "No use una comprensión de listas aquí"

    Esta opción existe para practicar `filter()` como función de orden superior.

### Opción 5 — Ver si alguna canción supera las 1000 reproducciones

Verifica, **con `any()` y una expresión generadora**, si al menos una canción de la playlist tiene más de 1000 reproducciones, sin construir ninguna lista intermedia.

### Opción 6 — Ver la canción más reproducida

Obtiene, **con `max()` y una expresión lambda en `key`**, la canción con más reproducciones de la playlist.

## Requisitos técnicos

- La opción 1 debe validar duración y reproducciones con `try-except`; ninguna canción inválida debe agregarse a la playlist.
- La opción 2 debe usar `functools.reduce()`; no se permite `sum()` ni un `for` con acumulador manual.
- La opción 3 debe usar `map()` con una lambda que retorne un diccionario nuevo por canción; la playlist original debe quedar intacta después de esta opción.
- La opción 4 debe usar `filter()` con una lambda; no se permite una comprensión de listas ni un `for` explícito.
- La opción 5 debe usar `any()` recibiendo una expresión generadora, no una lista ya construida.
- La opción 6 debe usar `max()` con el parámetro `key`, sin recorrer la playlist manualmente.
- El menú debe repetirse hasta que el usuario elija la opción 7.
- Si la playlist está vacía, las opciones 2 a 6 deben mostrar un mensaje indicándolo, en vez de operar sobre una lista vacía.

## Ejemplos de ejecución esperada

=== "Registro válido e inválido"

    ```
    === REPRODUCTOR DE MÚSICA ===
    1. Registrar canción
    ...
    Opción: 1
    Título: Horizonte
    Duración (minutos): 4.5
    Reproducciones: 820
    Canción 'Horizonte' registrada.

    Opción: 1
    Título: Eco
    Duración (minutos): -2
    La duración debe ser mayor que 0.

    Opción: 1
    Título: Marea
    Duración (minutos): 2.5
    Reproducciones: 1500
    Canción 'Marea' registrada.
    ```

=== "Duración total y modo radio"

    ```
    Opción: 2
    Duración total de la playlist: 7.00 minutos

    Opción: 3

    --- Playlist en modo radio ---
    Horizonte: 3.0 min
    Marea: 2.5 min
    ```

=== "Canciones cortas y más reproducida"

    ```
    Opción: 4

    --- Canciones cortas ---
    Marea: 2.5 min

    Opción: 6
    Canción más reproducida: Marea (1500 reproducciones)
    ```

=== "Reproducciones altas"

    ```
    Opción: 5
    ¿Alguna canción supera las 1000 reproducciones? True
    ```

=== "Playlist vacía"

    ```
    Opción: 2
    No hay canciones registradas.
    ```

=== "Duración no numérica"

    ```
    Opción: 1
    Título: Silencio
    Duración (minutos): larga
    La duración debe ser un número.
    ```

## Rúbrica de evaluación

| Criterio                                                                    | Puntaje |
| --------------------------------------------------------------------------- | ------: |
| La opción 1 valida correctamente duración y reproducciones con `try-except` |      10 |
| La opción 1 rechaza duraciones y reproducciones fuera de rango              |      10 |
| La opción 2 usa `functools.reduce()` correctamente                          |      15 |
| La opción 3 usa `map()` con lambda y no modifica la playlist original       |      15 |
| La opción 4 usa `filter()` con lambda, sin comprensión de listas            |      15 |
| La opción 5 usa `any()` con una expresión generadora                        |      15 |
| La opción 6 usa `max()` con `key` para encontrar la canción más reproducida |      10 |
| El menú se repite correctamente y valida opciones inválidas                 |       5 |
| Las opciones 2 a 6 manejan correctamente el caso de playlist vacía          |       5 |
| **Total**                                                                   | **100** |
