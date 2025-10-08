# Iterativa
def euclides(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# Recursiva
def mcd(a,b):
    if b == 0:
        return a
    return mcd(b,a%b)
