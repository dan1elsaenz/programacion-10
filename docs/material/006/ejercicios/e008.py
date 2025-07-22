"""
Ejercicio 8: Suma de dígitos

Solicita un número entero positivo y calcula la suma de sus dígitos uno a uno usando solo operaciones aritméticas.
Ejemplo: 342 → 3 + 4 + 2 = 9.
"""

# Caso sin strings

num = ""          # Número para ingresar del input
detenerse = False # Condición del while para solicitar el número

# Repetir hasta que se ingrese un número válido
while not detenerse:
    num = input("Ingrese un número entero positivo: ")

    # Si el número contiene únicamente dígitos y es mayor que 0, se detiene el loop 
    if num.isdigit() and int(num) > 0:
        detenerse = True

# Conversión a entero
num = int(num)

# Calcular la suma de los dígitos

# 342 % 10 = 2 (unidades)
# 342 // 10 = 34
# 34 % 10 = 4 (decenas)
# 34 // 10 = 3 
# 3 % 10 = 3 (centenas)
# 3 // 10 = 0 (sale del loop)

suma = 0 # Almacenar la suma total

# Repetir hasta que el número sea 0
while num > 0:
    digito = num % 10 # Obtener las unidades del número
    suma += digito # Agregar las unidades a la suma total
    num //= 10 # Parte entera respecto a 10 (quitar las unidades anteriores)

print(f"La suma de los dígitos es: {suma}")

# Caso en que se usan strings
string = str(num)

suma = 0 # Almacenar suma total
idx = 0  # Almacenar el índice del recorrido del string

# Repetir mientras el índice sea menor que el largo del string
while idx < len(string):
    suma += int(string[idx]) # Sumar cada dígito

    idx += 1 # Aumentar el índice para seguir el recorrido

print(f"La suma de los dígitos es: {suma}")

