# Solución Práctica Evaluada 1

print("Bienvenido a la calculadora de [NOMBRE ESTUDIANTE]")

# Ingreso de los números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Imprimir resultados
print("-- Resultados --")
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")

# Uso del operador ternario para verificar que si num2 es 0, no se puede realizar la división
print("No se puede realizar la división.") if num2 == 0 else print(f"División: {num1 / num2 : .2f}")

# También, al imprimir la división, se utilizó la notación `:.2f` para indicar que se va a redondear a dos espacios decimales

