"""
Archivo `tareas_utils.py`

Contiene las funciones para:
    1) Ver todas las tareas.
    2) Agregar una nueva tarea (solicitar nombre y prioridad).
    3) Eliminar una tarea por nombre.
    4) Calcular la cantidad de tareas con prioridad alta utilizando una función recursiva.
"""

def leer_archivo(nombre_archivo):
    """
    Leer los contenidos del archivo
    Devuelve `lista_tareas` de la forma: [(nombre_tarea, prioridad)]
    Manejo de errores:
        - Apertura y lectura del archivo
    """
    try:
        with open(nombre_archivo, 'r') as f:
            lista_tareas = list()

            for linea in f.readlines():
                nombre, prioridad = linea.split(";")
                lista_tareas.append((nombre, prioridad))

            return lista_tareas
    except FileNotFoundError:
        print("El archivo indicado no existe")
        exit(1)


def escribir_archivo(nombre_archivo, lista_tareas):
    """
    Escribir los contenidos de `lista_tareas` en el archivo
    """
    with open(nombre_archivo, 'w') as f:
        for nombre, prioridad in lista_tareas:
            f.write(f"{nombre};{prioridad}\n")

def ver_tareas(lista_tareas):
    """
    Imprimir todas las tareas almacenadas
    """
    print("=== Tareas almacenadas ===")
    for nombre_tarea, prioridad in lista_tareas:
        print(f"{nombre_tarea}: {prioridad}")


def agregar_tarea(lista_tareas, nombre_tarea, prioridad):
    """
    Agregar una nueva tarea con el nombre y prioridad indicados
    """
    lista_tareas.append((nombre_tarea, prioridad))

def eliminar_tarea(lista_tareas, nombre_tarea):
    """
    Eliminar una tarea con el nombre recibido
    """
    nueva_lista_tareas = list()

    existe = False
    for tupla in lista_tareas:
        if tupla[0] != nombre_tarea:
            nueva_lista_tareas.append(tupla)
        else:
            existe = True
            continue

    if not existe:
        print("La tarea a eliminar no existe")

    return nueva_lista_tareas

def tareas_alta_prioridad(lista_tareas):
    """
    Calcular la cantidad de tareas con alta prioridad
    """
    pass
