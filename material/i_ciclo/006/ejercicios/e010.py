"""
Ejercicio 10: Menú interactivo con opciones

Crea un menú con las siguientes opciones:

Ingresar nombre
Mostrar saludo personalizado
Salir
Debe funcionar con un while hasta que el usuario elija salir. Si selecciona la opción 2 sin haber ingresado un nombre, muestra un mensaje de advertencia.
"""

opcion = ""
nombre = ""


while opcion != "3":
    print("""
    1. Ingresar nombre
    2. Mostrar saludo personalizado
    3. Salir
    """)
    opcion = input("Ingrese una opción de las mostradas en el menú: ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
    elif opcion == "2":
        if nombre == "":
            print("No ha ingresado su nombre. Seleccione primero la opción 1.")
        else:
            print(f"Hola {nombre}")
    elif opcion == "3":
        print("Saliendo del programa...")
    else:
        print("Indicó una opción inválida.")



