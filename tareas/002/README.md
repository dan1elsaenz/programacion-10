# Tarea 2: Listas y Bucles `for` Anidados

## Descripción

Esta tarea consiste en **tres ejercicios independientes** que emplean **listas, bucles `for` y validaciones básicas de entrada**.  
Los ejercicios se enfocan en el uso de estructuras repetitivas, generación de salidas en distintos formatos y validación de strings numéricos.

Recuerde añadir **comentarios descriptivos**, así como utilizar **nombres de variables claros** en cada uno de sus programas.

## Ejercicio 1: Generar lista con los primeros `n` cuadrados

1. Solicite al usuario un string que cumpla con las siguientes condiciones:
   - Contiene únicamente dígitos.
   - Representa un número positivo (mayor que 0).
2. Si el valor ingresado es válido, convierta el string a un número entero `n`.
3. Cree una lista con los primeros `n` cuadrados (es decir, de $1^2$ a $n^2$).
4. Muestre la lista generada al usuario.

### Ejemplo de Ejecución

```
Ingrese un número: 5
[1, 4, 9, 16, 25]
```

Si el dato ingresado no es válido, debe mostrarse un mensaje de error adecuado.

## Ejercicio 2: Dibujar un triángulo con asteriscos

1. Solicite al usuario un string que cumpla las siguientes condiciones:
   - Contiene únicamente dígitos.
   - Representa un número positivo.
2. Si el valor es válido, convierta el string a un número entero `n`.
3. Dibuje un triángulo rectángulo de altura `n` usando asteriscos (`*`).
   - El triángulo debe crecer línea por línea desde 1 hasta `n` asteriscos.

### Ejemplo de Ejecución

```
Ingrese un número: 4
*
**
***
****
```

## Ejercicio 3: Tabla de multiplicar del 1 al 5

Cree un programa en Python que muestre las tablas de multiplicar del 1 al 5, desde el 1 hasta el 10 (ver ejemplo de salida).

1. Utilice bucles `for` anidados.
2. No debe recibir entradas del usuario.
3. Cada línea debe mostrar una multiplicación en el formato `a x b = resultado`.

### Ejemplo de Salida

```
1 x 1 = 1
1 x 2 = 2
...
3 x 5 = 15
...
5 x 10 = 50
```

---

## Entrega

- El código de cada ejercicio debe colocarse en **archivos separados**:  
  - `ejercicio1.py`, `ejercicio2.py` y `ejercicio3.py`.
- Suba los tres archivos `.py` al entorno de **Google Classroom** designado.

---

## Criterios de Evaluación (100 puntos)

### Ejercicio 1: Generar lista con cuadrados (30 puntos)
- **Validación de entrada**: 10 puntos  
- **Generación correcta de la lista**: 10 puntos  
- **Impresión clara del resultado**: 10 puntos  

### Ejercicio 2: Triángulo con asteriscos (30 puntos)
- **Validación de entrada**: 10 puntos  
- **Uso correcto de bucles `for`**: 10 puntos  
- **Formato correcto del triángulo**: 10 puntos  

### Ejercicio 3: Tabla de multiplicar (40 puntos)
- **Bucle anidado correcto para todas las combinaciones**: 15 puntos  
- **Formato adecuado de salida (`a x b = c`)**: 10 puntos  
- **Cobertura completa del 1 al 5 y 1 al 10**: 15 puntos


