# Clase 4: Bucle `while` en Python

El bucle `while` en Python permite ejecutar un bloque de código **mientras se cumpla una condición**. Es una de las estructuras de control de flujo más utilizadas cuando no se sabe de antemano cuántas veces se necesita repetir un conjunto de instrucciones.

---

## 1. Sintaxis básica del `while`

La **condición** se evalúa antes de cada iteración. Si es `True`, se ejecuta el bloque. Cuando la condición sea `False`, se detiene el bucle.

```python
while condición:
    # bloque de código a ejecutar mientras la condición sea True
```

### 1.1. Ejemplo con contador

Este bucle imprime los números del 1 al 5. Se utiliza un **contador** que se incrementa en cada vuelta para evitar un bucle infinito.

```python
contador = 1
while contador <= 5:
    print("Iteración número:", contador)
    contador += 1  # incremento del contador
```

### 1.2. Ejemplo con condición booleana

Aquí el bucle se mantiene activo mientras el usuario escriba `s`. La condición depende de una variable booleana que se actualiza dentro del bucle.

```python
continuar = True
while continuar:
    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() != "s":
        continuar = False
```

## 2. Palabras clave útiles en bucles

### 2.1 `break`

Detiene el bucle inmediatamente, sin esperar a que la condición sea falsa.

```python
while True:
    entrada = input("Escriba 'salir' para terminar: ")
    if entrada == "salir":
        break
    print("Ingresó:", entrada)
```

### 2.2. `continue`

Salta al siguiente ciclo del bucle, sin ejecutar el resto del bloque actual.

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)  # No imprimirá el número 3
```

### 2.3. `pass`

No hace nada. Se utiliza cuando la sintaxis requiere una instrucción pero no se desea ejecutar ninguna acción (placeholder).

```python
while True:
    pass  # Bucle infinito sin instrucciones (ejemplo teórico)
```

## 3. Casos de uso del `while`

### 3.1. Contador con condición

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### 3.2. Validación de entrada

```python
usuario = ""
while usuario != "admin":
    usuario = input("Ingrese el nombre de usuario correcto: ")
print("Bienvenido, admin.")
```

### 3.3. Esperar una condición externa

```python
import random

numero = 0
while numero != 5:
    numero = random.randint(1, 10)
    print("Número generado:", numero)
```

### 3.4. Repetir hasta que se introduzca un número válido

```python
entrada = input("Ingrese un número positivo: ")
while not entrada.isdigit() or int(entrada) <= 0:
    entrada = input("Error. Ingrese un número positivo: ")
print("Número aceptado:", entrada)
```

### 3.5. Calcular la suma de números hasta que el usuario escriba "fin"

```python
suma = 0
entrada = input("Ingrese un número o 'fin' para terminar: ")
while entrada != "fin":
    if entrada.isdigit():
        suma += int(entrada)
    else:
        print("Dato inválido, intente nuevamente.")
    entrada = input("Ingrese un número o 'fin' para terminar: ")
print("La suma total es:", suma)
```

### 3.6. Contraseña con intento limitado

```python
intentos = 0
clave = "python123"
while intentos < 3:
    entrada = input("Ingrese la contraseña: ")
    if entrada == clave:
        print("Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta.")
        intentos += 1
else:
    print("Demasiados intentos fallidos.")
```

## 4. Importancia del control del bucle

Es fundamental asegurarse de que **la condición del `while` pueda llegar a ser falsa**, de lo contrario el programa entrará en un **bucle infinito**. Normalmente esto se controla mediante:
- Incremento o modificación de variables internas.
- Validación de condiciones externas (como input).

## 5. `else` con `while`

El bucle `while` puede incluir un bloque `else`, que se ejecuta cuando la condición ya no se cumple **y el bucle no fue interrumpido con `break`**.

```python
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("El bucle terminó normalmente.")
```

# 6. Ejercicios del Bucle `while`

A continuación se presentan ejercicios para profundizar en el uso del bucle `while`.

### Ejercicio 1: Contador con condiciones

Escribe un programa que imprima los números del 1 al 20, pero:

- Si el número es múltiplo de 3, imprime "Fizz".
- Si es múltiplo de 5, imprime "Buzz".
- Si es múltiplo de ambos, imprime "FizzBuzz".
Usa un bucle `while`.

### Ejercicio 2: Validación de número primo

Solicita al usuario un número mayor que 1. Luego determina si es primo utilizando un bucle `while` que verifique sus divisores.

### Ejercicio 3: Suma acumulativa con control de errores

Pide al usuario que ingrese números uno por uno. Suma los valores válidos (enteros positivos) hasta que el usuario escriba "fin". Si ingresa algo incorrecto (como letras o números negativos), ignóralos y continúa.

### Ejercicio 4: Sistema de login con bloqueo

Simula un sistema de login donde el usuario tiene hasta 3 intentos para ingresar un usuario y contraseña válidos. Si falla, muestra un mensaje de bloqueo. El usuario válido es `admin` y la contraseña `1234`.

### Ejercicio 5: Adivinar número con intentos contados

Genera un número aleatorio entre 1 y 50. El usuario tiene hasta 5 intentos para adivinarlo. Después de cada intento, informa si el número secreto es mayor o menor que el ingresado. Si no lo acierta, indica el número correcto al final.

### Ejercicio 6: Frecuencia de letra en una palabra

Solicita al usuario una palabra y una letra. Recorre la palabra con un bucle `while` y cuenta cuántas veces aparece la letra (sin usar `.count()`).

### Ejercicio 7: Confirmación de cierre con múltiples respuestas

Solicita al usuario si desea salir del programa. Acepta "sí", "no", "s", "n", en mayúsculas o minúsculas. Solo finaliza cuando la respuesta sea afirmativa.

### Ejercicio 8: Suma de dígitos (sin strings)

Solicita un número entero positivo y calcula la suma de sus dígitos uno a uno usando solo operaciones aritméticas. Ejemplo: 342 → 3 + 4 + 2 = 9.

### Ejercicio 9: Tabla personalizada de multiplicar

Solicita al usuario un número entre 1 y 9, y el límite de la tabla (por ejemplo, hasta 15). Imprime su tabla de multiplicar con `while` hasta el número indicado.

### Ejercicio 10: Menú interactivo con opciones

Crea un menú con las siguientes opciones:
1. Ingresar nombre
2. Mostrar saludo personalizado
3. Salir

Debe funcionar con un `while` hasta que el usuario elija salir. Si selecciona la opción 2 sin haber ingresado un nombre, muestra un mensaje de advertencia.

