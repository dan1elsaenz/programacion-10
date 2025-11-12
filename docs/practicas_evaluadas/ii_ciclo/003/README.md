# Práctica evaluada 3: Git y GitHub

!!! info "Objetivo general"

    Poner en práctica los comandos esenciales de Git y GitHub a través de un proyecto en Python.
    Cada estudiante clonará un repositorio, personalizará sus datos, ejecutará el programa, y subirá los resultados al repositorio remoto.

---

## Clonar el repositorio

1. En la página del repositorio en GitHub, copiar la URL `HTTPS`.
2. Abrir una terminal y clonar el repositorio con:
   ```bash
   git clone https://github.com/usuario/nombre-repo.git
   cd nombre-repo
   ```
3. Verificar el contenido del proyecto:
   ```bash
   ls
   ```

## Estructura del proyecto

Cree una carpeta `practicas_evaluadas/pe03/` dentro del repositorio con:

```bash
mkdir -p practicas_evaluadas/pe03
```

Dentro de esta carpeta, realice la siguiente estructura:

```
.
├── practicas_evaluadas/
│   └── pe03/
│       ├── README.md
│       ├── data/
│       │   └── estudiante.txt
│       ├── salida/
│       │   └── resumen.txt  (se genera al ejecutar el programa)
│       └── src/
│           ├── app.py
│           └── modelo.py
├── README.md
└── .gitignore
```

!!! note "Anotaciones"

    - `data/estudiante.txt` contiene los datos que cada estudiante debe personalizar.
    - `src/app.py` es el punto de entrada principal.
    - `src/modelo.py` define la clase `Estudiante` y la lectura/escritura de archivos.
    - `salida/resumen.txt` se genera automáticamente.

## Contenido de los archivos

A continuación, copie y pegue el siguiente código en los archivos correspondientes dentro de la carpeta `practicas_evaluadas/pe03/`.

### `README.md`

Como documentación general de lo realizado.

```markdown
# Descripción

Proyecto de práctica evaluada que utiliza programación orientada a objetos y manejo de archivos en Python.
El objetivo es generar un resumen con la información del estudiante y guardarlo en un archivo de texto.

## Instrucciones

1. Completar los datos en `data/estudiante.txt`.
2. Ejecutar `python3 src/app.py` para generar el resumen.
3. Verificar la creación de `salida/resumen.txt`.
4. Hacer commit y push de los cambios a GitHub.
```

### `.gitignore`

Este archivo sirve para indicarle a Git los archivos y/o directorios que debe ignorar.
A continuación, se muestran algunos típicos en el desarrollo de Python.

```
__pycache__/
*.pyc
.venv/
venv/
.env
```

### `src/modelo.py`

```py
"""
@file modelo.py
@brief Clases de dominio para la práctica (POO + archivos).
"""

from pathlib import Path
from typing import Dict, List


class Estudiante:
    """
    @brief Modelo de estudiante con datos básicos.
    """

    def __init__(self, nombre: str, correo: str, materias: List[str] | None = None) -> None:
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.materias = [m.strip() for m in (materias or []) if m.strip()]

    def resumen(self) -> str:
        lineas = [
            f"Nombre: {self.nombre}",
            f"Correo: {self.correo}",
            f"Materias: {', '.join(self.materias) if self.materias else 'N/A'}",
        ]
        return "\n".join(lineas)


class GestorArchivos:
    """
    @brief Utilidades para leer/escribir archivos de texto plano.
    """

    @staticmethod
    def leer_kv(ruta: Path) -> Dict[str, str]:
        """
        @brief Lee pares clave=valor, ignora líneas vacías y comentarios (#).
        @param ruta: Ruta del archivo de datos.
        @return Diccionario con claves en mayúscula.
        """
        datos: Dict[str, str] = {}
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                if "=" not in linea:
                    continue
                clave, valor = linea.split("=", 1)
                datos[clave.strip().upper()] = valor.strip()
        return datos

    @staticmethod
    def escribir_texto(ruta: Path, contenido: str) -> None:
        """
        @brief Escribe texto en la ruta indicada, crea carpetas si no existen.
        """
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
```

### `src/app.py`

```py
"""
@file app.py
@brief Programa principal de la práctica PE03.
"""

from pathlib import Path
from modelo import Estudiante, GestorArchivos

RUTA_BASE = Path(__file__).resolve().parents[1]
RUTA_DATOS = RUTA_BASE / "data" / "estudiante.txt"
RUTA_SALIDA = RUTA_BASE / "salida" / "resumen.txt"


def construir_estudiante() -> Estudiante:
    if not RUTA_DATOS.exists():
        raise FileNotFoundError(f"No se encontró el archivo de datos: {RUTA_DATOS}")

    kv = GestorArchivos.leer_kv(RUTA_DATOS)
    nombre = kv.get("NOMBRE", "N/A")
    correo = kv.get("CORREO", "N/A")

    materias = []
    if "MATERIAS" in kv and kv["MATERIAS"]:
        materias = [m.strip() for m in kv["MATERIAS"].split(",")]

    return Estudiante(nombre, correo, materias)


def main() -> None:
    estudiante = construir_estudiante()
    texto = estudiante.resumen()
    print(texto)
    GestorArchivos.escribir_texto(RUTA_SALIDA, texto)
    print(f"\nResumen generado correctamente en: {RUTA_SALIDA}")


if __name__ == "__main__":
    main()
```

### `data/estudiante.txt`

Reemplazar los valores con su información personal:

```
# Archivo de datos del estudiante
NOMBRE=Nombre completo
CORREO=Correo
MATERIAS=Curso1, Curso2, Curso3
```

## Ejecutar el programa

1. Ejecutar el programa principal desde el directorio `practicas_evaluadas/pe03/`:
   ```bash
   python src/app.py
   ```
2. En la terminal se mostrará un resumen con la información personalizada.
3. Verificar que se generó el archivo `salida/resumen.txt` con el mismo contenido.

## Realizar el _commit_ de los cambios

1. Agregar los archivos modificados al _staging area_:
   ```bash
   git add <archivos>
   ```
2. Verificar el estado de los archivos agregados:
   ```bash
   git status
   ```
3. Confirmar los cambios con un mensaje descriptivo:
   ```bash
   git commit -m "Personaliza datos del estudiante y genera resumen"
   ```
4. Comprobar el historial:
   ```bash
   git log --oneline
   ```

## Subir los cambios al repositorio remoto

Enviar los cambios al repositorio en GitHub:

```bash
git push
```

## Verificar los resultados en GitHub

1. Recargar la página del repositorio.
2. Confirmar que los archivos modificados aparecen en la lista.
3. Revisar el historial de commits y la fecha del cambio.
4. Abrir el archivo `salida/resumen.txt` y verificar que contiene la información personalizada.

## Evaluación

| Criterio                           | Ponderación |
| ---------------------------------- | ----------- |
| Clonación correcta del repositorio | 25%         |
| Personalización de datos           | 25%         |
| Ejecución del programa             | 25%         |
| Commit y push exitosos             | 25%         |
