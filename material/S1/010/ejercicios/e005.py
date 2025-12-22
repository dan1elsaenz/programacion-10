"""
Calcular área de un rectángulo

Cree una función que reciba la base y altura de un rectángulo y retorne su área.
Luego use esa función en un `if` para decir si el área es mayor a 100.

**Ejemplo:**
```python
Entrada: base=10, altura=12
Salida: "Área: 120. Es mayor a 100."
```
"""

def area(base,altura):

    area = base * altura

    salida = f"Área: {area}. "

    if area > 100:
        salida += "Es mayor a 100."
    else:
        salida += "Es menor o igual a 100."

    return salida

