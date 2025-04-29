# Clase 9: Ejercicios de Estructuras de Datos (Tuplas, Diccionarios y Sets) <!-- omit from toc -->

<details> 
  <summary>Tabla de contenidos</summary>

- [1. Sistema de evaluación cruzada entre estudiantes](#1-sistema-de-evaluación-cruzada-entre-estudiantes)
- [2. Análisis de hábitos de lectura](#2-análisis-de-hábitos-de-lectura)
- [3. Base de datos de empleados por departamento](#3-base-de-datos-de-empleados-por-departamento)
- [4. Inventario de productos con múltiples almacenes](#4-inventario-de-productos-con-múltiples-almacenes)
- [5. Historial de navegación web](#5-historial-de-navegación-web)
- [6. Resumen de encuestas](#6-resumen-de-encuestas)
- [7. Agenda semanal de un salón de clases](#7-agenda-semanal-de-un-salón-de-clases)
- [8. Catálogo de cursos con prerequisitos](#8-catálogo-de-cursos-con-prerequisitos)
- [9. Análisis de perfiles de usuario en una red social](#9-análisis-de-perfiles-de-usuario-en-una-red-social)
- [10. Sistema de control de asistencia con sets y diccionarios](#10-sistema-de-control-de-asistencia-con-sets-y-diccionarios)

</details> 


En esta clase se plantean ejercicios de las estructuras de datos vistas anteriormente: sets, diccionarios y tuplas.

---

### 1. Sistema de evaluación cruzada entre estudiantes

Solicita a cada estudiante que califique a otros compañeros con una nota del 1 al 10. Guarda los resultados en un diccionario anidado. Luego:
- Calcula el promedio recibido por cada estudiante.
- Muestra quién fue el estudiante mejor evaluado.

**Ejemplo:**
```python
{
  "Ana": {"Luis": 9, "Carlos": 8},
  "Luis": {"Ana": 10, "Carlos": 9},
  "Carlos": {"Ana": 7, "Luis": 8}
}
```

---

### 2. Análisis de hábitos de lectura
Recoge información sobre libros leídos por un grupo de personas (como sets). Luego:
- Muestra qué libros han leído todos.
- Muestra qué libros son exclusivos de cada persona.
- Construye un set con todos los libros leídos sin repetir.

**Ejemplo:**
```python
{
  "Ana": {"1984", "El Principito", "Dune"},
  "Luis": {"Dune", "1984", "It"},
  "Carlos": {"1984", "Dune"}
}
```

---

### 3. Base de datos de empleados por departamento
Crea un diccionario donde la clave sea el nombre del departamento y el valor sea una lista de tuplas con información de cada empleado (nombre, edad, salario). Permite:
- Agregar un nuevo empleado.
- Calcular el promedio salarial por departamento.
- Encontrar al empleado con el salario más alto.

**Ejemplo:**
```python
{
  "TI": [("Ana", 30, 1200), ("Luis", 28, 1500)],
  "Ventas": [("Carlos", 35, 1000)]
}
```

---

### 4. Inventario de productos con múltiples almacenes
Gestiona un inventario que usa un diccionario anidado:
```python
inventario = {
  "producto1": {"almacen1": 20, "almacen2": 15},
  "producto2": {"almacen1": 5, "almacen2": 0}
}
```
Permite consultar:
- Stock total de un producto.
- Almacenes donde está agotado.
- Productos con stock cero en todos los almacenes.

---

### 5. Historial de navegación web

Guarda en una lista de tuplas las visitas a sitios web en formato `(usuario, sitio, fecha)`. Luego:
- Crea un diccionario con claves usuario y valores como sets de sitios visitados.
- Muestra los sitios comunes entre todos los usuarios.

**Ejemplo:**
```python
[
  ("Ana", "wikipedia.org", "2024-05-01"),
  ("Ana", "openai.com", "2024-05-02"),
  ("Luis", "openai.com", "2024-05-01"),
  ("Luis", "wikipedia.org", "2024-05-03")
]
```

---

### 6. Resumen de encuestas
Simula una encuesta donde cada persona puede elegir múltiples respuestas (almacenadas como sets). Luego analiza:
- La opción más popular.
- Qué combinación de opciones fue más frecuente.
- Cuántas respuestas únicas hubo en total.

**Ejemplo:**
```python
[
  {"Python", "Java"},
  {"Python", "C++"},
  {"Python", "Java"}
]
```

---

### 7. Agenda semanal de un salón de clases
Crea una estructura donde cada día de la semana es una clave y su valor es una lista de tuplas con eventos `(nombre_evento, hora)`. Permite:
- Buscar eventos por nombre en toda la semana.
- Ver el evento más temprano de un día específico.
- Detectar si hay conflictos horarios (mismo horario, mismo día).

**Ejemplo:**
```python
{
  "lunes": [("Matemáticas", 8), ("Química", 10)],
  "martes": [("Historia", 8)]
}
```

---

### 8. Catálogo de cursos con prerequisitos
Diseña un sistema donde cada curso (clave del diccionario) tiene como valor un set de cursos prerequisito. Luego:
- Detecta si hay prerequisitos cíclicos.
- Lista todos los cursos que no requieren ningún prerequisito.

**Ejemplo:**
```python
{
  "Cálculo II": {"Cálculo I"},
  "Física II": {"Física I"},
  "Cálculo I": set()
}
```

---

### 9. Análisis de perfiles de usuario en una red social
Cada usuario tiene una tupla con su edad, ciudad y una lista de intereses. Almacena todos los usuarios en un diccionario. Luego:
- Muestra los intereses más comunes.
- Filtra usuarios por ciudad e interés.
- Agrupa usuarios por rango de edad usando sets.

**Ejemplo:**
```python
{
  "Ana": (22, "San José", ["lectura", "música"]),
  "Luis": (28, "Cartago", ["lectura", "deportes"])
}
```

---

### 10. Sistema de control de asistencia con sets y diccionarios
Cada clase contiene un set de estudiantes presentes. Almacena la asistencia en un diccionario con la fecha como clave. Luego:
- Muestra el total de clases asistidas por cada estudiante.
- Identifica a quienes no asistieron nunca.
- Compara la asistencia entre dos fechas.

**Ejemplo:**
```python
{
  "2024-04-01": {"Ana", "Luis"},
  "2024-04-02": {"Ana"},
  "2024-04-03": {"Luis", "Carlos"}
}
```

