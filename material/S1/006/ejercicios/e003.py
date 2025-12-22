"""
Ejercicio 3: Suma acumulativa con control de errores

Pide al usuario que ingrese números uno por uno.
Suma los valores válidos (enteros positivos) hasta que el usuario escriba "fin". Si ingresa algo incorrecto (como letras o números negativos), ignóralos y continúa.
"""

# Declarar variable de suma
suma = 0
entrada = ""

while entrada != "fin":
    entrada = input("Ingrese un número entero positivo: ")

    if entrada.isdigit() and int(entrada) > 0:
        suma += int(entrada)

print(f"La suma resultante es: {suma}")
