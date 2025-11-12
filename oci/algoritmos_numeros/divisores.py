from math import sqrt

# Numero para hallar los divisores
n = 16
raiz = int(sqrt(n))

# Lista de divisores
divisores = [1]

if n != 1:
    divisores.append(n)

for i in range(2, raiz+1):
    if n % i == 0:
        divisores.append(i)

        if n // i != i:
            divisores.append(n//i)

divisores.sort()
print(divisores)
