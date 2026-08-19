---
icon: material/ferris-wheel
---

# :material-ferris-wheel: Tarea 1

## Enunciado

El Parque Aventura Puriscal necesita un sistema para administrar sus atracciones durante la temporada alta.
Cada atracción tiene una capacidad máxima de visitantes, un tiempo de ciclo distinto y una regla propia para decidir si un visitante puede subir según su estatura.
Además, el parque como tal necesita administrar el conjunto completo de atracciones: agregarlas, buscarlas por nombre, consultar cuáles tienen cupo disponible y calcular el tiempo de un recorrido con varias de ellas.

Se debe desarrollar un programa en Python que administre las atracciones del parque usando programación orientada a objetos.
La jerarquía de atracciones debe partir de una clase abstracta, y una clase adicional debe administrar esa jerarquía por composición.

**La clase abstracta `Atraccion` hereda de `ABC` y debe tener:**

| Atributo               | Descripción                                        |
| ---------------------- | -------------------------------------------------- |
| `nombre`               | Nombre de la atracción                             |
| `_capacidad`           | Atributo protegido; capacidad máxima de visitantes |
| `_visitantes_actuales` | Atributo protegido; inicia en `0`                  |

**Métodos abstractos de `Atraccion`:**

| Método                          | Descripción                                                               |
| ------------------------------- | ------------------------------------------------------------------------- |
| `calcular_tiempo_ciclo()`       | Retorna la duración en minutos de una vuelta completa                     |
| `verificar_restriccion(altura)` | Retorna `True` o `False` según si una persona de esa estatura puede subir |

**Métodos concretos de `Atraccion`** (heredados sin cambios por todas las subclases):

| Método                       | Descripción                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `subir_visitantes(cantidad)` | Suma visitantes sin superar `_capacidad`; retorna `True` si la operación fue posible, `False` si no había cupo suficiente |
| `vaciar()`                   | Reinicia `_visitantes_actuales` a `0`                                                                                     |
| `cupos_disponibles()`        | Retorna `_capacidad - _visitantes_actuales`                                                                               |

**Subclases de `Atraccion`**:

| Subclase       | Atributo propio                             | Tiempo de ciclo | Regla de `verificar_restriccion(altura)` |
| -------------- | ------------------------------------------- | --------------- | ---------------------------------------- |
| `MontañaRusa`  | `altura_minima`, recibido en el constructor | 3 min           | Exige `altura >= self.altura_minima`     |
| `RuedaFortuna` | `altura_minima`, recibido en el constructor | 10 min          | Exige `altura >= self.altura_minima`     |
| `Carrusel`     | No tiene                                    | 5 min           | Siempre retorna `True`                   |

!!! warning "`altura_minima` es un atributo, no un valor fijo dentro del método"

    `MontañaRusa` y `RuedaFortuna` deben recibir `altura_minima` como parámetro de su propio `__init__`.
    Después de llamar a `super().__init__(nombre, capacidad)`, deben guardarlo con `self.altura_minima = altura_minima`.
    `verificar_restriccion(altura)` debe comparar contra `self.altura_minima`, nunca contra un número escrito directamente dentro del método.

La clase `Parque` administra las atracciones por composición:

| Elemento                          | Descripción                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `nombre`                          | Nombre del parque                                                                                                                                      |
| `_atracciones`                    | Atributo protegido; lista de objetos `Atraccion`, inicia vacía                                                                                         |
| `agregar_atraccion(atraccion)`    | Agrega un objeto `Atraccion`, de cualquier subclase, a `_atracciones`                                                                                  |
| `listar_atracciones()`            | Retorna una copia de la lista de atracciones registradas                                                                                               |
| `buscar_atraccion(nombre)`        | Retorna el objeto `Atraccion` con ese nombre, o `None` si no existe                                                                                    |
| `atracciones_disponibles()`       | Retorna la lista de atracciones cuyo `cupos_disponibles()` sea mayor que `0`                                                                           |
| `tiempo_total_recorrido(nombres)` | Recibe una lista de nombres, suma el `calcular_tiempo_ciclo()` de las atracciones encontradas y retorna ese total junto con los nombres que no existen |

El programa principal debe crear un objeto `Parque`, agregar las atracciones predefinidas con `agregar_atraccion()`, y luego mostrar un menú en ciclo `while` con las siete opciones descritas abajo.

