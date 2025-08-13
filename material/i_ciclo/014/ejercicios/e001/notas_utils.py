# Leer contenidos de notas
def leer_notas(nombre_archivo):
    # Declaración de lista
    lista_estudiantes = []

    # Leer contenidos del archivo `notas.csv`
    try:
        with open('notas.csv') as f:
            lista_contenidos = f.readlines()

            for linea in lista_contenidos:
                nombre = linea[:linea.find(",")]
                nota = int(linea[linea.find(",")+1:])
                lista_estudiantes.append((nombre, nota))
    except FileNotFoundError:
        print("El archivo no existe, se va a crear en este directorio")
        with open('notas.csv', 'x') as f:
            print("Creado")

    return lista_estudiantes

# Calcular promedios de los estudiantes
def calcular_promedios(lista_estudiantes):
    if len(lista_estudiantes) == 0:
        print("Promedio inválido: lista vacía")
    else:
        promedio = 0

        # lista_estudiantes = [(nombre, nota), ...]
        # Sumar todas las notas
        for _, nota in lista_estudiantes:
            promedio += nota

        # Dividir entre el número de estudiantes
        promedio /= len(lista_estudiantes)

        print(f"Promedio: {promedio:.2f}")

# Mostrar resumen de aprobados y reprobados
def mostrar_resumen(lista_estudiantes):
    aprobados = []
    reprobados = []

    # Clasificar en aprobados y reprobados
    for nombre, nota in lista_estudiantes:
        if nota > 60:
            aprobados.append(nombre)
        else:
            reprobados.append(nombre)

    # Imprimir estudiantes aprobados
    print("Estudiantes aprobados")
    for nombre in aprobados:
        print(f"\t- {nombre}")

    # Imprimir estudiantes reprobados
    print("Estudiantes reprobados")
    for nombre in reprobados:
        print(f"\t- {nombre}")


# Agregar nuevo estudiante
def agregar_estudiante(nombre, nota):
    # Guardar los datos en el archivo
    with open('notas.csv', 'a') as f:
        f.write(f"{nombre},{nota}\n")

