"""
Ejercicio 1: Conversor de notas a letras  

Escribe un programa que reciba un número representando una calificación (de 0 a 100) e imprima la letra correspondiente según la siguiente escala:  

- 90-100 → A  
- 80-89 → B  
- 70-79 → C  
- 60-69 → D  
- Menos de 60 → F  
"""

# Input() recibe la nota de la persona
nota = input("Ingrese la nota del estudiante: ")

# Convertir la nota recibida en entero, al verificar que es un valor numérico el que se ingresó
if nota.isdigit():
    nota = int(nota)
else:
    print("Se ingresó una nota que no es numérica.")
    exit(1)

# Clasificar esta nota dependiendo de los rangos establecidos para las notas
if nota >= 90 and nota <= 100:
    nota = "A"
elif nota >= 80 and nota < 90:
    nota = "B"
elif nota >= 70 and nota < 80:
    nota = "C"
elif nota >= 60 and nota < 70:
    nota = "D"
elif nota <= 60 and nota >= 0:
    nota = "F"
else:
    nota = "Nota inválida"

# Imprimir el resultado
print(f"La nota es: {nota}")

