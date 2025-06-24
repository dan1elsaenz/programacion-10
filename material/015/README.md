# Clase 15: Repaso para el examen

## Ejercicio 1

Crear un programa que lea un archivo de texto llamado `numeros.txt` que contiene un número por línea.
El programa debe:

- Leer los números.
- Imprimir la suma total y el promedio.
- Detectar y manejar errores:
  - Si el archivo no existe, mostrar un mensaje.
  - Si hay contenido no numérico, ignorar esas líneas y continuar.
- Incluir una función recursiva que calcule la suma de los números.

**Opcional:** Si el archivo está vacío o no existe, generarlo con 10 números aleatorios entre 1 y 100.

---

## Ejercicio 2

Crear una función recursiva que determine si una palabra es un palíndromo.
Luego, escribir un programa que:

- Lea palabras desde un archivo llamado `palabras.txt`, una por línea.
- Imprima únicamente las palabras que son palíndromos.
- Use `try-except` para mostrar un mensaje si el archivo no existe.

---

## Ejercicio 3

Desarrollar un pequeño sistema de tareas.
El programa debe guardar y leer la información desde un archivo `tareas.txt`, donde cada línea tiene el formato:

```
nombre;prioridad
```

El programa debe permitir al usuario:

1. Ver todas las tareas.
2. Agregar una nueva tarea (solicitar nombre y prioridad).
3. Eliminar una tarea por nombre.
4. Calcular la cantidad de tareas con prioridad **alta** utilizando una función recursiva.

**Requisitos:**

- Menú interactivo con un loop (`while`).
- Cada opción debe estar implementada como una función separada.
- Manejo de errores con `try-except` para apertura y lectura del archivo.
- Validar que las prioridades sean correctas (`alta`, `media`, `baja`).


