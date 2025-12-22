"""
Pide al usuario que ingrese una lista de precios de productos.
Luego:

- Calcula el total de la compra
- Muestra cuántos productos son mayores a 1000 colones
- Muestra el precio más caro y más barato
- Aplica un 10% de descuento si el total supera los 5000 colones
"""

# Solicitar la lista de precios al usuario
precios_str = input("Ingrese los precios de los productos separados por coma: ").split(", ")

# Lista de precios en entero
precios = []

# Convertir de lista de precios_str a entero y agregarlos a la lista de precios enteros
for i in range(len(precios_str)):
    precios.append(int(precios_str[i]))

# Calcular el total de la compra
total = sum(precios)
print(f"Total antes del descuento: {total}")

# Productos mayores a 1000
contador = 0

for precio in precios:
    if precio > 1000:
        contador += 1

print(f"Productos mayores a 1000 colones: {contador}")

# Precio más caro
mayor_precio = max(precios)
print(f"Precio más caro: {mayor_precio}")

# Precio más barato
menor_precio = min(precios)
print(f"Precio más barato: {menor_precio}")

# Aplicar 10% de descuento
if total > 5000:
    print(f"Total con descuento: {0.9*total}")
else:
    print(f"Total con descuento: {total}")

