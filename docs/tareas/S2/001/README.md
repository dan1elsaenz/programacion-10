# Tarea 1: Sistema de gestión de cursos, estudiantes y profesores

Desarrolle un programa en Python que simule un **sistema de gestión de cursos, estudiantes y profesores**, aplicando los principios de **programación orientada a objetos** vistos en clase:

- **Clases y objetos**
- **Encapsulamiento de datos (`#!python @property`, getters/setters)**
- **Herencia**

El sistema debe permitir registrar estudiantes y profesores, crear cursos, asignar profesores a cursos, matricular estudiantes y generar reportes básicos.

La asignación va a ser realizada en grupos de 3 personas.
Sólo una persona debe entregar los archivos y debe indicar por medio de un comentario en Classroom los 3 integrantes del equipo.
Asimismo, en cada uno de los archivos, en la parte superior deben incluir un comentario con `""" """` para indicar los 3 integrantes del equipo.

---

## Requisitos de diseño

### Clase `Persona`

| Elemento      | Detalle                             |
| ------------- | ----------------------------------- |
| **Atributos** | `nombre` (`str`)<br>`edad` (`int`)  |
| **Métodos**   | `presentar()`: retorna `"{nombre}"` |

### Clase `Estudiante` (hereda de `Persona`)

| Elemento         | Detalle                                                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Atributos**    | `_carrera` (`str`, encapsulado con `@property`)                                                                                                                          |
| **Métodos**      | `presentar()`: sobrescribe el del padre para incluir la carrera. Retorna `{nombre} ({_carrera})`<br>`matricular(curso)`: agrega el curso a su lista de cursos inscritos. |
| **Validaciones** | `_carrera` no puede ser cadena vacía.                                                                                                                                    |

### Clase `Profesor` (hereda de `Persona`)

| Elemento         | Detalle                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| **Atributos**    | `_especialidad` (`str`, encapsulado con `@property`)                                                       |
| **Métodos**      | `presentar()`: sobrescribe el del padre para incluir la especialidad. Retorna `{nombre} ({_especialidad})` |
| **Validaciones** | `_especialidad` no puede ser cadena vacía.                                                                 |

### Clase `Curso`

| Elemento      | Detalle                                                                                                                                                                                                                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Atributos** | `nombre` (`str`)<br>`codigo` (`str`)<br>`profesor` (inicialmente `None` y ser asignado, instancia de `Profesor`)<br>`estudiantes` (lista compuesta por instancias de la clase `Estudiante`)                                                                                         |
| **Métodos**   | `asignar_profesor(profesor)`: asigna el profesor al curso.<br>`agregar_estudiante(estudiante)`: agrega el estudiante a la lista.<br>`listar_estudiantes()`: muestra todos los estudiantes matriculados.<br>`info()`: retorna el nombre del curso, el código y el profesor asignado. |

### Composición

| Relación   | Detalle                                           |
| ---------- | ------------------------------------------------- |
| Curso      | **tiene** un profesor y una lista de estudiantes. |
| Estudiante | **puede estar** en varios cursos.                 |

### Menú interactivo

Debe permitir seleccionar las siguientes opciones:

| Opción | Acción                                                       |
| :----: | ------------------------------------------------------------ |
|   1    | Registrar estudiante                                         |
|   2    | Registrar profesor                                           |
|   3    | Crear curso                                                  |
|   4    | Asignar profesor a curso                                     |
|   5    | Matricular estudiante en curso                               |
|   6    | Ver estudiantes en un curso                                  |
|   7    | Ver cursos de un estudiante                                  |
|   8    | Ver información de un curso (incluye profesor y estudiantes) |
|   9    | Salir                                                        |

---

## Archivos requeridos

### `#!python main.py`

- Presenta el menú principal.
- Gestiona las opciones y la interacción con el usuario.

### `#!python modelos.py`

Debe contener las clases implementadas:

```python
class Persona:
    pass

class Estudiante(Persona):
    pass

class Profesor(Persona):
    pass

class Curso:
    pass
```

---

## Ejemplo de uso esperado

```
--- Menú ---
1. Registrar estudiante
2. Registrar profesor
3. Crear curso
4. Asignar profesor a curso
5. Matricular estudiante en curso
6. Ver estudiantes en un curso
7. Ver cursos de un estudiante
8. Ver información de un curso
9. Salir

Opción: 1
Nombre: Ana
Edad: 20
Carrera: Ingeniería

Opción: 2
Nombre: Luis
Edad: 45
Especialidad: Matemáticas

Opción: 3
Nombre del curso: Programación
Código: PY001

Opción: 4
Curso: Programación
Profesor: Luis

Opción: 5
Estudiante: Ana
Curso: Programación

Opción: 8
Curso Programación (PY001)
Profesor: Luis (Matemáticas)
Estudiantes: Ana (Ingeniería)
```

---

## Recomendaciones y pistas

### Identificadores y registros

- Usar **diccionarios** para guardar los datos:

      - `estudiantes: dict[str, Estudiante]` (clave: nombre).
      - `profesores: dict[str, Profesor]` (clave: nombre).
      - `cursos: dict[str, Curso]` (clave: **`codigo`** del curso).

- Crear funciones **de ayuda** para obtener instancias:

      - `obtener_estudiante(nombre)`, `obtener_profesor(nombre)`, `obtener_curso(codigo)`.
      - Al crear un estudiante, profesor o curso, se debería agregar a un diccionario de `estudiantes`, `profesores`, `cursos`, donde se pueden buscar TODOS los estudiantes, profesores y cursos basándose en los nombres o códigos dependiendo del caso.
      - Cada una de ellas debe retornar `estudiantes[nombre]`, `profesores[nombre]`, `cursos[codigo]`, que consiste en una instancia de la clase correspondiente.

### Encapsulamiento y validaciones

- En `Estudiante`:

      - `_carrera` con `@property` + `@setter` (no vacía).

- En `Profesor`:

      - `_especialidad` con `@property` + `@setter` (no vacía).

- Validar también:

      - `nombre` no vacío para `Estudiante` y `Profesor`, `edad >= 0`, `codigo` no vacío en `Curso`.

- En `Curso`:

      - Mantener la lista interna de estudiantes como **privada** (`_estudiantes`) y exponer solo métodos:
          - `agregar_estudiante(estudiante)`: evita duplicados.
          - `listar_estudiantes()`: **retorna** datos (el menú se encarga de imprimir).

      - `profesor` puede iniciar en `None`. Método `asignar_profesor()` valida instancia.

### Patrón para el menú

- Bucle principal `while continuar:`

      - Mostrar opciones
      - Leer opción validada (`int` de 1..9)
      - Llamar funciones en cada caso (`registrar_estudiante()`)

---

## Criterios de evaluación

| Criterio                                                                   | Puntos  |
| -------------------------------------------------------------------------- | ------- |
| Implementación correcta de clases y objetos                                | 10      |
| Uso de herencia (`Persona` → `Estudiante`, `Profesor`)                     | 15      |
| Uso de encapsulamiento con `@property` y validaciones                      | 15      |
| Implementación de composición (`Curso` contiene profesor y estudiantes)    | 15      |
| Menú interactivo con todas las funcionalidades                             | 20      |
| Código modular en múltiples archivos (`main.py`, `modelos.py`)             | 10      |
| Buenas prácticas (nombres claros, comentarios, docstrings)                 | 5       |
| Ejecución sin errores y manejo básico de entradas inválidas (`try-except`) | 5       |
| Documentación clara                                                        | 5       |
| **Total**                                                                  | **100** |
