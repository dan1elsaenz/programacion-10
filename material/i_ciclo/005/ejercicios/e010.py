"""
Ejercicio 10: Contar números pares e impares en una lista

Dada una lista de números enteros, cuenta cuántos son pares y cuántos son impares.

```
Entrada: [1, 2, 3, 4, 5, 6]  
Salida: "Pares: 3, Impares: 3"
```
"""


# Declarar contadores
contadorPares = 0
contadorImpares = 0

# Declaración de lista
lista = [1, 2, 3, 4, 5, 6]

# Recorrer la lista
for numero in lista:
    # Verificar residuo respecto a 2
    if numero % 2 == 0:
        contadorPares += 1
    elif numero & 2 == 1:
        contadorImpares += 1

# Imprimir resultados
print(f"Pares: {contadorPares}, Impares: {contadorImpares}")

