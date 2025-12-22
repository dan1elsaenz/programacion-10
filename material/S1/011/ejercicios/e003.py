"""
3. Calcular potencia de un número

Escriba una función recursiva que calcule `base^exponente`, sin usar `**`.

```
Entrada: base=2, exponente=3
Salida: 8
```
"""

def potencia(base, exponente):
    # Case base
    if exponente == 0:
        return 1
    # Recursión
    return base * potencia(base, exponente-1)

print(potencia(2,3))

