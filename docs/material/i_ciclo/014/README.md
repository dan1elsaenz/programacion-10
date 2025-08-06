# Clase 14: Manejo de archivos, múltiples archivos, módulos y manejo de errores <!-- omit from toc -->

## Manejo de Archivos en Python

Python permite trabajar con archivos de texto mediante funciones integradas que permiten abrir, leer, escribir y cerrar archivos. La función principal para esto es `open()`.

### Formas de abrir archivos

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

### Modos de apertura

| Modo | Significado                    |
| ---- | ------------------------------ |
| 'r'  | Lectura (por defecto)          |
| 'w'  | Escritura (sobrescribe)        |
| 'a'  | Agregar contenido al final     |
| 'x'  | Crear archivo, error si existe |
| 'b'  | Binario (ej: 'rb', 'wb')       |
| '+'  | Lectura y escritura            |

### Lectura de archivos

- `read()`: lee todo el contenido como un string.
- `readline()`: lee solo una línea del archivo.
- `readlines()`: devuelve una lista con todas las líneas.

#### Ejemplo:

```python
with open('datos.txt', 'r') as f:
    todo = f.read()
    f.seek(0)  # volver al inicio del archivo
    una_linea = f.readline()
    f.seek(0)
    lineas = f.readlines()
```

### Escritura de archivos

- `write(texto)`: escribe el texto (sobrescribe si está en modo 'w').
- `writelines(lista)`: escribe una lista de strings.

```python
with open('salida.txt', 'w') as archivo:
    archivo.write("Hola, mundo\n")
    archivo.writelines(["Línea 1\n", "Línea 2\n"])
```

### Crear o agregar archivos

- Modo `'x'`: crea un archivo y lanza error si ya existe.
- Modo `'a'`: abre el archivo y agrega contenido al final.
- Modo `'w'`: crea el archivo o sobrescribe si ya existe.

```python
# Crear
with open('nuevo.txt', 'x') as f:
    f.write("Archivo creado")

# Agregar
with open('log.txt', 'a') as f:
    f.write("Nueva entrada\n")
```

---

## Manejo de Paths en Python

### ¿Qué es un path?

En una computadora, un **path** (ruta) es una cadena de texto que indica la ubicación de un archivo o carpeta dentro del sistema de archivos.

Existen dos tipos principales de rutas:

- **Ruta absoluta**: comienza desde la raíz del sistema de archivos. Ejemplo en Linux/macOS:  
  `/home/usuario/documentos/archivo.txt`  
  o en Windows:  
  `C:\Usuarios\usuario\documentos\archivo.txt`

- **Ruta relativa**: se interpreta en relación con la carpeta actual desde donde se ejecuta el programa. Ejemplo:  
  `documentos/archivo.txt`

Python permite trabajar con ambas rutas. Para evitar errores de compatibilidad entre sistemas (por ejemplo, separadores `/` vs `\\`), es importante usar herramientas como `os.path` o `pathlib`, que abstraen estas diferencias.

### Usando `os.path`

El módulo `os.path` proporciona funciones para construir, transformar y analizar rutas de archivos en forma de cadenas (`str`). Es compatible con versiones anteriores de Python y funciona en todos los sistemas operativos.

```python
import os

ruta_relativa = "archivo.txt"
ruta_absoluta = os.path.abspath(ruta_relativa)  # Devuelve la ruta absoluta
existe = os.path.exists(ruta_relativa)          # Verifica si el archivo existe
carpeta = os.path.dirname(ruta_absoluta)        # Extrae el directorio
nombre_archivo = os.path.basename(ruta_absoluta) # Extrae el nombre del archivo

print("Ruta absoluta:", ruta_absoluta)
print("¿Existe el archivo?", existe)
print("Carpeta contenedora:", carpeta)
print("Nombre del archivo:", nombre_archivo)
```

#### Ventajas:

- Compatible con Python 2 y 3
- Funciones simples para tareas comunes

#### Limitaciones:

- Todas las operaciones son con cadenas (`str`)
- El código puede ser más difícil de leer y componer, especialmente al unir rutas

### Usando `pathlib` (moderno)

El módulo `pathlib` permite trabajar con rutas como objetos (`Path`) en lugar de simples cadenas. Esto hace que el código sea más legible, expresivo y compatible con múltiples plataformas.

```python
from pathlib import Path

ruta = Path("archivo.txt")

print("Ruta absoluta:", ruta.resolve())  # Devuelve un Path absoluto
print("¿Existe el archivo?", ruta.exists())
print("Carpeta padre:", ruta.parent)
print("Nombre del archivo:", ruta.name)
```

También se pueden leer y escribir archivos directamente desde objetos `Path`:

```python
# Escribir texto en un archivo
ruta.write_text("Hola desde pathlib")

# Leer el contenido del archivo
contenido = ruta.read_text()
print("Contenido:", contenido)
```

Para unir carpetas o navegar directorios se usa `/`, no `+` ni `os.path.join()`:

```python
nueva_ruta = Path("documentos") / "proyectos" / "informe.txt"
print(nueva_ruta)  # documentos/proyectos/informe.txt
```

#### Ventajas:

- Sintaxis moderna, clara y orientada a objetos
- Más expresivo al construir rutas
- Métodos integrados para lectura y escritura

#### Limitaciones:

- No está disponible en versiones anteriores a Python 3.4

### Comparación breve

| Tarea                      | `os.path`                      | `pathlib`                |
| -------------------------- | ------------------------------ | ------------------------ |
| Unir rutas                 | `os.path.join("a", "b")`       | `Path("a") / "b"`        |
| Obtener nombre del archivo | `os.path.basename(path)`       | `ruta.name`              |
| Obtener carpeta            | `os.path.dirname(path)`        | `ruta.parent`            |
| Verificar existencia       | `os.path.exists(path)`         | `ruta.exists()`          |
| Ruta absoluta              | `os.path.abspath(path)`        | `ruta.resolve()`         |
| Leer archivo               | `open(path).read()`            | `ruta.read_text()`       |
| Escribir archivo           | `open(path, 'w').write(texto)` | `ruta.write_text(texto)` |

---

## Manejo de Errores con try-except

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

---

## Uso de Múltiples Archivos

En programas grandes, es común dividir el código en varios archivos para mantener una estructura limpia.

### Ejemplo:

- `principal.py`: archivo principal
- `utilidades.py`: funciones auxiliares

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

---

## Módulos Externos

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

---

## Ejercicio

### Enunciado

Desarrollar un programa de gestión de notas de estudiantes. El sistema debe permitir:

1. Agregar estudiantes y sus notas (nombre y lista de notas).
2. Guardar la información en un archivo `notas.txt`.
3. Leer el archivo y calcular el promedio de cada estudiante.
4. Mostrar un resumen de estudiantes aprobados y reprobados.

Dividir el programa en dos archivos:

- `main.py`: para la interfaz principal
- `notas_utils.py`: para funciones auxiliares
