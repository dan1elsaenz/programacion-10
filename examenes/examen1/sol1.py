# ejercicio1.py

# Solicita la cantidad de personas a registrar
cantidad = int(input("Cantidad de personas para el registro: "))

# Listas para clasificar personas
permitidos_nombres = []
permitidos_edades = []
menores = []
mayores = []

# Registrar cada persona
for i in range(1, cantidad + 1):
    nombre = input(f"Nombre de la persona {i}: ")
    edad = int(input("Edad: "))

    if 15 <= edad <= 18:
        permitidos_nombres.append(nombre)
        permitidos_edades.append(edad)
    elif edad < 15:
        menores.append(nombre)
    else:
        mayores.append(nombre)

# Mostrar resultados
print("Personas permitidas:", permitidos_nombres)
print("Rechazados menores de edad:", len(menores))
print("Rechazados mayores de edad:", len(mayores))

# Encontrar la persona permitida con mayor edad
if len(permitidos_edades) > 0:
    edad_mayor = max(permitidos_edades)
    indice = permitidos_edades.index(edad_mayor)
    print("Persona permitida con mayor edad:", permitidos_nombres[indice])
else:
    print("No hubo personas permitidas.")
