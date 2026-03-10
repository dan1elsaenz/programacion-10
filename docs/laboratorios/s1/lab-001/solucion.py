nombre = input("Nombre: ").strip()

if nombre == "":
    print("Error: el nombre no puede estar vacío.")
else:
    try:
        edad = int(input("Edad: "))

        if edad < 0:
            print("Error: la edad no puede ser negativa.")
        else:
            permiso = input("Permiso: ").strip().lower()

            if edad >= 18 or permiso == "si":
                print(f"Bienvenido/a {nombre}.")
                print("Puede ingresar al evento.")
            else:
                print(f"Lo sentimos {nombre}.")
                print("No puede ingresar al evento.")

    except ValueError:
        print("Error: la edad debe ser un número válido.")
