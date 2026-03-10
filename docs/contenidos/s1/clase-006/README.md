---
icon: material/pencil
---

# :material-pencil: Clase 6: Quiz 2

!!! abstract "Instrucciones generales"

    - El quiz consta de dos ejercicios de programación.
    - Cada ejercicio se entrega como un archivo `.py` independiente.
    - El código debe ejecutarse sin errores y producir los resultados esperados.

## Ejercicio 1: Suma de números pares positivos

El programa recibe números enteros ingresados por el usuario uno por uno y se guardan en una lista.
Solo se acumulan los que sean **positivos y pares**.
Al ingresar `0`, la captura termina y se muestran los resultados.

El programa debe cumplir con los siguientes requisitos:

1. Usar un ciclo `while` para recibir números hasta que el usuario ingrese `0`.
2. Ignorar los números negativos o impares sin registrarlos.
3. Al finalizar, mostrar:
    - Cuántos números pares positivos se ingresaron.
    - La suma de esos números.
    - El promedio de esos números. Si no se ingresó ninguno, mostrar un mensaje indicándolo.

!!! tip "Pista"

    - Para determinar si un número es par, se puede usar el operador `%`.  Si `numero % 2 == 0`, el número es par.
    - Recuerde que la lista debe estar _afuera_ del `while` para que guarde los elementos recibidos y se puedan acceder después.

### Ejemplos de ejecución

=== "Con datos válidos e inválidos"

    ```
    Digite un número (0 para terminar): 4
    Digite un número (0 para terminar): -3
    Digite un número (0 para terminar): 7
    Digite un número (0 para terminar): 10
    Digite un número (0 para terminar): 2
    Digite un número (0 para terminar): 0

    Cantidad de números pares positivos: 3
    Suma: 16
    Promedio: 5.33
    ```

=== "Sin números válidos"

    ```
    Digite un número (0 para terminar): -2
    Digite un número (0 para terminar): 3
    Digite un número (0 para terminar): -8
    Digite un número (0 para terminar): 0

    No se ingresó ningún número par positivo.
    ```

=== "Solo el cero"

    ```
    Digite un número (0 para terminar): 0

    No se ingresó ningún número par positivo.
    ```

### Rúbrica de evaluación

| Criterio                                                                   | Puntaje |
| -------------------------------------------------------------------------- | ------: |
| El ciclo `while` recibe números y termina correctamente al ingresar `0`    |      10 |
| Se ignoran los números negativos e impares (uso correcto del operador `%`) |      15 |
| Se acumula la suma y el conteo de números válidos correctamente            |      10 |
| Se muestran la cantidad, la suma y el promedio al finalizar                |      10 |
| Se muestra un mensaje apropiado cuando no se ingresó ningún número válido  |       5 |
| **Total**                                                                  |  **50** |

## Ejercicio 2: Analizador de texto

El programa solicita una oración al usuario y la analiza carácter por carácter para generar un reporte.

El programa debe cumplir con los siguientes requisitos:

1. Solicitar una oración al usuario.
2. Usar un ciclo `for` para recorrer cada carácter de la oración y contar:
    - Cantidad de **vocales**.
    - Cantidad de **espacios**.
3. Mostrar también:
    - La cantidad total de caracteres (con `len()`).
    - La cantidad de caracteres **sin contar espacios** (utilice la información que ya tiene para calcularlo).
    - La oración convertida a **mayúsculas** y a **minúsculas**.

!!! tip "Pista"

    - Utilice el siguiente bloque de código como condición: `caracter in "AaEeIiOoUu"` para verificar si el caracter sobre el que está iterando es una vocal (tanto en mayúscula como minúscula). Alternativamente, se puede convertir todo a mayúscula/minúscula.
    - Para el espacio, recuerde que puede comparar el caracter con `" "` para ver si es igual.
    - Defina contadores fuera del loop para las cantidades que le solicitan.

### Ejemplos de ejecución

=== "Caso 1"

    ```
    Digite una oración: Hola mundo

    --- Reporte ---
    Total de caracteres: 10
    Caracteres sin espacios: 9
    Vocales: 4
    Espacios: 1
    En mayúsculas: HOLA MUNDO
    En minúsculas: hola mundo
    ```

=== "Caso 2"

    ```
    Digite una oración: El colegIO CIENtífico de Puriscal

    --- Reporte ---
    Total de caracteres: 33
    Caracteres sin espacios: 29
    Vocales: 13
    Espacios: 4
    En mayúsculas: EL COLEGIO CIENTÍFICO DE PURISCAL
    En minúsculas: el colegio científico de puriscal
    ```

### Rúbrica de evaluación

| Criterio                                                             | Puntaje |
| -------------------------------------------------------------------- | ------: |
| Se usa un ciclo `for` para recorrer la oración carácter por carácter |      10 |
| Se cuentan las vocales correctamente (mayúsculas y minúsculas)       |      15 |
| Se cuentan los espacios correctamente                                |      10 |
| Se muestra el total de caracteres y la cantidad sin espacios         |      10 |
| Se muestra la oración en mayúsculas y en minúsculas                  |       5 |
| **Total**                                                            |  **50** |
