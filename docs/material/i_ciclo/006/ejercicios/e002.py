"""
Ejercicio 2: Validación de número primo

Solicita al usuario un número mayor que 1. Luego determina si es primo utilizando un bucle while que verifique sus divisores.
"""

# Definición de número primo n: Número divisible entre 1 y n

# Validación de la entrada
num = ""         # Declaración de num
continuar = True # Condición del while

while continuar:
    num = input("Ingrese un número entero positivo: ")

    # Comprobar que el número contenga únicamente dígitos
    if not num.isdigit():
        print("Ingrese únicamente valores enteros positivos. Intente de nuevo.")


    elif int(num) < 1:
        print("Ingrese únicamente valores enteros positivos. Intente de nuevo.")

    else:
        continuar = False

# Convertir el número a entero después de comprobar su validez
num = int(num)

# Determinar si es primo por medio de un while
divisor = 2     # Primer divisor posible a verificar
esPrimo = True  # Condición de si es primo

# Recorrer desde divisor = 2 hasta divisor < num ** 0.5 (raíz cuadrada del número ingresado)
while divisor < num ** 0.5 and esPrimo:
    # Si el residuo de num/divisor es 0, significa que no es primo
    if num % divisor == 0:
        esPrimo = False # Cambiar el estado de la condición
    divisor += 1 # Aumentar divisor

# Imprimir resultados
if esPrimo:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")

