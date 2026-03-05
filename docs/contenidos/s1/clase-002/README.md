---
icon: material/keyboard
---

# :material-keyboard: Clase 2

## Entrada interactiva y salida estándar

En un programa, la **entrada de datos** corresponde a la información que la persona usuaria proporciona durante la ejecución, mientras que la **salida estándar** corresponde a los resultados que el programa muestra en pantalla.

### Entrada interactiva de datos

La entrada interactiva permite que el programa **solicite información al usuario mediante el teclado** mientras se está ejecutando.

En Python, esto se realiza utilizando la función `input()`.

```python hl_lines="1"
nombre = input("Digite su nombre: ")
print(nombre)
```

!!! tip "Hay que guardar la información"

    La función `input()` por sí sola recibe el dato, pero hay que almacenarlo en una variable para preservar su contenido.

En este ejemplo:

- El programa **detiene su ejecución** hasta que se ingresa un valor.
- El valor digitado se almacena en una variable.
- El estado del programa cambia al asignarse ese valor.

!!! note "Tipo de dato recibido..."

    La función `input()` **siempre retorna un valor de tipo `str`**, independientemente de lo que se digite.

    > Si se ingresa un número, hay que convertirlo explícitamente a entero con `int()`, por ejemplo.

### Entrada de datos y tipos de datos

Aunque la persona usuaria digite números, el valor recibido por `input()` es texto.
Por esta razón, para realizar operaciones matemáticas, es necesario **convertir el tipo de dato**.

```python
edad_texto = input("Digite su edad: ")
edad = int(edad_texto)
print(edad + 1)
```

!!! warning "Posible problema"

    Si el texto ingresado no representa un número válido, la conversión fallará y se **genera un error en tiempo de ejecución**.

### Salida estándar de datos

La **salida estándar** permite mostrar información en pantalla mediante la función `print()`.

```python
print("Hola mundo")
```

También es posible mostrar texto junto con variables:

```python
resultado = 15
print("El resultado es:", resultado)
```

La salida estándar se utiliza para:

- Mostrar resultados finales.
- Informar al usuario sobre el estado del programa (_logs_).
- Comunicar mensajes importantes al usuario.

## Verificación y validación de datos

Cuando un programa recibe datos desde la entrada interactiva, **no se puede asumir que esos datos son correctos**.
La persona usuaria puede cometer errores al digitar o ingresar valores que no tienen sentido dentro del problema.

Por esta razón, antes de utilizar un dato, es importante **verificarlo y validarlo**.

### Verificación de datos

La **verificación** consiste en comprobar que un dato:

- Tiene un **formato adecuado**.
- Puede ser tratado como el **tipo de dato esperado**.

Por ejemplo, si un programa necesita trabajar con números, primero se debe verificar que el valor ingresado **realmente pueda interpretarse como un número**.

### Validación de datos

La **validación** consiste en comprobar que un dato, además de tener un formato correcto, **cumple con las reglas del problema**.

Por ejemplo:

- Una edad debe ser un número, pero además debe representar una edad posible.
- Una nota debe ser un número, pero debe pertenecer a un rango razonable.

En esta etapa del curso, la validación se aborda **a nivel conceptual**.
Cuando se estudien los condicionales, va a quedar más claro.

## Manejo básico de errores y excepciones

Al programar, es normal cometer errores.
Python, al detectar un problema, muestra **mensajes de error** que indican qué ocurrió y por qué el programa no pudo continuar.

### Errores comunes en Python

Python identifica los errores mediante **tipos de excepción**, los cuales permiten reconocer la causa del problema.

La siguiente tabla muestra algunos de los errores más frecuentes:

| Error               | Descripción                                                  | Ejemplo                            |
| ------------------- | ------------------------------------------------------------ | ---------------------------------- |
| `ValueError`        | El valor es del tipo correcto, pero su contenido es inválido | Convertir `"abc"` a entero         |
| `TypeError`         | Se usan tipos incompatibles en una operación                 | Sumar un número con texto          |
| `ZeroDivisionError` | División entre cero                                          | `10 / 0`                           |
| `NameError`         | Uso de una variable que no existe                            | Imprimir una variable no definida  |
| `IndexError`        | Acceso a una posición inexistente (_listas_)                 | Acceder a un índice fuera de rango |
| `KeyError`          | Uso de una clave inexistente (_diccionarios_)                | Acceder a una clave no definida    |
| `SyntaxError`       | Error en la estructura del código                            | Falta de paréntesis o comillas     |

!!! note "Algunos errores se detectan antes de ejecutar..."

    Algunos errores, como `SyntaxError`, se detectan **antes de ejecutar el programa**.
    Otros aparecen **durante la ejecución**.

### Ejemplo de un error común

Si el texto ingresado no representa un número válido, Python genera un `ValueError`.

```python
texto = input("Digite un número: ")
numero = int(texto)
```

### Errores en tiempo de ejecución

Un **error en tiempo de ejecución** ocurre cuando:

- El programa comienza a ejecutarse correctamente.
- Se encuentra una instrucción que no puede completarse.
- Python detiene el programa y muestra un mensaje de error.

Muchos de los errores vistos anteriormente, como `ValueError` o `ZeroDivisionError`, ocurren durante la ejecución del programa.

### Excepciones

Una **excepción** es el mecanismo que utiliza Python para **indicar que ocurrió un error durante la ejecución**.

Cuando se produce una excepción:

- Se interrumpe el flujo normal del programa.
- Python informa el tipo de error ocurrido.
- El programa termina si la excepción no se maneja.

### Manejo de excepciones

Python permite **capturar excepciones** y definir una respuesta controlada cuando ocurre un error.

Esto se realiza utilizando las palabras clave (_keywords_) `try` y `except`.

```python hl_lines="1 4"
try: # (1)!
    numero = int(input("Digite un número: "))
    print(numero)
except ValueError: # (2)!
    print("Ocurrió un error al convertir el dato")
```

1. Intente ejecutar este bloque de código.
2. Si se genera un `ValueError`, se ejecuta este bloque.

En este ejemplo:

- El bloque `try` contiene instrucciones que pueden fallar.
- El bloque `except` se ejecuta si ocurre el error indicado.
- El programa no finaliza abruptamente.

## Calculadora básica

A continuación, se muestra un ejemplo de una calculadora básica en Python con los conceptos vistos hasta el momento.

```python
print("=== Calculadora básica ===")

try:
    a_texto = input("Digite el primer número: ")
    b_texto = input("Digite el segundo número: ")

    a = float(a_texto)
    b = float(b_texto)

    print("\nResultados:")
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", a / b)

except ValueError:
    print("\nError: se esperaba un número válido.")
except ZeroDivisionError:
    print("\nError: no se puede dividir entre cero.")

print("\nFin del programa.")
```

> `\n` equivale a un salto de línea; es decir, un ++enter++
