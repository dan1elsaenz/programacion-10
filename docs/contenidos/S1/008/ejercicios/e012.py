"""
Ejercicio 12: Filtro de nombres duplicados

Solicita al usuario una lista de nombres.
Elimina duplicados con un set, pero conserva el orden original.
(Tip: usar un set auxiliar y un loop).
"""

# Solicitar los nombres
nombres = input("Ingrese una lista de nombres: ").split()
# Daniela Sofia Pilar Isaac Esteban Daniela Esteban Pilar Daniela Daniela

# Nombres revisados
vistos = set()

# Nombres únicos
nombres_unicos = []

for nombre in nombres:
    # Si el nombre no ha sido visto, entonces es nuevo
    if nombre not in vistos:
        vistos.add(nombre)
        nombres_unicos.append(nombre)

print(f"La lista de nombres únicos es: {nombres_unicos}")

