# Función de menú
def menu():
    print("Bienvenido a la aplicación")
    opcion = input("Ingrese una opción: ")

    lista = [1,2,3,4]

    if opcion == "1": 
        print(f"El número máximo es: {encontrarMaximo(lista)}")
    elif opcion == "2":
        encontrarMinimo(lista)
    elif opcion == "3":
        return -1
    else: 
        print("Ingrese una opción válida.")

    return 1

def encontrarMaximo(lista):
    pass

def encontrarMinimo(lista):
    pass

# Cuerpo del programa (punto de inicio)
continuar = True
while continuar:
    if menu() == -1:
        continuar = False

