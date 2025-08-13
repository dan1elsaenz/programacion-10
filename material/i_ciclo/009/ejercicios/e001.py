"""
1. Sistema de evaluación cruzada entre estudiantes

Solicita a cada estudiante que califique a otros compañeros con una nota del 1 al 10.
Guarda los resultados en un diccionario anidado.

- Calcula el promedio recibido por cada estudiante.
- Muestra quién fue el estudiante mejor evaluado.
"""

# Solicitar la cantidad de estudiantes que se van a calificar
cantidad = int(input("Cantidad de estudiantes: "))

# Solicitar los nombres de los estudiantes (claves del diccionario)

diccionario = dict()

for i in range(cantidad):
    # Ingreso del nombre
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")

    # Ingresar nombre al diccionario como clave y un diccionario vacío como valor
    diccionario.update({ nombre : dict() })

# Solicitar las notas que le pone un estudiante a los demás

for estudiante, notas in diccionario.items():

    print(f"\n--- Notas para {estudiante} ---")

    for companero in diccionario.keys():
        # Revisar que el estudiante a calificar sea distinto que el que califica
        if estudiante == companero:
            continue

        # Solicitar nota
        nota = int(input(f"Nota de {companero} a {estudiante}: "))

        # Agregar nota con la clave del compañero que califica y el valor de la nota agregada
        notas.update({ companero : nota })

# Imprimir promedio por estudiante

notas_promedio = list() # [(Ana, 9), (Luis, 8.5), (Carlos, 8)]

print("\n--- Notas promedio ---")

for estudiante, notas in diccionario.items():

    suma_total = 0

    # Calcular el promedio
    for nota in notas.values():
        suma_total += nota

    promedio = suma_total / (cantidad - 1)

    print(f"{estudiante}: {promedio}")

    notas_promedio.append((estudiante, promedio))

# Imprimir el estudiante mejor evaluado
mejor_estudiante = ["", 0]

for estudiante, nota in notas_promedio:
    if mejor_estudiante[1] < nota:
        mejor_estudiante[1] = nota
        mejor_estudiante[0] = estudiante

print(f"\n--- Mejor promedio ---\n{mejor_estudiante[0]}: {mejor_estudiante[1]}")

