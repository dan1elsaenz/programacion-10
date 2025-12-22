"""
En una pequeña ciudad rodeada de vibrante vegetación y ríos cristalinos, Camila y Jonathan son apasionados por la historia y la cultura que se refleja en un símbolo nacional muy particular, el Yigüirro, el ave nacional. Ambos han dedicado años a coleccionar sellos con la imagen de este encantador pájaro.

Un buen día, un amigo historiador les solicita prestados algunos de sus sellos para una exposición. La cantidad varía cada vez, y se vuelve un tanto complicado para Camila y Jonathan llevar la cuenta de cuántos sellos les quedan luego de cada préstamo.

Necesitan tu ayuda para llevar un registro preciso. En cada ocasión, te informarán cuántos sellos tenían originalmente y cuántos su amigo les ha pedido prestados. Con esa información, deberás indicarles cuántos sellos les quedan. Recuerda, si el amigo les solicita más sellos de los que tienen, simplemente entregan todos sus sellos.
"""

# Ingresar los números
numeros = input("Ingrese dos números: ")

# Separar los números
num1, num2 = numeros.split()

# Convertirlos a enteros
num1 = int(num1)
num2 = int(num2)

# Si la resta es mayor que 0, imprimo la resta
if num1 - num2 > 0:
    print(num1 - num2)
# Si la resta es menor que 0, me quedan 0
elif num1 - num2 < 0:
    print(0)

