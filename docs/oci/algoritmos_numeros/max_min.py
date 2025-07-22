l = [213, 34, 12, 43, 65, 78, 100, 1, -1 , -234]

# Encontrar el max/min

maximo = None
minimo = None
for i in l:
    # Encontrar el maximo
    if maximo == None or maximo < i:
        maximo = i

    # Encontrar el minimo
    if minimo == None:
        minimo = i
    elif minimo > i:
        minimo = i

print(maximo)
print(minimo)

# Encontrar el indice del max/min

indice_max = None
indice_min = None

for i in range(len(l)):
    # Encontrar el maximo
    if indice_max == None or indice_max < l[i]:
        indice_max = i

    # Encontrar el minimo
    if indice_min == None:
        indice_min = i
    elif indice_min > l[i]:
        indice_min = i

print(indice_max)
print(indice_min)



