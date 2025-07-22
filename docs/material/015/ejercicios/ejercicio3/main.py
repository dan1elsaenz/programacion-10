"""
Archivo `main.py`
Contiene el menú del programa
"""

import tareas_utils

def menu():
    continuar = True
    while continuar:
        print("""
1) Ver todas las tareas
2) Agregar una nueva tarea
3) Eliminar una tarea
4) Calcular la cantidad de tareas con prioridad alta
5) Salir
        """)

        opcion = input("Ingrese una opción del menú: ")

        # Leer las tareas del archivo `tareas.txt`
        nombre_archivo = "tareas.txt"
        lista_tareas = tareas_utils.leer_archivo(nombre_archivo)

        if opcion == "1":
            tareas_utils.ver_tareas(lista_tareas)

        elif opcion == "2":
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            prioridad = input("Ingrese la prioridad: ")
            tareas_utils.agregar_tarea(lista_tareas, nombre_tarea, prioridad)

        elif opcion == "3":
            nombre_tarea = input("Ingrese el nombre de la tarea a eliminar: ")
            lista_tareas = tareas_utils.eliminar_tarea(lista_tareas, nombre_tarea)

        elif opcion == "4":
            tareas_utils.tareas_alta_prioridad(lista_tareas)

        elif opcion == "5":
            print("Saliendo...")
            continuar = False

        else:
            print("Ingrese una de las opciones del menú")


menu()
