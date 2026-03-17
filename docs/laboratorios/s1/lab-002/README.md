---
icon: material/terrain
---

# :material-terrain: Laboratorio 2

## Ejercicio 1: Validador de secuencia montaña

Una **secuencia montaña** es una lista de números enteros que cumple exactamente tres condiciones:

1. Tiene al menos 3 números.
2. Existe un _pico_: un número que es mayor a todos los anteriores y a todos los posteriores.
3. Desde el inicio hasta el pico, los números son **estrictamente crecientes** (sin repetidos ni descensos).
4. Desde el pico hasta el final, los números son **estrictamente decrecientes** (sin repetidos ni ascensos).

El programa debe cumplir con los siguientes requisitos:

1. Usar un ciclo `while continuar` (`continuar` es una variable booleana) para capturar números enteros uno por uno. Ingresar `0` termina la captura.
2. Si el usuario ingresa algo que no sea un número entero, mostrar un error y usar `continue` para volver a pedir sin registrar nada.
3. Si se ingresaron menos de 3 números, mostrar un mensaje indicando que la secuencia no puede ser montaña.
4. Usar un ciclo `for` con `break` para encontrar el pico: recorrer la secuencia mientras los valores suban. Cuando dejen de subir, detener con `break`.
5. Usar otro ciclo `for` con `break` para verificar la fase descendente desde el pico: si en algún punto los valores no bajan estrictamente, romper con `break`.
6. Al final, indicar si **es** o **no es** una secuencia montaña, y en caso afirmativo, indicar cuál es el valor del pico.

!!! warning "El 0 es centinela, no elemento"

    El `0` solo indica el fin de la captura. No debe incluirse en la secuencia.

### Ejemplos de ejecución

=== "Sí es montaña"

    ```
    Número (0 para terminar): 1
    Número (0 para terminar): 3
    Número (0 para terminar): 7
    Número (0 para terminar): 5
    Número (0 para terminar): 2
    Número (0 para terminar): 0

    Secuencia: [1, 3, 7, 5, 2]
    Es una secuencia montaña. Pico: 7
    ```

=== "Solo sube"

    ```
    Número (0 para terminar): 1
    Número (0 para terminar): 3
    Número (0 para terminar): 7
    Número (0 para terminar): 0

    Secuencia: [1, 3, 7]
    No es montaña: no hay fase descendente.
    ```

=== "Sube de nuevo tras bajar"

    ```
    Número (0 para terminar): 1
    Número (0 para terminar): 5
    Número (0 para terminar): 3
    Número (0 para terminar): 6
    Número (0 para terminar): 2
    Número (0 para terminar): 0

    Secuencia: [1, 5, 3, 6, 2]
    No es montaña: la fase descendente no es estrictamente decreciente.
    ```

=== "Con _plateau_"

    ```
    Número (0 para terminar): 1
    Número (0 para terminar): 3
    Número (0 para terminar): 3
    Número (0 para terminar): 2
    Número (0 para terminar): 0

    Secuencia: [1, 3, 3, 2]
    No es montaña: no hay fase ascendente válida.
    ```

=== "Con entrada inválida"

    ```
    Número (0 para terminar): 4
    Número (0 para terminar): hola
    Error: debe ingresar un número entero.
    Número (0 para terminar): 9
    Número (0 para terminar): 6
    Número (0 para terminar): 0

    Secuencia: [4, 9, 6]
    Es una secuencia montaña. Pico: 9
    ```

=== "Menos de 3 números"

    ```
    Número (0 para terminar): 5
    Número (0 para terminar): 0

    Secuencia: [5]
    No es montaña: se necesitan al menos 3 números.
    ```

### Requisitos técnicos

- Usar `while continuar` con `break` para la captura de datos.
- Usar `continue` para manejar entradas inválidas sin interrumpir el ciclo.
- Usar `for` con `break` para la fase ascendente.
- Usar `for` con `break` para la fase descendente.
- No usar funciones propias de Python como `sorted()` o comparaciones directas sobre toda la lista de una vez.

