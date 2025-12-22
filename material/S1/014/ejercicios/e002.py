"""
Validación de entrada numérica positiva del usuario
Utilizando `try-except`
"""

def validar_numero():
    continuar = True

    while continuar:
        try:
            # Solicitar número
            numero = int(input("Ingrese un número entero positivo: "))

            # Verificar que si el número es negativo, lanzo un ValueError que es manejado por el except
            if numero < 0:
                raise ValueError

            return numero
        except ValueError:
            print("Ingrese una entrada numérica positiva.")


