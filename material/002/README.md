
# Clase 2: Operadores, Booleanos y Estructura de Control `if-elif-else`

En esta clase se abordarán los operadores en Python, los valores booleanos que resultan de ellos y la estructura de control `if-elif-else`, con explicaciones detalladas y ejemplos prácticos.

## 1. Operadores en Python

Los operadores en Python permiten realizar diversas operaciones, desde cálculos matemáticos hasta comparaciones lógicas. Son fundamentales para la programación, ya que permiten manipular datos de manera efectiva.

### 1.1 Operadores Matemáticos

Los operadores matemáticos permiten realizar cálculos entre valores numéricos. Python maneja automáticamente los tipos de datos adecuados en las operaciones.

| Operador | Descripción        | Ejemplo (`a = 10, b = 3`) | Resultado |
|----------|--------------------|--------------------------|-----------|
| `+`      | Suma               | `a + b`                  | `13`      |
| `-`      | Resta              | `a - b`                  | `7`       |
| `*`      | Multiplicación      | `a * b`                  | `30`      |
| `/`      | División (decimal)  | `a / b`                  | `3.3333`  |
| `//`     | División entera     | `a // b`                 | `3`       |
| `%`      | Módulo (residuo)    | `a % b`                  | `1`       |
| `**`     | Potencia           | `a ** b`                 | `1000`    |

Python respeta la jerarquía de operaciones matemáticas, ejecutando primero las potencias, luego multiplicaciones y divisiones, y por último sumas y restas.

Ejemplo en Python:

```python
a = 10
b = 3

print(a + b)   # Suma: 13
print(a - b)   # Resta: 7
print(a * b)   # Multiplicación: 30
print(a / b)   # División: 3.3333
print(a // b)  # División entera: 3
print(a % b)   # Módulo: 1
print(a ** b)  # Potencia: 1000
```

---

### 1.2 Operadores de Asignación

Los operadores de asignación permiten modificar el valor de una variable de manera eficiente. En lugar de escribir expresiones completas como `x = x + 5`, se puede utilizar `x += 5` para reducir la complejidad del código.

| Operador | Descripción                       | Ejemplo (`a = 5`) | Equivalente a |
|----------|-----------------------------------|-------------------|---------------|
| `=`      | Asigna un valor                   | `a = 5`           | `a = 5`       |
| `+=`     | Suma y asigna                     | `a += 3`          | `a = a + 3`   |
| `-=`     | Resta y asigna                    | `a -= 2`          | `a = a - 2`   |
| `*=`     | Multiplica y asigna               | `a *= 4`          | `a = a * 4`   |
| `/=`     | Divide y asigna                   | `a /= 2`          | `a = a / 2`   |
| `//=`    | División entera y asigna          | `a //= 3`         | `a = a // 3`  |
| `%=`     | Módulo y asigna                   | `a %= 2`          | `a = a % 2`   |
| `**=`    | Exponente y asigna                | `a **= 3`         | `a = a ** 3`  |

Estos operadores permiten optimizar y hacer más legible el código, lo que facilita su mantenimiento.

---

## 3. Estructura de Control `if-elif-else`

### ¿Qué es una estructura condicional?

En programación, una estructura condicional permite tomar decisiones basadas en ciertas condiciones. En Python, se usa la estructura `if-elif-else` para evaluar diferentes escenarios y ejecutar bloques de código según se cumplan o no determinadas condiciones.

### Sintaxis básica de `if`

```python
if condicion:
    # Código que se ejecuta si la condición es verdadera
```

El bloque de código dentro del `if` se ejecuta solo si la condición es `True`. Si la condición es `False`, el bloque se ignora.

Ejemplo:

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
```

### Uso de `elif`

El `elif` permite evaluar múltiples condiciones sin necesidad de anidar varios `if`. Se ejecutará el primer `elif` cuya condición sea `True`, y el resto se ignorará.

```python
edad = 14
if edad >= 18:
    print("Eres adulto.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres un niño.")
```

### Uso de `else`

El `else` se usa como un caso final para cubrir cualquier escenario que no haya sido manejado en los `if` y `elif` anteriores.

```python
numero = -5
if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es negativo.")
```

### If anidado

Es posible anidar estructuras `if` dentro de otras para evaluar múltiples condiciones de manera jerárquica.

```python
x = 20
if x > 10:
    print("Mayor que 10")
    if x > 15:
        print("Mayor que 15")
```

### Operador ternario

Python permite simplificar condicionales mediante un operador ternario, que es una expresión compacta equivalente a `if-else`.

```python
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)
```

Este operador es útil cuando se necesita asignar valores en función de una condición de manera concisa.

