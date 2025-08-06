# Solución del Ejercicio 2

palabra = "programacion"
nueva_palabra = ""

for letra in palabra:
    if letra in "aeiou":
        nueva_palabra += "*"
    else:
        nueva_palabra += letra

print(nueva_palabra)
