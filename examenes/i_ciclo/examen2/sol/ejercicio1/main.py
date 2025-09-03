"""
Archivo `main.py`
Cuerpo de la aplicación
"""

# Importar funciones del módulo `asistencia_utils.py`
from asistencia_utils import (
    leer_asistencias,
    contar_asistencias,
    guardar_reporte,
    guardar_frecuentes,
    mostrar_estadisticas
)

def main():
    nombre_archivo = "asistencia.txt"

    nombres = leer_asistencias(nombre_archivo)
    conteo = contar_asistencias(nombres)

    continuar = True
    while continuar:
        print("\nMenú de opciones:")
        print("1. Ver estadísticas")
        print("2. Generar reporte de asistencia")
        print("3. Generar lista de estudiantes frecuentes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_estadisticas(conteo)
        elif opcion == "2":
            guardar_reporte(conteo)
        elif opcion == "3":
            guardar_frecuentes(conteo)
        elif opcion == "4":
            print("Saliendo del programa...")
            continuar = False
        else:
            print("Opción inválida.")

main()

