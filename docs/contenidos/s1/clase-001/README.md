---
icon: material/console
---

# :material-console: Clase 1

## ¿Qué es programar?

Programar consiste en **dar instrucciones a una computadora para que realice una tarea o resuelva un problema**.
Estas instrucciones deben ser **claras, precisas y estar en un orden lógico**, pues la computadora ejecuta exactamente lo que se le indica.

Desde un punto de vista general, programar implica:

- Analizar un problema.
- Pensar una solución paso a paso.
- Expresar esa solución en un lenguaje que la computadora pueda entender.

!!! note "Idea clave"

    Programar no es solo escribir código, sino **pensar cómo resolver un problema de forma ordenada**.

## ¿Qué es un algoritmo?

Un **algoritmo** es una **secuencia finita de pasos ordenados** que permiten resolver un problema o realizar una tarea específica.

Un algoritmo:

- No depende de un lenguaje de programación.
- Puede escribirse en palabras, diagramas o pseudocódigo.
- Describe _qué hacer_ y _en qué orden_, sin necesidad de usar código.

**Ejemplo sencillo de algoritmo:**

1. Solicitar dos números.
2. Sumarlos.
3. Mostrar el resultado.

### Características de un algoritmo

Para que una secuencia de pasos sea considerada un algoritmo, debe cumplir con las siguientes características:

- **Claridad:**
  Cada paso debe ser comprensible y no ambiguo.
- **Finitud:**
  El algoritmo debe terminar después de un número limitado de pasos.
- **Orden:**
  Los pasos deben ejecutarse en una secuencia lógica.

!!! warning "Entendimiento de un algoritmo"

    Si un algoritmo no es claro o no tiene un final definido, no puede implementarse correctamente en un programa.

### Algoritmos en la vida cotidiana

Los algoritmos no son exclusivos de la informática.
Muchas actividades diarias siguen una estructura algorítmica.

**Ejemplos:**

- Seguir una receta de cocina.
- Armar un mueble usando un manual.
- Instrucciones para llegar a un lugar.

En todos los casos se siguen **pasos ordenados** para obtener un resultado esperado.

## Lenguajes de programación y paradigmas

Un **lenguaje de programación** es un conjunto de reglas y símbolos que permiten **escribir instrucciones para que una computadora las ejecute**.

Mediante un lenguaje de programación es posible:

- Expresar algoritmos de forma precisa.
- Comunicarle a la computadora qué tareas debe realizar.
- Resolver problemas de manera automática.

Cada lenguaje de programación tiene su propia sintaxis y forma de expresar las instrucciones, pero todos comparten el mismo objetivo: **convertir una idea en un programa ejecutable**.

### Ejemplos de lenguajes de programación

Existen muchos lenguajes de programación, cada uno diseñado para distintos propósitos.

Algunos ejemplos son:

- Python
- C
- C++
- Java
- JavaScript

!!! note "Importancia de entender las bases de programación"

    Aunque los lenguajes son diferentes, los conceptos fundamentales de la programación se mantienen y pueden trasladarse de uno a otro.

### Introducción a los paradigmas de programación

Un **paradigma de programación** es una **forma de pensar y estructurar la solución de un problema** utilizando un lenguaje de programación.

El paradigma define:

- Cómo se organiza el código.
- Cómo se expresan las soluciones.
- Cómo se modela el problema a resolver.

No existe un único paradigma correcto; cada uno tiene ventajas dependiendo del tipo de problema.

### Enfoque del curso: programación imperativa / procedimental

En este curso se trabajará principalmente con el paradigma **imperativo o procedimental**, el cual se caracteriza por:

- Ejecutar instrucciones paso a paso.
- Modificar el estado del programa mediante variables.
- Seguir un orden claro de ejecución.

Este enfoque es especialmente adecuado para introducir los conceptos básicos de la programación, debido a que se asemeja a la forma en que las personas describen procedimientos en la vida cotidiana.

## Ciclo de desarrollo de un programa

### Análisis del problema

La primera etapa al desarrollar un programa es el **análisis del problema**.
En esta fase se busca comprender con claridad **qué se debe resolver** antes de escribir cualquier código.

Durante el análisis se identifican:

- Las **entradas**: datos que el programa recibe.
- El **proceso**: operaciones o pasos que se deben realizar.
- Las **salidas**: resultados que el programa debe mostrar.

Un buen análisis evita errores y retrabajos en etapas posteriores.

