"""
Criba de Eratóstenes

Hacer una lista de números primos

Si un número en la criba de Eratóstenes es 0, indica que es primo y se esparce al resto de la criba
en pasos de n (donde n es el número primo)

Si es distinto de 0, se continúa
"""

def criba_lista(n):
    lista_criba = [0] * (n - 1)  # de 2 a n

    for i in range(2, n + 1):
        if lista_criba[i - 2] != 0:
            continue
        for j in range(2 * i, n + 1, i):
            lista_criba[j - 2] = i

    print(lista_criba)  # 0 si es primo, o su mayor divisor primo

criba_lista(22)

# Indices: 0  1  2  3  4  5  6  7  8  9
# Número:  2  3  4  5  6  7  8  9 10  11
# Criba:   0  0  2  0  3  0  2  3  5  0


def criba_verificar_primo(n):
    es_primo = [True for _ in range(n + 1)]
    menor_primo = [-1 for _ in range(n + 1)]
    es_primo[0] = es_primo[1] = False

    for i in range(2, n + 1):
        if es_primo[i]:
            for j in range(2 * i, n + 1, i):
                es_primo[j] = False
                # Se agrega esta condición para determinar el menor primo (si se quita, se modifica al mayor primo)
                if menor_primo[j] == -1:
                    menor_primo[j] = i

    print(es_primo[n], menor_primo[n])

