# Clase 14: Manejo de archivos, múltiples archivos, módulos y manejo de errores

## 1. Manejo de Archivos en Python

Python permite trabajar con archivos de texto mediante funciones integradas que permiten abrir, leer, escribir y cerrar archivos. La función principal para esto es `open()`.

### 1.1 Formas de abrir archivos

#### Usando `open()` directamente:

```python
archivo = open('archivo.txt', 'r')
contenido = archivo.read()
archivo.close()
```

Es necesario cerrar el archivo manualmente con `close()`.

#### Usando `with open()`:

```python
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
```

La ventaja es que el archivo se cierra automáticamente al finalizar el bloque `with`.

### 1.2 Modos de apertura

| Modo | Significado                    |
| ---- | ------------------------------ |
| 'r'  | Lectura (por defecto)          |
| 'w'  | Escritura (sobrescribe)        |
| 'a'  | Agregar contenido al final     |
| 'x'  | Crear archivo, error si existe |
| 'b'  | Binario (ej: 'rb', 'wb')       |
| '+'  | Lectura y escritura            |

### 1.3 Lectura de archivos

* `read()`: lee todo el contenido como un string.
* `readline()`: lee solo una línea del archivo.
* `readlines()`: devuelve una lista con todas las líneas.

#### Ejemplo:

```python
with open('datos.txt', 'r') as f:
    todo = f.read()
    f.seek(0)  # volver al inicio del archivo
    una_linea = f.readline()
    f.seek(0)
    lineas = f.readlines()
```

### 1.4 Escritura de archivos

* `write(texto)`: escribe el texto (sobrescribe si está en modo 'w').
* `writelines(lista)`: escribe una lista de strings.

```python
with open('salida.txt', 'w') as archivo:
    archivo.write("Hola, mundo\n")
    archivo.writelines(["Línea 1\n", "Línea 2\n"])
```

### 1.5 Crear o agregar archivos

* Modo `'x'`: crea un archivo y lanza error si ya existe.
* Modo `'a'`: abre el archivo y agrega contenido al final.
* Modo `'w'`: crea el archivo o sobrescribe si ya existe.

```python
# Crear
with open('nuevo.txt', 'x') as f:
    f.write("Archivo creado")

# Agregar
with open('log.txt', 'a') as f:
    f.write("Nueva entrada\n")
```

## 2. Manejo de Paths en Python

En sistemas reales, trabajar con rutas (paths) correctamente es clave, especialmente cuando se desarrolla en diferentes sistemas operativos.

### 2.1 Usando `os.path`

```python
import os

ruta_absoluta = os.path.abspath("archivo.txt")
existe = os.path.exists("archivo.txt")
carpeta = os.path.dirname(ruta_absoluta)
nombre_archivo = os.path.basename(ruta_absoluta)
```

### 2.2 Usando `pathlib` (moderno y recomendado)

```python
from pathlib import Path

ruta = Path("archivo.txt")
print(ruta.resolve())           # ruta absoluta
print(ruta.exists())            # True o False
print(ruta.parent)              # carpeta padre
print(ruta.name)                # nombre del archivo

# Leer archivo
contenido = ruta.read_text()

# Escribir archivo
ruta.write_text("Hola desde pathlib")
```

## 3. Manejo de Errores con try-except

El bloque `try-except` permite manejar errores sin que el programa se detenga abruptamente.

```python
try:
    archivo = open('archivo_inexistente.txt')
except FileNotFoundError:
    print("El archivo no fue encontrado.")
```

### Tabla de errores comunes

| Error                    | Cuándo ocurre                               |
| ------------------------ | ------------------------------------------- |
| `FileNotFoundError`      | Archivo no existe                           |
| `PermissionError`        | Permiso denegado para acceder al archivo    |
| `IsADirectoryError`      | Se intentó abrir un directorio como archivo |
| `IOError` o `OSError`    | Error de E/S general                        |
| `ValueError`             | Operación inválida en archivos abiertos     |
| `TypeError`              | Tipo de dato incorrecto usado               |
| `ZeroDivisionError`      | División entre cero                         |
| `KeyError`, `IndexError` | Acceso a clave o índice inexistente         |

## 4. Uso de Múltiples Archivos

En programas grandes, es común dividir el código en varios archivos para mantener una estructura limpia.

### Ejemplo:

* `principal.py`: archivo principal
* `utilidades.py`: funciones auxiliares

**utilidades.py**

```python
def saludar(nombre):
    return f"Hola, {nombre}"
```

**principal.py**

```python
import utilidades

nombre = input("Ingresa tu nombre: ")
print(utilidades.saludar(nombre))
```

## 5. Módulos Externos

Python incluye muchos módulos externos en su biblioteca estándar. Se importan con la palabra `import`.

### Ejemplo con `math`

```python
import math

print(math.sqrt(25))      # Raíz cuadrada
print(math.pi)            # Valor de pi
print(math.sin(math.pi))  # Seno de pi
```

Para instalar módulos externos que no están en la biblioteca estándar:

```bash
pip install nombre_modulo
```

## 6. Ejercicio

### Enunciado

Desarrollar un programa de gestión de notas de estudiantes. El sistema debe permitir:

1. Agregar estudiantes y sus notas (nombre y lista de notas).
2. Guardar la información en un archivo `notas.txt`.
3. Leer el archivo y calcular el promedio de cada estudiante.
4. Mostrar un resumen de estudiantes aprobados y reprobados.

Dividir el programa en dos archivos:

* `main.py`: para la interfaz principal
* `notas_utils.py`: para funciones auxiliares

