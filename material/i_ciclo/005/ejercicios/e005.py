"""
Ejercicio 5: Convertir palabras a mayúsculas si tienen más de 5 letras  

Dada una lista de palabras, devuelve una nueva lista donde las palabras con más de 5 letras estén en mayúsculas y las demás queden igual.  

```
Entrada: ["hola", "elefante", "mundo", "estrella"]  
Salida: ["hola", "ELEFANTE", "mundo", "ESTRELLA"]
```
"""

palabra = "programacion"
nueva_palabra = ""

for letra in palabra:
    if letra in "aeiou":
        nueva_palabra += "*"
    else:
        nueva_palabra += letra

print(nueva_palabra)

