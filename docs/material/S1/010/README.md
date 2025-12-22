# Clase 10: Funciones en Python

## ¿Por qué usar funciones?

Las funciones son bloques reutilizables de código que permiten estructurar mejor los programas, evitar repeticiones y dividir las tareas en partes más pequeñas.
Uno de los principales beneficios que brindan las funciones está vinculado con el principio **DRY** (_don't repeat yourself_), pues permite llamar bloques de código específico a partir del nombre de la función.

En esta clase se abordan desde los aspectos básicos hasta temas como recursión y tipos de argumentos.
Usar funciones correctamente permite mejorar la organización del código, facilitar su mantenimiento y comprensión.

---

## Declarar y definir una función

**Declarar** una función significa anunciar que existe, mientras que **definir** una función implica escribir qué acciones realizará.
En Python, se utiliza la palabra clave `def` seguida del nombre de la función, paréntesis y dos puntos:

```python
def saludar():
    print("¡Hola!")
```

En este ejemplo, `saludar` es el nombre de la función.
Todo el bloque de código indentado después de los dos puntos pertenece al cuerpo de la función.

Es importante evitar usar nombres de funciones que coincidan con palabras reservadas de Python o funciones integradas como `print`, `sum`, `input`, entre otros.

---

## Llamar a una función

Una vez definida una función, puede ser **llamada** desde cualquier parte del código usando su nombre seguido de paréntesis.
Si la función tiene parámetros, estos deben proporcionarse en la llamada.

```python
saludar()  # Salida: ¡Hola!
```

Llamar una función varias veces permite reutilizar el mismo bloque de instrucciones sin duplicar código.

---

## Parámetros y argumentos

- Un **parámetro** es una variable en la definición de una función, es como una _entrada esperada_.
- Un **argumento** es el valor que se pasa cuando se llama a la función.

```python
def saludar(nombre):  # 'nombre' es el parámetro
    print(f"Hola, {nombre}")

saludar("Ana")  # "Ana" es el argumento
```

!!! info "Número de argumentos posicionales"

    El número de argumentos debe coincidir con el número de parámetros en la definición, salvo que se utilicen mecanismos como `*args` o valores predeterminados.

Python permite definir múltiples parámetros separados por comas.
Todos los argumentos se asignan en orden.

---

## Variables locales y globales

- **Variables locales**: se crean dentro de una función y sólo existen mientras la función se ejecuta.
  No son accesibles desde fuera.
- **Variables globales**: se definen fuera de las funciones y pueden ser accedidas desde cualquier parte del programa.

```python
mensaje = "Hola global"

def mostrar():
    mensaje = "Hola local"
    print(mensaje)

mostrar()        # Hola local
print(mensaje)   # Hola global
```

Si se desea modificar una variable global dentro de una función, se debe usar la palabra clave `global`, lo cual debe hacerse con precaución:

```python
def cambiar():
    global mensaje
    mensaje = "Modificado"
```

!!! warning "Uso de `global`"

    Esta no es considerada una buena práctica de programación e indica un diseño pobre.

---

## `*args` – Número arbitrario de argumentos

`*args` permite que una función reciba cualquier cantidad de argumentos posicionales, que son accesibles como una tupla:

```python
def sumar_todos(*numeros): # Números representa una tupla
    print(sum(numeros))

sumar_todos(1, 2, 3, 4)  # Salida: 10
```

Se usa cuando no se conoce con antelación cuántos valores serán enviados.
No puede ir antes de argumentos normales, y sólo se puede usar una vez en la definición.

---

## Keyword arguments

Permiten especificar el nombre del parámetro al pasarle el argumento, sin importar el orden:

```python
def saludar(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")

# Se accede a las variables de los argumentos por su nombre, no por posición
saludar(edad=20, nombre="Luis")
```

Esto es especialmente útil para funciones con muchos argumentos, lo cual hace el código más legible.

---

## Parámetros predeterminados

Se pueden definir valores por defecto para los parámetros, de modo que si no se especifican al llamar la función, se use ese valor:

```python
def saludar(nombre="Usuario"):
    print(f"Hola, {nombre}") # Se imprime `Usuario` si no se indica ningún argumento en la llamada
```

El parámetro con valor por defecto debe colocarse **después** de los que no tienen.
Si se define uno sin valor después de uno con valor predeterminado, Python lanzará un error.

---

## Paso por valor y referencia

- **Inmutables** (`int`, `str`, `float`) se pasan por valor: no se modifica el valor original.
- **Mutables** (`list`, `dict`) se pasan por referencia: sí se puede modificar el objeto original desde la función.

```python
def modificar_lista(l):
    l.append(4)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(mi_lista)  # Salida: [1, 2, 3, 4]
```

Para evitar efectos secundarios con estructuras mutables, se trabaja con una copia:

```python
def modificar_sin_afectar(l):
    copia = l.copy()
    copia.append(99) # l no se ve afectada
```

---

## Palabra clave `pass`

`pass` se utiliza cuando se necesita una función vacía, por ejemplo, en una estructura que se completará más adelante.

```python
def pendiente():
    pass
```

Esto evita errores de sintaxis cuando aún no se define el cuerpo de la función.

---

## Palabra clave `return`

`return` detiene la ejecución de la función y puede:

- No retornar nada (equivale a `return None`)
  - Recordar que el tipo de dato `None` es un tipo de dato nulo.
- Retornar un único valor
- Retornar múltiples valores en forma de tupla

`return` permite comunicar distintas funciones o porciones de código entre sí.
Consiste en la **salida** de la función.

```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

x, y = operaciones(5, 2)
```

Una función puede tener múltiples `return`, dependiendo de las condiciones:

```python
def analizar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    return "cero"
```

!!! warning "Numerosos `return` statements"

    No se recomienda que las funciones tengan muchos `return` distintos.
