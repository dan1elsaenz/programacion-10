"""
Criba de Eratostenes:

Una lista donde se coloca 0 si el numero es primo, o se coloca su mayor divisor primo
si es un numero compuesto
"""


def criba_lista(n):
    lista_criba = list()

    # Creacion de la lista inicializada en 0 para n elementos
    for _ in range(2, n+1):
        lista_criba.append(0)

    # Implementacion del algoritmo
    for i in range(2, n+1):
        if lista_criba[i-2] != 0:
            continue

        for j in range(2*i, n+1, i):
            lista_criba[j-2] = i

    print(lista_criba)

# print([i for i in range(2, 15+1)])
criba_lista(15)

def criba_verificar_primo(n):

    es_primo = [True for _ in range(n+1)]

    menor_primo = [-1 for _ in range(n+1)]

    es_primo[0] = es_primo[1] = False

    primos = []

    for i in range(2, n+1):
        if es_primo[i]:
            primos.append(i)

            for j in range(i*i, n+1, i):
                es_primo[j] = False

                if menor_primo[j] == -1:
                    menor_primo[j] = i


    print(es_primo[n], menor_primo[n])

criba_verificar_primo(6)