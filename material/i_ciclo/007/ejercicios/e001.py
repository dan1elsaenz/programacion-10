"""
Solicitar al usuario la cantidad de estudiantes a registrar
Solicitar nombre y nota de cada uno de los estudiantes

Luego muestra:

Lista de estudiantes con su nota
Promedio general del grupo
Cuántos estudiantes aprobaron (nota >= 70)
Cuál fue el mejor y el peor estudiante
Requisitos:

Usar dos listas: una para nombres y otra para notas
"""

# Solicitar la cantidad de estudiantes
cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))

# Definir una lista donde se van a guardar los nombres
nombres = []

# Definir lista de notas
notas = []

# Solicitar los datos de los estudiantes
for i in range(1, cantidad+1):
    # Solicitar nombre
    nombre = input(f"Nombre del estudiante {i}: ")

    # Agregar nombre a la lista de nombres
    nombres.append(nombre)

    # Solicitar la nota
    nota = int(input(f"Nota del estudiante {i}: "))

    # Agregar nota a la lista de notas
    notas.append(nota)


# Mostrar todas los nombres y notas
print("\nNotas ingresadas: ")
for i in range(cantidad):
    # Imprimir la información
    print(f"{nombres[i]} - {notas[i]}")

# Mostrar promedio
promedio = sum(notas) / cantidad

print(f"Promedio: {promedio}")

# Mostrar cuántos aprobaron
contador_aprobados = 0

for nota in notas:
    if nota >= 70:
        contador_aprobados += 1

print(f"Aprobados: {contador_aprobados}")

# Mostrar mejor y peor estudiante

# índices de la mejor y peor nota
indice_max = 0
indice_min = 0

for i in range(cantidad):
    # Nota mayor
    if notas[i] > notas[indice_max]:
        indice_max = i

    # Nota menor
    if notas[i] < notas[indice_min]:
        indice_min = i

# Mostrar mejor estudiante
nombre_mejor_nota = nombres[indice_max]
mejor_nota = notas[indice_max]

print(f"Mejor estudiante: {nombre_mejor_nota} ({mejor_nota})")

# Mostrar peor estudiante
nombre_peor_nota = nombres[indice_min]
peor_nota = notas[indice_min]

print(f"Peor estudiante: {nombre_peor_nota} ({peor_nota})")


