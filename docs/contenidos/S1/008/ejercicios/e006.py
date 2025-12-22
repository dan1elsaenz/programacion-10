"""
Sistema de inventario con lógica:

Implementa un sistema de inventario donde cada producto tiene precio, cantidad y categoría.
Permite consultar productos por categoría y calcular el valor total del inventario
"""

# Declaración de diccionario de productos
productos = {
    "Té frío" : { "precio": 1000, "cantidad": 10, "categoria": "Bebidas" },
    "Té blanco" : { "precio": 1000, "cantidad": 10, "categoria": "Bebidas" },
    "Fideos" : { "precio": 2000, "cantidad": 20, "categoria":"Pastas", }, 
    "Cloro" : { "precio": 2500, "cantidad": 5, "categoria":"Limpieza", }, 
}

continuar = True

while continuar:
    print("""
    1. Consultar producto por categoría
    2. Calcular el valor total del inventario
    3. Salir
    """)
    opcion = input("Ingrese una de las opciones anteriores: ")


    if opcion == "1":
        categoria = input("Ingrese la categoría que quiere consultar: ")

        # Recorrer diccionario
        for clave, valor in productos.items():
            # Si la categoría ingresada por el usuario es igual a la categoría del producto sobre el que se está iterando
            # se imprime su información
            if valor["categoria"] == categoria:
                print(f'{clave}  |  precio: {valor["precio"]}  |  cantidad: {valor["cantidad"]}')

    elif opcion == "2":
        valor_total = 0

        # Recorrer el diccionario
        for elemento in productos.values():
            # Multiplicar cantidad por precio de cada producto
            valor_total += elemento["precio"] * elemento["cantidad"]

        print(f"El valor total de los productos en inventario es: {valor_total}")

    elif opcion == "3": 
        continuar = False
        print("Saliendo...")

    else: 
        print("Opción inválida. Intente nuevamente.")

