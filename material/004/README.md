# Clase 4: Ejercicios de repaso y `for` Loops <!-- omit from toc -->

<details> 
  <summary>Tabla de contenidos</summary>

- [1. Ejercicios de repaso](#1-ejercicios-de-repaso)
  - [Ejercicio 1: Conversor de notas a letras](#ejercicio-1-conversor-de-notas-a-letras)
  - [Ejercicio 2: Clasificación de palabras](#ejercicio-2-clasificación-de-palabras)
  - [Ejercicio 3: Encontrar el número mayor y menor en una lista](#ejercicio-3-encontrar-el-número-mayor-y-menor-en-una-lista)
  - [Ejercicio 4: Última palabra de una oración](#ejercicio-4-última-palabra-de-una-oración)
  - [Ejercicio 5: Comprobar si un número es múltiplo de otro](#ejercicio-5-comprobar-si-un-número-es-múltiplo-de-otro)
  - [Ejercicio 6: Comparar la longitud de dos palabras](#ejercicio-6-comparar-la-longitud-de-dos-palabras)
  - [Ejercicio 7: Verificar si una palabra empieza con vocal](#ejercicio-7-verificar-si-una-palabra-empieza-con-vocal)
  - [Ejercicio 8: OCI I Eliminatoria 2023](#ejercicio-8-oci-i-eliminatoria-2023)
- [2. Bucles `for` en Python](#2-bucles-for-en-python)
  - [2.1 Iteración sobre Listas y Strings](#21-iteración-sobre-listas-y-strings)
  - [2.2 Iteración con `range()`](#22-iteración-con-range)
  - [2.3 Uso de `break`, `continue`, `pass`](#23-uso-de-break-continue-pass)
  - [2.4 Bucles `for` Anidados](#24-bucles-for-anidados)
  - [2.5 `else` en un `for`](#25-else-en-un-for)
</details> 

## 1. Ejercicios de repaso

### Ejercicio 1: Conversor de notas a letras  

Escribe una función que reciba un número representando una calificación (de 0 a 100) y devuelva la letra correspondiente según la siguiente escala:  
- 90-100 → A  
- 80-89 → B  
- 70-79 → C  
- 60-69 → D  
- Menos de 60 → F  

**Ejemplo:**  
```plaintext
Entrada: 85  
Salida: 'B'
```

### Ejercicio 2: Clasificación de palabras  

Escribe una función que reciba una palabra y determine si cumple con alguna de las siguientes condiciones:
- Es un palíndromo (se lee igual al derecho y al revés).
- Tiene más de 5 caracteres.
- Comienza con una vocal.

La función debe devolver una lista con los mensajes correspondientes.

**Ejemplo:**
```plaintext
Entrada: "radar"  
Salida: ['La palabra es un palíndromo.']
```

### Ejercicio 3: Encontrar el número mayor y menor en una lista  

Escribe una función que reciba una lista de números enteros y devuelva el número más grande y el más pequeño.  

**Ejemplo:**  
```plaintext
Entrada: 3 1 7 9 2 8
Salida: (9, 1)
```

### Ejercicio 4: Última palabra de una oración  

Escribe una función que reciba una oración como string y devuelva la última palabra de la oración.  

**Ejemplo:**  
```plaintext
Entrada: "Hola, esto es un test"  
Salida: 'test'
```

### Ejercicio 5: Comprobar si un número es múltiplo de otro

Pide dos números y muestra si el primero es múltiplo del segundo.

```plaintext
Entrada: 12 4  
Salida: "12 es múltiplo de 4."
```

### Ejercicio 6: Comparar la longitud de dos palabras

Solicita dos palabras al usuario y muestra cuál es más larga o si tienen la misma cantidad de letras.

```plaintext
Entrada: "manzana pera"  
Salida: "La palabra 'manzana' es más larga que 'pera'."
```

### Ejercicio 7: Verificar si una palabra empieza con vocal

Pide al usuario una palabra y muestra un mensaje indicando si comienza con una vocal.

```plaintext
Entrada: "elefante"  
Salida: "La palabra comienza con una vocal."
```

### Ejercicio 8: OCI I Eliminatoria 2023

En una pequeña ciudad rodeada de vibrante vegetación y ríos cristalinos, Camila y Jonathan son apasionados por la historia y la cultura que se refleja en un símbolo nacional muy particular, el Yigüirro, el ave nacional. Ambos han dedicado años a coleccionar sellos con la imagen de este encantador pájaro.

Un buen día, un amigo historiador les solicita prestados algunos de sus sellos para una exposición. La cantidad varía cada vez, y se vuelve un tanto complicado para Camila y Jonathan llevar la cuenta de cuántos sellos les quedan luego de cada préstamo.
Necesitan tu ayuda para llevar un registro preciso. En cada ocasión, te informarán cuántos sellos tenían originalmente y cuántos su amigo les ha pedido prestados. Con esa información, deberás indicarles cuántos sellos les quedan. Recuerda, si el amigo les solicita más sellos de los que tienen, simplemente entregan todos sus sellos.

```
Entrada: "10 5"
Salida: 5
```

---

## 2. Bucles `for` en Python

Un bucle `for` permite ejecutar un bloque de código múltiples veces, iterando sobre elementos de una secuencia como una lista, un string o un rango de números.

### 2.1 Iteración sobre Listas y Strings

```python
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)

mensaje = "Python"
for letra in mensaje:
    print(letra)
```

En estos ejemplos, el bucle `for` recorre cada elemento de la lista `colores` y cada carácter del string `mensaje`.

### 2.2 Iteración con `range()`

El `range()` genera una secuencia de números, útil para iterar un número específico de veces.
El rango creado inicia en 0 de forma predeterminada.

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

El `range(inicio, fin, paso)` permite especificar un inicio y un incremento personalizado. El valor de `fin` no es incluido en el rango final, realmente se recorre de `inicio` a `fin - 1`.

```python
for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8
```

¿Por qué se usa `range()` en bucles?

- Es eficiente: No genera una lista en memoria, sino que produce los valores sobre la marcha.
- Es flexible: Permite definir rangos personalizados con diferentes pasos.
- Es fácil de usar con estructuras iterativas.

### 2.3 Uso de `break`, `continue`, `pass`

```python
for num in range(10):
    if num == 5:
        break  # Detiene el bucle
    if num % 2 == 0:
        continue  # Salta a la siguiente iteración
    print(num)
```

```python
for _ in range(3):
    pass  # No hace nada
```

### 2.4 Bucles `for` Anidados

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

**Complejidad:** Un `for` anidado puede aumentar la cantidad de ejecuciones, generalmente con una complejidad de O(n²).

### 2.5 `else` en un `for`

Si el bucle `for` no se interrumpe con `break`, el bloque `else` se ejecuta.

```python
for num in range(5):
    print(num)
else:
    print("Bucle terminado sin interrupción")
```

