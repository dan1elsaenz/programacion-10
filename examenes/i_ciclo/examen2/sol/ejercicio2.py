"""
Solución del Ejercicio 2
"""

def es_simetrica(lista):
    if len(lista) <= 1:
        return True
    if lista[0] != lista[-1]:
        return False
    return es_simetrica(lista[1:-1])

def main():
    # Ingreso de la entrada
    entrada = input("Ingrese una secuencia de enteros separados por coma: ")

    # Separar entrada de strings por ","
    lista_strings = entrada.split(",")

    # Declarar lista vacía de números
    lista_numeros = list()

    try:
        # Hacer type-casting de los strings a enteros
        for string in lista_strings:
            # Si falla acá, se ejecuta el except
            lista_numeros.append(int(string))

        # Ejecutar la función recursiva
        if es_simetrica(lista_numeros):
            print("La lista es simétrica.")
        else:
            print("La lista no es simétrica.")
    except ValueError:
        print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

main()