### Diseño de la solución

Una vez entendido el problema, se procede al **diseño de la solución**.
En esta etapa se define **cómo se va a resolver el problema**.

El diseño puede incluir:

- Algoritmos escritos en lenguaje natural.
- Diagramas de flujo.
- Ejemplos de ejecución manual.
- Pseudocódigo.

El objetivo es tener una solución clara antes de comenzar a programar.

### Implementación del programa

La **implementación** consiste en traducir el diseño realizado a un **lenguaje de programación**, en este caso Python.

En esta etapa:

- Se escribe el código fuente.
- Se siguen las reglas de sintaxis del lenguaje.
- Se transforman los pasos del algoritmo en instrucciones ejecutables.

Es común cometer errores durante la implementación, lo cual es parte normal del proceso de aprendizaje.

### Pruebas y verificación de resultados

La etapa de **pruebas** tiene como objetivo verificar que el programa funciona correctamente.

Durante esta fase se:

- Ejecuta el programa con distintos valores de entrada.
- Comparan los resultados obtenidos con los resultados esperados.
- Identifican y corrigen errores.

!!! warning "Hay que definir resultados esperados..."

    Un programa que se ejecuta sin errores no siempre es correcto.
    Las pruebas permiten confirmar que la solución resuelve realmente el problema planteado.

### Visión general del ciclo de desarrollo

El ciclo de desarrollo no es estrictamente lineal.
Si durante la implementación o las pruebas se detecta un error, es necesario volver a etapas anteriores.

!!! note "Idea clave"

    Programar es un proceso iterativo: analizar, diseñar, implementar y probar tantas veces como sea necesario.

## Archivos de código fuente

Un programa en Python se escribe en un **archivo de texto** con extensión `.py`, conocido como **archivo de código fuente**.

Este archivo contiene:

- Instrucciones escritas en Python.
- Comentarios que explican el funcionamiento del programa.
- La lógica necesaria para resolver un problema.

El archivo de código fuente puede editarse con distintos editores de texto, como Visual Studio Code.

## Variables, constantes y estado en memoria

Una **variable** es un nombre que se utiliza para **referirse a un valor almacenado en la memoria** de la computadora durante la ejecución de un programa.

Las variables permiten:

- Guardar información.
- Modificar valores a lo largo del programa.
- Utilizar datos en distintas instrucciones.

En Python, una variable se crea al asignarle un valor por primera vez.

```python title="Declaración y asignación"
a = 10
```

### Constantes

Una **constante** es un valor que **no debería cambiar durante la ejecución del programa**.

Python no tiene constantes estrictas, pero se utiliza una **convención** para identificarlas:

- El nombre de la constante se escribe en **mayúsculas**.
- Esto indica que su valor no debe modificarse.

### Estado del programa durante la ejecución

El **estado del programa** corresponde al **conjunto de valores que tienen las variables en un momento determinado** mientras el programa se está ejecutando.

El estado:

- Cambia conforme se ejecutan las instrucciones.
- Depende del orden de ejecución del programa.
- Permite que el programa recuerde información entre una instrucción y otra.

Comprender el estado del programa es fundamental para entender el comportamiento del código.

## Tipos de datos básicos

Un **tipo de dato** indica **qué tipo de información puede almacenar una variable** y cómo puede utilizarse dentro de un programa.

El tipo de dato determina:

- Qué operaciones se pueden realizar con el valor.
- Cómo se almacena la información en memoria.
- Cómo se interpreta el valor durante la ejecución del programa.

### Tipos de datos fundamentales en Python

En el curso, se trabajará inicialmente con los siguientes tipos de datos básicos:

- **Enteros (`int`)**
  Representan números enteros, positivos o negativos, sin parte decimal.

```python
a = 5
b = -3
c = 0
```

- **Reales (`float`)**
  Representan números con parte decimal.

```python
a = 3.14
b = -0.5
c = 2.0
```

- **Cadenas de texto/_strings_ (`str`)**
  Representan texto y se escriben entre comillas.

```python
a = "Hola"
b = "Python"
c = "123"
```

- **Booleanos (`bool`)**
  Representan valores lógicos.

```python
a = True
b = False
```

### Identificación del tipo de dato

Python permite conocer el tipo de dato de un valor o una variable utilizando la función `type()`.

```python
a = 1
print(type(a)) # (1)!
```

1. `<class 'int'>`

