# Se puede hacer con sqrt() del modulo math

n = 25
x = 2 # Menor divisor primo
esPrimo = True

while x*x <= n:
    if n%x == 0:
        esPrimo = False
        break
    x+=1

print(esPrimo)