### Rúbrica de evaluación

| Criterio                                                                     | Puntaje |
| ---------------------------------------------------------------------------- | ------: |
| Se usa `while continuar` + `break` para capturar la secuencia correctamente  |       8 |
| Se usa `continue` para ignorar entradas no numéricas sin detener el ciclo    |       7 |
| Se detecta y reporta correctamente si hay menos de 3 elementos               |       5 |
| Se usa `for` + `break` para encontrar el pico (fase ascendente)              |      10 |
| Se verifica correctamente que el pico no es el primero ni el último elemento |       5 |
| Se usa `for` + `break` para validar la fase descendente                      |      10 |
| Se reporta correctamente si es montaña, indicando el valor del pico          |       5 |
| Se reporta el motivo correcto cuando no es montaña                           |       5 |
| El `0` no se incluye en la secuencia                                         |       5 |
| **Total**                                                                    |  **60** |

## Ejercicio 2: Análisis del algoritmo de Kadane

El **algoritmo de Kadane** resuelve el siguiente problema: dada una lista de números enteros (que puede incluir negativos), encontrar la mayor suma posible de un subgrupo de elementos consecutivos.

Por ejemplo, en la lista `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, el subgrupo `[4, -1, 2, 1]` produce la mayor suma posible: `6`.

A continuación se presenta una versión simplificada del algoritmo. **No debe modificarlo.** Su tarea es analizarlo y responder las preguntas planteadas.

```python title="kadane.py"
n = int(input("¿Cuántos números? "))

numeros = []
for _ in range(n):
    numeros.append(int(input("Número: ")))

actual = numeros[0]
mejor  = numeros[0]

for i in range(1, len(numeros)):
    if actual < 0:
        actual = numeros[i]
    else:
        actual += numeros[i]

    if actual > mejor:
        mejor = actual

print(f"Mayor suma contigua: {mejor}")
```

### Preguntas de análisis

Responda las siguientes preguntas en un archivo `analisis.txt`. El número de cada pregunta debe preceder su respuesta.
Puede ayudarse con búsquedas en Internet.

**Pregunta 1: Variables iniciales**

¿Qué representan `actual` y `mejor` al inicio del programa, antes de que comience el ciclo `for`? ¿Por qué se inicializan con `numeros[0]` y no con `0`?

!!! tip "Pista"

    Piense qué ocurriría si todos los números de la lista fueran negativos y `mejor` comenzara en `0`.

**Pregunta 2: La decisión clave**

La línea más importante del algoritmo es:

```python
if actual < 0:
    actual = numeros[i]
```

Explique con sus propias palabras qué decisión toma el algoritmo en ese punto y por qué tiene sentido **descartar** la suma acumulada cuando es negativa.

!!! tip "Pista"

    Si `actual = -3` y el siguiente número es `5`, ¿cuánto da `-3 + 5`? ¿Y cuánto da empezar directamente desde `5`? ¿Cuál es mayor?

**Pregunta 3: Caso extremo**

¿Qué resultado produce el algoritmo con la lista `[-5, -2, -8, -1, -4]`? Justifique por qué ese es el resultado correcto y no `0`.

**Pregunta 4: Identificación del ciclo**

¿Qué tipo de ciclo se usa para recorrer la lista y por qué tiene sentido usarlo aquí en lugar de un `while`?

### Rúbrica de evaluación

| Criterio                                                                                                | Puntaje |
| ------------------------------------------------------------------------------------------------------- | ------: |
| **Pregunta 1:** explica correctamente `actual` y `mejor` y justifica la inicialización con `numeros[0]` |      10 |
| **Pregunta 2:** explica correctamente la lógica de descartar la suma negativa                           |      10 |
| **Pregunta 3:** identifica el resultado correcto y justifica por qué no es `0`                          |      10 |
| **Pregunta 4:** justifica el uso de `for` correctamente                                                 |      10 |
| **Total**                                                                                               |  **40** |
