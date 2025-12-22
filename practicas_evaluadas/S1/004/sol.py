def contar_vocales(cadena):
    # Caso base: String vacío
    if not cadena:
        return 0

    # Extraer el primer caracter y convertirlo a minúscula
    primera = cadena[0].lower()

    # Verificar si el primer caracter es una vocal
    esVocal = 1 if primera in "aeiou" else 0

    # Retornar recursión
    return esVocal + contar_vocales(cadena[1:])

# Entrada del usuario
texto = input("Ingrese una cadena: ")
# Salida del resultado
print("Cantidad de vocales:", contar_vocales(texto))
