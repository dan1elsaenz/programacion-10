"""
Conversor de tiempo a segundos

Cree una función que reciba una cadena en el formato `hh:mm:ss` y devuelva la cantidad total de segundos.

**Ejemplo:**
```python
Entrada: "01:45:30"
Salida: 6330
```
"""

# tiempo: `hh:mm:ss`
def conversor_tiempo(tiempo):

    lista = tiempo.split(":") # ["hh", "mm", "ss"]

    segundos_totales = 3600 * int(lista[0]) + 60 * int(lista[1]) + int(lista[2])

    return segundos_totales


segundos_tiempo1 = conversor_tiempo("01:45:30") # 6330
print(conversor_tiempo("02:52:19")) # 10339

