# ejercicio2.py

# Solicitar la frase
frase = input("Ingrese una frase: ")

# Dividir en palabras
palabras = frase.split()

# Variables para análisis
terminan_en_a = 0
palabra_larga = ""
palabra_oculta = ""
palabras_5_letras = 0
invertidas = []

# Recorrer las palabras
for palabra in palabras:
    # Palabras que terminan con "a"
    if palabra.endswith('a'):
        terminan_en_a += 1

    # Palabra de mayor longitud
    if len(palabra) > len(palabra_larga):
        palabra_larga = palabra

    # Palabra oculta: Obtener la última letra de cada palabra
    palabra_oculta += palabra[-1]

    # Extra: Palabras que tengan un largo de 5 caracteres
    if len(palabra) == 5:
        palabras_5_letras += 1

    # Extra: Invertir cada palabra y agregarla a la lista de invertidas
    invertidas.append(palabra[::-1])

# Mostrar resultados
print("Palabras que terminan con 'a':", terminan_en_a)
print("Palabra más larga:", palabra_larga)
print("Palabra oculta:", palabra_oculta)
print("Palabras con exactamente 5 letras:", palabras_5_letras)
print("Palabras invertidas:", invertidas)