!!! danger "Ninguna opción del menú puede usar `isinstance()`"

    Todo el comportamiento que cambia según el tipo de atracción debe resolverse llamando al método correspondiente sobre el objeto, como `atraccion.calcular_tiempo_ciclo()` o `atraccion.verificar_restriccion(altura)`; nunca preguntando de qué clase es cada objeto.

## Datos iniciales

Al iniciar el programa, el parque ya cuenta con las siguientes atracciones:

| Nombre         | Tipo         | Capacidad | Altura mínima |
| -------------- | ------------ | --------- | ------------- |
| Trueno Salvaje | MontañaRusa  | 8         | 140 cm        |
| Vista Central  | RuedaFortuna | 12        | 100 cm        |
| Caballitos     | Carrusel     | 16        | —             |

## Menú principal

Al iniciar, el programa debe mostrar el siguiente menú en cada iteración del ciclo:

```
=== PARQUE AVENTURA PURISCAL ===
1. Ver todas las atracciones
2. Ver atracciones con cupo disponible
3. Subir visitantes a una atracción
4. Vaciar una atracción
5. Verificar restricción de altura
6. Calcular tiempo total de un recorrido
7. Salir
```

> El usuario elige una opción digitando su número.
> Si digita una opción inválida, el programa debe mostrar un mensaje de error y volver al menú.

## Descripción

### Opción 1: Ver todas las atracciones

- Llamar a `listar_atracciones()` sobre el `Parque` y recorrer el resultado, imprimiendo el nombre, la capacidad, la ocupación actual y el tiempo de ciclo de cada atracción con los métodos definidos en `Atraccion`.
- El tipo concreto de cada atracción puede obtenerse con `type(atraccion).__name__` solo para mostrarlo en pantalla, nunca para decidir qué calcular.

### Opción 2: Ver atracciones con cupo disponible

- Llamar a `atracciones_disponibles()` sobre el `Parque` y mostrar el nombre y los cupos restantes de cada una.
- Si ninguna atracción tiene cupo disponible, mostrar un mensaje indicándolo.

### Opción 3: Subir visitantes a una atracción

- Solicitar el nombre de la atracción y la cantidad de visitantes a subir.
- Buscar la atracción con `buscar_atraccion(nombre)`. Si no existe, mostrar un mensaje de error.
- Llamar a `subir_visitantes(cantidad)`. Si retorna `True`, confirmar la operación. Si retorna `False`, indicar que no hay cupo suficiente y mostrar `cupos_disponibles()`.

!!! warning "Validación de entrada"

    La cantidad de visitantes debe ser un número entero. Si el usuario ingresa letras u otro tipo de dato, el programa debe mostrar un mensaje de error sin cerrarse.

### Opción 4: Vaciar una atracción

- Solicitar el nombre de la atracción y buscarla con `buscar_atraccion(nombre)`.
- Si existe, llamar a `vaciar()` y confirmar. Si no existe, mostrar un mensaje de error.

### Opción 5: Verificar restricción de altura

- Solicitar el nombre de la atracción y la estatura del visitante, en centímetros.
- Buscar la atracción con `buscar_atraccion(nombre)`, llamar a `verificar_restriccion(altura)` sobre ella e imprimir si el visitante puede o no subir.

### Opción 6: Calcular tiempo total de un recorrido

- Solicitar al usuario una lista de nombres de atracciones separados por espacio, representando el orden en que las visitará.
- Llamar a `tiempo_total_recorrido(nombres)` sobre el `Parque` y mostrar el tiempo total. Si algún nombre no fue encontrado, mostrar una advertencia con los nombres omitidos.

### Opción 7: Salir

- Mostrar un mensaje de despedida y terminar el programa.

## Requisitos técnicos

