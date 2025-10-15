"""
Escriba un programa en Python que permita analizar una oración ingresada por el usuario y realizar diversas operaciones sobre ella.
El programa debe mostrar un menú con las siguientes opciones:

- Convertir a mayúsculas: Muestra el texto ingresado completamente en mayúsculas.
- Convertir a minúsculas: Muestra el texto ingresado completamente en minúsculas.
- Contar la cantidad de palabras: Muestra cuántas palabras tiene la oración.
- Verificar si la oración empieza con una palabra específica: Solicita una palabra al usuario y verifica si la oración comienza con esa palabra.
- Reemplazar una palabra: Solicita dos palabras al usuario: una palabra a buscar en el texto y otra con la que se reemplazará.
- Salir: Finaliza el programa.
"""

# Ingresar la oracion
oracion = input("Ingrese la oracion a analizar: ")

# Mostrar menú
print("""=== Opciones disponibles ===
1) Convertir a mayusculas
2) Convertir a minusculas
3) Contar cantidad de palabras
4) Verificar si la oracion empieza con una palabra
5) Reemplazar una palabra
6) Salir
""")

# Ingresar una opcion
opcion = input("Ingrese la opcion: ").strip()

# Verificar que la opcion sea numérica
if not opcion.isdigit():
    print("La opción ingresada no es una opción numérica. Intente de nuevo.")
    exit(1) # Salir del programa: Código de error de `1`

# Convertir opción a entero
opcion = int(opcion)

# Validación de opciones
if opcion == 1:
    # Convertir a mayúsculas
    print(f"El string en mayuscula es: {oracion.upper()}")
elif opcion == 2:
    # Convertir a minuscula
    print(f"El string en minuscula es: {oracion.lower()}")
elif opcion == 3:
    # Contar palabras
    palabras = oracion.split()
    largo = len(palabras)
    print(f"El largo de mi string es: {largo}")
elif opcion == 4:
    # Verificar si comienza con un substring en especifico
    inicio = input("Ingrese el string que quiere verificar si está al inicio de la oracion: ")

    # if oracion.startswith(inicio):
        # print("La oración comienza con el substring ingresado.")
    # else:
        # print("La oración no comienza con el substring ingresado.")

    palabras = oracion.split()

    if palabras[0] == inicio:
        print("La oración comienza con la palabra ingresada.")
    else: 
        print("La oración no comienza la palabra ingresada.")

elif opcion == 5:
    # Reemplazar
    old = input("Ingrese el string a reemplazar: ")
    new = input("Ingrese el string por el que desea reemplazar: ")
    nueva_oracion = oracion.replace(old, new)
    print(f"La nueva oración es: {nueva_oracion}")
elif opcion == 6:
    # Salir
    print("Saliendo del programa")

