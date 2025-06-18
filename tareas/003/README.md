# Tarea 3: Sistema de gestión de logs de eventos

## Enunciado

Desarrolle un programa en Python que permita gestionar un archivo de logs llamado `logs.txt`.
Cada línea del archivo representa un evento del sistema con la siguiente estructura:

```
[tipo] mensaje
```

donde `tipo` puede ser:
- `INFO` – mensajes informativos
- `ERROR` – errores del sistema
- `WARNING` – advertencias

### Ejemplo de contenido
```
[INFO] Inicio del sistema
[ERROR] No se pudo conectar a la base de datos
[WARNING] Memoria al 90%
```

---

## Funcionalidades del programa

El programa debe permitir al usuario:

1. **Agregar evento nuevo**
   - Mostrar un **submenú** para seleccionar el tipo de evento: `INFO`, `ERROR`, `WARNING`.
   - Solicitar el mensaje del evento.
   - Guardar la entrada en `logs.txt` con formato `[TIPO] mensaje`.

2. **Ver todos los eventos registrados**
   - Leer el archivo y mostrar todas las líneas.

3. **Filtrar eventos por tipo**
   - Mostrar solo los eventos que coincidan con el tipo seleccionado.

4. **Eliminar eventos por tipo**
   - Eliminar todas las entradas de un tipo específico.
     *Pista: Leer todas las líneas, filtrar las que no coincidan y sobrescribir el archivo usando el modo `'w'`.*

5. **Mostrar resumen de eventos**
   - Mostrar cuántos eventos hay en total y cuántos hay por tipo (`INFO`, `ERROR`, `WARNING`).

6. **Salir del programa**

---

## Archivos requeridos

### `main.py`
- Muestra el menú principal y el submenú de tipos.
- Llama a las funciones definidas en `log_utils.py`.

### `log_utils.py`
Debe contener las siguientes funciones:

```python
def agregar_log(tipo, mensaje):
    # Escribe una nueva línea en `logs.txt` en formato [TIPO] mensaje
    pass

def leer_logs():
    # Devuelve una lista de todas las entradas
    pass

def filtrar_logs(tipo):
    # Devuelve solo las entradas del tipo indicado
    pass

def eliminar_logs_por_tipo(tipo):
    # Reescribe `logs.txt` sin las líneas del tipo indicado
    pass

def contar_logs(lista_logs):
    # Retorna total de eventos y cuántos hay de cada tipo
    pass
```

---

## Criterios de evaluación

| Criterio                                                     | Puntos |
|--------------------------------------------------------------|--------|
| Escritura y lectura correcta con `open()`                    | 25     |
| Uso de múltiples archivos (`main.py`, `log_utils.py`)        | 10     |
| Implementación de `try-except` para errores de archivo       | 10     |
| Submenú correcto para seleccionar tipo de evento             | 10     |
| Filtro y conteo de eventos por tipo                          | 10     |
| Eliminación funcional por tipo (reescritura de archivo)      | 15     |
| Validación básica de entradas                                | 10     |
| Diseño claro del menú y código legible                       | 5      |
| Documentación clara                       | 5      |
| **Total**                                                    | **100** |
