def cargar(vagones, p, v):
    """
    func agregar
    """
    for i in range(p):
        vagones[i] += v


def consultar(vagones, p):
    """
    func consultar
    """
    return vagones[p - 1]


"""
main
"""
N = int(input())  # Cantidad de vagones
Q = int(input())  # Cantidad de operaciones

vagones = [0] * N

for _ in range(Q):
    linea = input().split()  # ["A", "p", "v"] / ["C", "p"]

    if linea[0] == "A":
        p = int(linea[1])
        v = int(linea[2])

        cargar(vagones, p, v)

    elif linea[0] == "C":
        p = int(linea[1])

        print(consultar(vagones, p))