### Errores comunes al mezclar tipos de datos

Un error frecuente al iniciar en programación es intentar **combinar tipos de datos incompatibles**.

Algunos ejemplos de situaciones problemáticas incluyen:

- Intentar sumar un número con una cadena de texto.
- Tratar un valor de texto como si fuera un número.
- Comparar valores sin considerar su tipo.

## Asignación de variables

La **asignación** es el proceso mediante el cual se le da un valor a una variable.  
En Python, la asignación se realiza utilizando el operador `=`.

Al asignar un valor:

- La variable pasa a referirse a ese valor en memoria.
- Si la variable ya existía, su valor anterior se reemplaza.
- El cambio afecta el estado del programa a partir de ese punto.

Es importante recordar que el símbolo `=` **no representa igualdad matemática**, sino asignación.

## Conversión de tipo de datos

La conversión de tipos permite:

- Transformar texto en números.
- Asegurar que las operaciones se realicen correctamente.
- Evitar errores de tipo durante la ejecución.

Algunas conversiones comunes incluyen:

- Texto a entero.
- Texto a número real.
- Número a texto para mostrar resultados.

> La conversión debe realizarse **solo cuando sea necesario** y de forma cuidadosa.

Al convertir tipos:

- El valor debe tener un formato válido.
- Una conversión incorrecta puede provocar errores.
- Es responsabilidad del programador asegurarse de que los datos sean adecuados.

!!! warning "Importancia de conocer el tipo de dato"

    Intentar convertir un texto que no representa un número a un tipo numérico provocará un error durante la ejecución del programa.

## Operadores y expresiones

### Operadores aritméticos

Los **operadores aritméticos** permiten realizar operaciones matemáticas básicas sobre valores numéricos.

| Operador | Nombre           | Ejemplo  | Resultado |
| -------: | ---------------- | -------- | --------- |
|      `+` | Suma             | `5 + 3`  | `8`       |
|      `-` | Resta            | `5 - 3`  | `2`       |
|      `*` | Multiplicación   | `5 * 3`  | `15`      |
|      `/` | División         | `5 / 2`  | `2.5`     |
|     `//` | División entera  | `5 // 2` | `2`       |
|      `%` | Módulo (residuo) | `5 % 2`  | `1`       |
|     `**` | Potenciación     | `2 ** 3` | `8`       |

### Operadores relacionales

Los **operadores relacionales** permiten **comparar dos valores** y producen como resultado un valor booleano (`True` o `False`).

| Operador | Descripción       | Ejemplo  | Resultado |
| -------: | ----------------- | -------- | --------- |
|     `==` | Igual a           | `5 == 5` | `True`    |
|     `!=` | Diferente de      | `5 != 3` | `True`    |
|      `>` | Mayor que         | `5 > 3`  | `True`    |
|      `<` | Menor que         | `5 < 3`  | `False`   |
|     `>=` | Mayor o igual que | `5 >= 5` | `True`    |
|     `<=` | Menor o igual que | `5 <= 3` | `False`   |

### Operadores lógicos

Los **operadores lógicos** permiten **combinar o negar condiciones** y trabajan con valores booleanos.

| Operador | Significado | Ejemplo               | Resultado |
| -------: | ----------- | --------------------- | --------- |
|    `and` | Y lógico    | `(5 > 3) and (2 < 4)` | `True`    |
|     `or` | O lógico    | `(5 < 3) or (2 < 4)`  | `True`    |
|    `not` | Negación    | `not (5 > 3)`         | `False`   |

### Precedencia y evaluación de expresiones

Cuando una expresión contiene varios operadores, Python sigue un **orden de precedencia** para evaluarla.

| Nivel | Tipo de operador | Operadores                       |
| ----: | ---------------- | -------------------------------- |
|     1 | Paréntesis       | `( )`                            |
|     2 | Potenciación     | `**`                             |
|     3 | Aritméticos      | `*`, `/`, `//`, `%`              |
|     4 | Aritméticos      | `+`, `-`                         |
|     5 | Relacionales     | `==`, `!=`, `<`, `>`, `<=`, `>=` |
|     6 | Lógicos          | `not`                            |
|     7 | Lógicos          | `and`                            |
|     8 | Lógicos          | `or`                             |

!!! tip "Recomendación de uso"

    El uso de **paréntesis** permite controlar el orden de evaluación y hace que las expresiones sean más claras y fáciles de entender.
