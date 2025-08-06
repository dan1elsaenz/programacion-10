# Práctica Evaluada 3

## Ejercicio 1: Convertir palabras a mayúsculas si tienen más de 5 letras

- Use un `for` loop para recorrer la lista de palabras.
- Dentro del loop, revise la longitud de cada palabra con `len()`.
- Si la longitud es mayor a 5, use `.upper()` para convertir la palabra en mayúsculas.
- Guarde los resultados en una nueva lista. Esta debe ser declarada antes del `for`, no dentro, para poder modificarla (por el alcance o _scope_ explicado en clase).
- Use `print()` para mostrar la lista resultante.

```plaintext
Entrada: ["hola", "elefante", "mundo", "estrella"]  
Salida: ["hola", "ELEFANTE", "mundo", "ESTRELLA"]
```

## Ejercicio 2: Reemplazar vocales en una palabra

- Use un `for` loop para recorrer cada letra de la palabra.
- Verifique si la letra es una vocal `(a, e, i, o, u)`.
- Si es una vocal, reemplazar por `*`, si no, deje la letra igual.
- Construya la nueva palabra con las letras modificadas. Defina una variable `palabra_nueva` antes del loop y vaya concatenando los nuevos caracteres conforme avanza en el loop.
- Use `print()` para mostrar el resultado.

```plaintext
Entrada: "programacion"  
Salida: "pr*gr*m*c**n"
```



