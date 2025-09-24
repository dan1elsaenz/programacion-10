"""
Escribir un programa que reciba tres notas.
El estudiante reprueba si alguna nota es menor que 50 o si el promedio de
las tres es menor que 70.
"""

notas = [int(x) for x in input().split(", ")]

promedio = sum(notas) / len(notas)

es_valido = True
for nota in notas:
    if nota < 50:
        es_valido = False

if not es_valido or promedio < 70:
    print("Reprobado")
else:
    print("Aprobado")
