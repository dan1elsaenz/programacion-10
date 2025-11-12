"""
Ejercicio 1

Crear un programa que lea un archivo de texto llamado `numeros.txt` que contiene un número por línea.
El programa debe:

- Leer los números.
- Imprimir la suma total y el promedio.
- Detectar y manejar errores:
    - Si el archivo no existe, mostrar un mensaje.
    - Si hay contenido no numérico, ignorar esas líneas y continuar.
- Incluir una función recursiva que calcule la suma de los números.

Opcional: Si el archivo está vacío o no existe, generarlo con 10 números aleatorios entre 1 y 100.
"""

# Importar la función `randint(inicio, fin)` que genera enteros aleatorios
from random import randint

def leer_archivo(nombre_archivo):
    """
    Leer los contenidos del archivo en forma de lista y los retorna
    Manejo de errores:
        - Si el archivo no existe, mostrar un mensaje
    """
    lista_strings = list()

    try:
        with open(nombre_archivo, 'r') as f:
            lista_strings = f.readlines()

            if not lista_strings:
                raise FileNotFoundError

    except FileNotFoundError:
        with open(nombre_archivo, 'w') as f:
            # Generar 10 números aleatorios y escribirlos en el archivo
            for _ in range(10):
                numero_aleatorio = randint(1, 100)
                lista_strings.append(str(numero_aleatorio) + "\n")
            f.writelines(lista_strings)

    return lista_strings

def procesar_datos(lista_strings):
    """
    Convertir strings a enteros
    Manejo de errores:
        - Si hay contenido no numérico, ignorar esas líneas y continuar
    """
    lista_numeros = list()

    for string in lista_strings:
        try:
            lista_numeros.append(int(string))
        except ValueError:
            continue

    return lista_numeros


def calcular_suma(lista_numeros):
    """
    Calcular la suma de la lista de números de forma recursiva
    """
    if not lista_numeros:
        return 0

    return lista_numeros[0] + calcular_suma(lista_numeros[1:])


def imprimir_resultados(suma_total, cantidad_numeros):
    """
    Imprimir la suma total y el promedio
    """
    print(f"Suma total: {suma_total}")
    print(f"Promedio: {suma_total/cantidad_numeros}")

def main():
    """
    Llama a las funciones del programa
    """
    nombre_archivo = "numeros.txt"

    lista_strings = leer_archivo(nombre_archivo)

    lista_numeros = procesar_datos(lista_strings)

    suma_total = calcular_suma(lista_numeros)

    cantidad_numeros = len(lista_numeros)
    imprimir_resultados(suma_total, cantidad_numeros)

main()
