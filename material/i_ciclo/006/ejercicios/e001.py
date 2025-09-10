"""
Ejercicio 1: Contador con condiciones

Escribe un programa que imprima los números del 1 al 20, pero:

Si el número es múltiplo de 3, imprime "Fizz".
Si es múltiplo de 5, imprime "Buzz".
Si es múltiplo de ambos, imprime "Fizz Buzz". Usa un bucle while.
"""

# Definición de variable num con valor inicial de 1
num = 1

# Loop hasta que num sea 20
while num <= 20:
    # Mensaje con el número
    mensaje = f"{num}"

    # Si es múltiplo de 3, se le concatena Fizz
    if num % 3 == 0:
        mensaje += " Fizz"

    # Si es múltiplo de 5, se le concatena Buzz
    if num % 5 == 0:
        mensaje += " Buzz"

    # Imprimir el mensaje resultante
    print(mensaje)

    # IMPORTANTE: Incrementar el número (condición de terminación del loop)
    num += 1

