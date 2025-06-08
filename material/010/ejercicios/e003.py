"""
Generador de correos institucionales

Cree una función que reciba una lista de nombres completos y devuelva una lista de correos en el formato `inicial_nombre.apellido@ccp.ed.cr`.

**Ejemplo:**
```python
Entrada: ["Ana Gómez", "Luis Fernández"]
Salida: ["a.gomez@ccp.ed.cr", "l.fernandez@ccp.ed.cr"]
```
"""

def generador_correos(lista_nombres):
    lista_correos = []

    for nombre_completo in lista_nombres:
        # Separar nombre completo en nombre y apellido
        nombre, apellido = nombre_completo.split()

        # Convertir nombre y apellido a minúscula
        nombre = nombre.lower()
        apellido = apellido.lower()

        # Obtener la letra inicial del nombre
        letra_inicial = nombre[0]

        # Formar el correo con un f-string
        correo = f"{letra_inicial}.{apellido}@ccp.ed.cr"

        # Agregar correo a la lista de correos
        lista_correos.append(correo)

    return lista_correos

print(generador_correos(["Ana Gomez", "Luis Fernandez"]))
