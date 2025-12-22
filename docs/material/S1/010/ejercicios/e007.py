"""
Validación de expresiones con paréntesis

Cree una función que reciba un string con paréntesis y determine si están correctamente balanceados.

**Ejemplo:**
```python
Entrada: "(a + b) * (c - d)"
Salida: True

Entrada: "(a + b * (c - d)) )"
Salida: False
```
"""

def validarParentesis(entrada):

    # Variable booleana de salida
    seCumple = True

    # Pila: Los elementos entran y salen por el final
    pila = []

    # Recorrer el string de entrada
    for caracter in entrada:

        if caracter in ("(", "[", "{"):
            pila.append(caracter)
        elif caracter in (")", "]", "}") and len(pila) == 0:
            seCumple = False
            break
        elif caracter == ")" and pila[-1] == "(":
            pila.pop()
        elif caracter == ")" and pila[-1] != "(":
            seCumple = False
            break
        elif caracter == "]" and pila[-1] == "[":
            pila.pop()
        elif caracter == "]" and pila[-1] != "[":
            seCumple = False
            break
        elif caracter == "}" and pila[-1] == "{":
            pila.pop()
        elif caracter == "}" and pila[-1] != "{":
            seCumple = False
            break

    if len(pila) > 0:
        seCumple = False

    return seCumple

print(validarParentesis("(a + b) * (c - d)"))
print(validarParentesis("(a + b * (c - d)) )"))

