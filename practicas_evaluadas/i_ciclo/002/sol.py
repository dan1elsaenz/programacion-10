# Solución Práctica evaluada 2

# Imprimir opciones
print("""Menú de opciones
1. Verificar divisibilidad
2. Invertir string
3. Cálculo de raíz n-ésima
""")

# Solicitar una opción al usuario
opcion = input("Seleccione una opción (1-3): ")

# Validación de las opciones por medio de if-elif-else
if opcion == "1":
    a = int(input("Ingrese el primer número (a): "))
    b = int(input("Ingrese el segundo número (b): "))

    if b == 0:
        print("No se puede dividir entre cero.")
    elif a % b == 0:
        print(f"{a} es divisible por {b}.")
    else:
        print(f"{a} no es divisible por {b}.")

elif opcion == "2":
    cadena = input("Ingrese una cadena de texto: ")

    print("Resultado:", cadena[::-1])

elif opcion == "3":
    x = float(input("Ingrese el número x: "))
    n = int(input("Ingrese el índice n: "))

    # Verificar que el valor del índice de la raíz sea mayor que 0
    if n > 0:
        # 1) Verificar que x sea mayor que 0: En este caso no importa si el índice es par o impar
        # 2) Verificar que si x es menor que 0, el índice debe ser impar
        # Como se utiliza un `or`: Con que uno de los dos se cumpla, la condición del `if` se vuelve True.
        if x >= 0 or (x < 0 and n % 2 != 0):
            resultado = x ** (1/n)
            print(f"La raíz {n}-ésima de {x} es: {resultado:.4f}")
        else:
            print("No se puede calcular la raíz par de un número negativo.")
    else:
        print("El índice n debe ser mayor que 0.")
else:
    print("Ingrese un número dentro de las opciones del menú.")
