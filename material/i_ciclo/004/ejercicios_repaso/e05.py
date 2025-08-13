"""
Ejercicio 5: Comprobar si un número es múltiplo de otro

Pide dos números y muestra si el primero es múltiplo del segundo.

```
Entrada: "12 4"
Salida: "12 es múltiplo de 4."
```
"""

# Ingresar los números
numeros = input("Ingrese dos números: ")

num1, num2 = numeros.split()
num1 = int(num1)
num2 = int(num2)

if num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}")
else:
    print(f"{num1} no es múltiplo de {num2}")


