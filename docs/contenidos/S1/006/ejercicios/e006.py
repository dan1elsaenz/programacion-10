"""
Ejercicio 6: Frecuencia de letra en una palabra

Solicita al usuario una palabra y una letra.
Recorre la palabra con un bucle while y cuenta cuántas veces aparece la letra (sin usar .count()).
"""

# Solicitar una palabra y letra al usuario
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")

contador = 0 # Cuántas veces aparece la letra
idx = 0      # Índice de cada letra en la palabra (para recorrer)

# Repetir hasta que se llega al final de la palabra (por índice)
while idx < len(palabra):
    # Comparar si la letra que voy recorriendo es igual a la letra objetivo
    if palabra[idx] == letra:
        contador += 1

    idx += 1 # Aumentar el índice en 1 para asegurarse que se está recorriendo el string

# Imprimir resultados
print(f"La letra {letra} aparece {contador} veces en la palabra {palabra}.")

