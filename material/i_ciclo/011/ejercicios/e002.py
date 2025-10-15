"""
2. Invertir una cadena

Cree una función recursiva que reciba un string y lo retorne invertido.

```python
Entrada: "python"
Salida: "nohtyp"
```
"""

# Implementación sin recursión
def invertir(string):
    return string[::-1]

# Implementación con recursión
def invertir_recursivo(string):
    # Caso base: Que el string esté vacío
    if len(string) <= 1:
        return string
    # Recursión
    return string[-1] + invertir_recursivo(string[:-1])

print(invertir("python"))
print(invertir_recursivo("python"))

