"""
Archivo `asistencias_utils.py`
Contiene la definición de las funciones de asistencias
"""

def leer_asistencias(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            contenido = f.readlines()

            # Quitar salto de línea
            for i in range(len(contenido)):
                contenido[i] = contenido[i][:-1]

            return contenido
    except FileNotFoundError:
        print("El archivo no existe.")
        return []

def contar_asistencias(lista_nombres):
    # Diccionario
    conteo = {}

    # Contar cuántas veces aparecen
    for nombre in lista_nombres:
        conteo[nombre] = conteo.get(nombre, 0) + 1
    return conteo

def guardar_reporte(conteo):
    # Ordenar estudiantes con base en sus asistencias
    ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    # Escribir los estudiantes de más a menos asistencias
    with open("reporte_asistencia.txt", "w") as f:
        for nombre, cantidad in ordenado:
            f.write(f"{nombre}: {cantidad}\n")

def guardar_frecuentes(conteo):
    with open("frecuentes.txt", "w") as f:
        for nombre, cantidad in conteo.items():
            # Verificar que la cantidad de asistencias sea mayor que 1
            if cantidad > 1:
                f.write(nombre + "\n")

def mostrar_estadisticas(conteo):
    # Verificar que el diccionario de conteo tiene contenidos
    if not conteo:
        print("No hay datos para mostrar.")
        return

    # Obtener el estudiante con más asistencias
    max_estudiante = ["", 0]
    for nombre, cantidad in conteo.items():
        if max_estudiante[1] < cantidad:
            max_estudiante[0] = nombre
            max_estudiante[1] = cantidad

    # Obtener el total de estudiantes
    total_estudiantes = len(conteo)

    # Obtener el total de asistencias (se analizan los valores)
    total_asistencias = 0
    for cantidad in conteo.values():
        total_asistencias += cantidad

    # Calcular el promedio de asistencias
    promedio = total_asistencias / total_estudiantes

    # Imprimir resultados
    print(f"Estudiante con más asistencias: {max_estudiante[0]}")
    print(f"Total de estudiantes distintos: {total_estudiantes}")
    print(f"Promedio de asistencias por estudiante: {promedio:.2f}")
