"""
Dada una lista de palabras, realizar las siguientes operaciones usando **programación funcional**:

1. Filtrar únicamente las palabras que tengan más de 5 letras.
2. Convertir todas esas palabras a mayúsculas.
3. Obtener la cantidad total de letras que suman todas esas palabras.

Ejemplo de entrada:
```python
palabras = ["python", "java", "javascript", "c", "haskell", "go", "typescript"]
```

Resultado esperado:
```
['PYTHON', 'JAVASCRIPT', 'HASKELL', 'TYPESCRIPT']
Número total de letras: 33
```
"""

# Lista inicial
palabras = ["python", "java", "javascript", "c", "haskell", "go", "typescript"]

# Filtrar palabras con más de 5 letras y convertir a mayúscula
palabras_largas = [x.upper() for x in palabras if len(x) > 5]

# Calcular cantidad total de letras
total = 0
for s in palabras_largas:
    total += len(s)


print(palabras_largas)
print(f"Número total de letras: {total}")
