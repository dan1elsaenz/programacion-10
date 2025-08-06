
# Saludar
print("Bienvenido a la calculadora")

# Preguntar cuál operación desea realizar
operacion = input("""Seleccione cuál operación desea realizar:
1. Suma
2. Resta
3. Multiplicación
4. División\n""")

if operacion not in "1234":
    print("Operación ingresada incorrecta.")
else:
    # Ingreso de los números
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))

    # Verificar cuál operación se seleccionó
    if operacion == "1":
        print(f"Suma = {n1 + n2}")
    elif operacion == "2":
        print(f"Resta = {n1 - n2}")
    elif operacion == "3":
        print(f"Multiplicación = {n1 * n2}")
    elif operacion == "4":
        print(f"División = {n1 / n2}")


