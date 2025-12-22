# Archivo `main.py`
# Menú del programa

import notas_utils

def menu():
    continuar = True
    while continuar:

        print("""
    ==== Gestor de notas ====
    1. Agregar estudiante
    2. Calcular el promedio
    3. Mostrar resumen de aprobados/reprobados
    4. Salir
        """)
        opcion = input("Ingrese una opción de las mostradas en el menú: ")

        lista_estudiantes = notas_utils.leer_notas("notas.csv")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = input(f"Ingrese la nota de {nombre}: ")

            notas_utils.agregar_estudiante(nombre, nota)
        elif opcion == "2":
            notas_utils.calcular_promedios(lista_estudiantes)
        elif opcion == "3":
            notas_utils.mostrar_resumen(lista_estudiantes)
        elif opcion == "4":
            print("Saliendo...")
            continuar = False
        else:
            print("Ingrese una opción numérica válida.")

menu()
