
## Práctica Evaluada 2

Se debe implementar un programa en Python que presente un **menú interactivo** con las siguientes opciones:

### 1. Verificar divisibilidad
- El usuario ingresa dos números enteros, `a` y `b`.
- El programa determina si `a` es divisible por `b` y muestra un mensaje indicando si la división es exacta o no.
- Si `b` es 0, lo cual provoca una división indefinida, se debe de verificar antes de realizar la división con un `if` para mostrar un mensaje de error.

### 2. Manipulación de string con slicing
- El usuario ingresa una cadena de texto.
- Se debe mostrar la cadena en orden inverso.
    - Sugerencia: Con `string[::-1]` hace slicing desde el inicio hasta el final, con un paso de -1 (orden inverso).

### 3. Extra: Cálculo de una raíz n-ésima
- El usuario ingresa dos números: `x` y `n`, donde `x` es el número del que se quiere calcular la raíz y `n` es el índice de la raíz.
- El programa calcula la **raíz n-ésima de `x`** usando la función `x ** (1/n)`.
- Se debe validar que `n` sea un número positivo y diferente de 0.
- Si `x` es negativo y `n` es par, se debe mostrar un mensaje de error, puesto que los números negativos no tienen raíces pares reales.

## Requisitos
- El programa debe implementarse usando un **menú con `if-elif-else`**.