- `Atraccion` debe heredar de `ABC`, importado del módulo `abc`, y declarar sus métodos abstractos con `@abstractmethod`.
- Las tres subclases deben inicializarse con `super().__init__(nombre, capacidad)`.
- `MontañaRusa` y `RuedaFortuna` deben guardar `altura_minima` como atributo propio, recibido en su constructor. No debe quedar como un número fijo dentro de `verificar_restriccion()`.
- `_capacidad` y `_visitantes_actuales` deben tratarse como atributos protegidos; ninguna opción del menú debe modificarlos directamente, solo a través de los métodos de `Atraccion`.
- `Parque` debe administrar sus atracciones por **composición**: mantiene una lista de objetos `Atraccion` como atributo, pero no hereda de `Atraccion` ni de `ABC`.
- El programa principal no debe mantener su propia lista de atracciones ni su propia función de búsqueda; toda operación sobre una atracción específica debe pasar por los métodos de `Parque`.
- Ninguna opción del menú puede usar `isinstance()`. El comportamiento distinto entre atracciones debe resolverse por polimorfismo.
- Validar toda entrada numérica con `try/except` en las opciones 3 y 5.
- El menú debe ejecutarse en un ciclo `while` y terminar únicamente con la opción 7.

## Ejemplos de ejecución esperada

=== "Opción 1 — Estado inicial"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 1

    Trueno Salvaje (MontañaRusa): 0/8 visitantes, ciclo de 3 min
    Vista Central (RuedaFortuna): 0/12 visitantes, ciclo de 10 min
    Caballitos (Carrusel): 0/16 visitantes, ciclo de 5 min
    ```

=== "Opción 2 — Cupo disponible"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 2

    Trueno Salvaje: 3 cupo(s) disponible(s)
    Vista Central: 12 cupo(s) disponible(s)
    Caballitos: 16 cupo(s) disponible(s)
    ```

=== "Opción 3 — Subida exitosa"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 3
    Nombre de la atracción: Trueno Salvaje
    Cantidad de visitantes: 5

    5 visitante(s) subieron a Trueno Salvaje.
    ```

=== "Opción 3 — Capacidad excedida"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 3
    Nombre de la atracción: Trueno Salvaje
    Cantidad de visitantes: 6

    No hay cupo suficiente. Cupos disponibles: 3
    ```

=== "Opción 4 — Vaciar exitoso"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 4
    Nombre de la atracción: Trueno Salvaje

    Trueno Salvaje fue vaciada. Cupos disponibles: 8
    ```

=== "Atracción inexistente"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 4
    Nombre de la atracción: Tren Fantasma

    No existe una atracción llamada 'Tren Fantasma'.
    ```

=== "Opción 5 — Restricción de altura"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 5
    Nombre de la atracción: Trueno Salvaje
    Estatura del visitante (cm): 135

    El visitante NO puede subir a Trueno Salvaje.
    ```

=== "Opción 6 — Recorrido completo"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 6
    Ingrese las atracciones a visitar, separadas por espacio: Vista Central Caballitos Trueno Salvaje

    Tiempo total del recorrido: 18 minutos
    ```

=== "Opción inválida"

    ```
    === PARQUE AVENTURA PURISCAL ===
    1. Ver todas las atracciones
    2. Ver atracciones con cupo disponible
    3. Subir visitantes a una atracción
    4. Vaciar una atracción
    5. Verificar restricción de altura
    6. Calcular tiempo total de un recorrido
    7. Salir

    Elija una opción: 9

    Opción inválida. Debe digitar un número del 1 al 7.
    ```

## Rúbrica de evaluación

| Criterio                                                                                                                                                           | Puntos  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| Clase abstracta `Atraccion`: atributos, métodos abstractos y métodos concretos correctos                                                                           | 15      |
| Subclases `MontañaRusa`, `RuedaFortuna` y `Carrusel` con herencia, `super().__init__()` y `altura_minima` como atributo correctos                                  | 15      |
| Clase `Parque`: composición correcta y métodos `agregar_atraccion`, `listar_atracciones`, `buscar_atraccion`, `atracciones_disponibles` y `tiempo_total_recorrido` | 20      |
| Opciones 1 y 6 resueltas por polimorfismo                                                                                                                          | 15      |
| Opción 3: validación de capacidad y de entrada con `try/except`                                                                                                    | 10      |
| Opciones 4 y 5: lógica y manejo de atracción inexistente                                                                                                           | 10      |
| Opción 6: suma correcta del tiempo de ciclo y manejo de nombres inválidos                                                                                          | 10      |
| Menú en ciclo `while` con manejo de opción inválida                                                                                                                | 5       |
| **Total**                                                                                                                                                          | **100** |
