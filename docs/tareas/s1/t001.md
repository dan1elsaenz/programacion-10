---
icon: material/vote
---

# :material-vote: Tarea 1

## Enunciado

Se debe desarrollar un programa en Python que simule el sistema de conteo de votos
para una **elección estudiantil** con 5 candidatos.

El programa debe gestionar dos listas predefinidas: una con los **nombres** de los candidatos
y otra con sus **votos iniciales**. A partir de estas listas, el usuario podrá interactuar
con el sistema a través de un menú de opciones.

## Datos iniciales

El programa debe iniciar con los siguientes datos predefinidos:

| Candidato | Votos iniciales |
| --------- | --------------- |
| Valeria   | 45              |
| Andrés    | 38              |
| Camila    | 52              |
| Diego     | 29              |
| Fernanda  | 41              |

## Menú principal

Al iniciar, el programa debe mostrar el siguiente menú:

```
=== Sistema de Votación Estudiantil ===
1. Consultar votos de un candidato
2. Registrar votos a un candidato
3. Ver estadísticas generales
4. Ver candidato ganador
```

> El usuario elige una opción digitando su número.
> Si digita una opción inválida, el programa debe mostrar un mensaje de error.

## Descripción

### Opción 1 — Consultar votos de un candidato

- Solicitar el nombre del candidato a consultar.
- Si el candidato existe, mostrar su nombre, la cantidad de votos y una clasificación según el siguiente criterio:
  - 50 votos o más: `Candidato destacado`
  - Entre 35 y 49 votos: `Candidato competitivo`
  - Menos de 35 votos: `Candidato con pocos votos`
- Si el candidato no existe, mostrar un mensaje indicándolo.

### Opción 2 — Registrar votos a un candidato

- Solicitar el nombre del candidato.
- Si el candidato existe, solicitar la cantidad de votos a agregar.
  - Los votos ingresados deben sumarse a los votos actuales del candidato.
  - Mostrar un mensaje de confirmación con el nuevo total.
- Si el candidato no existe, mostrar un mensaje indicándolo.

!!! warning "Votos válidos"

    La cantidad de votos a registrar debe ser un número entero mayor a cero.
    Si se ingresa un valor inválido, mostrar un mensaje de error.

### Opción 3 — Ver estadísticas generales

Mostrar las siguientes estadísticas calculadas a partir de la lista de votos:

- Total de votos registrados
- Promedio de votos por candidato
- Candidato con más votos
- Candidato con menos votos

### Opción 4 — Ver candidato ganador

- Determinar quién es el candidato con mayor cantidad de votos.
- Mostrar su nombre y su cantidad de votos.
- _Opcional_ (+5 pts): Si hay empate en el primer lugar, mostrar ambos nombres.

## Requisitos técnicos

- Utilizar **dos listas paralelas**: una para nombres y otra para votos.
- Utilizar el operador `in` para verificar si un candidato existe.
- Utilizar `index()` para relacionar ambas listas.
- Utilizar `sum()`, `min()`, `max()` y `len()` para las estadísticas.
- Utilizar **f-strings** para todos los mensajes de salida.
- Normalizar la entrada del usuario con `.strip()` y `.title()`.

## Ejemplos de ejecución esperada

=== "Opción 1 — Candidato encontrado"

    ```
    === Sistema de Votación Estudiantil ===
    1. Consultar votos de un candidato
    2. Registrar votos a un candidato
    3. Ver estadísticas generales
    4. Ver candidato ganador

    Elija una opción: 1
    Digite el nombre del candidato: camila

    Candidato: Camila
    Votos: 52
    Clasificación: Candidato destacado
    ```

=== "Opción 2 — Registrar votos"

    ```
    === Sistema de Votación Estudiantil ===
    1. Consultar votos de un candidato
    2. Registrar votos a un candidato
    3. Ver estadísticas generales
    4. Ver candidato ganador

    Elija una opción: 2
    Digite el nombre del candidato: diego
    Digite la cantidad de votos a agregar: 10

    Votos registrados correctamente.
    Diego ahora tiene 39 votos.
    ```

=== "Opción 3 — Estadísticas"

    ```
    === Sistema de Votación Estudiantil ===
    1. Consultar votos de un candidato
    2. Registrar votos a un candidato
    3. Ver estadísticas generales
    4. Ver candidato ganador

    Elija una opción: 3

    --- Estadísticas generales ---
    Total de votos: 205
    Promedio por candidato: 41.0
    Candidato con más votos: Camila (52)
    Candidato con menos votos: Diego (29)
    ```

=== "Opción 4 — Candidato ganador"

    ```
    === Sistema de Votación Estudiantil ===
    1. Consultar votos de un candidato
    2. Registrar votos a un candidato
    3. Ver estadísticas generales
    4. Ver candidato ganador

    Elija una opción: 4

    El candidato ganador es: Camila con 52 votos.
    ```

=== "Opción inválida"

    ```
    === Sistema de Votación Estudiantil ===
    1. Consultar votos de un candidato
    2. Registrar votos a un candidato
    3. Ver estadísticas generales
    4. Ver candidato ganador

    Elija una opción: 7

    Opción inválida. Debe digitar un número del 1 al 4.
    ```

## Rúbrica de evaluación

| Criterio                                               | Puntos  |
| ------------------------------------------------------ | ------- |
| Listas declaradas correctamente con datos predefinidos | 10      |
| Menú funcional con manejo de opción inválida           | 15      |
| Opción 1: consulta y clasificación correcta            | 20      |
| Opción 2: registro y actualización de votos            | 20      |
| Opción 3: estadísticas calculadas correctamente        | 20      |
| Opción 4: candidato ganador identificado correctamente | 15      |
| **Total**                                              | **100** |
