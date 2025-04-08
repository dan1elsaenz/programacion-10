# Clase 7: Ejercicios de repaso

En esta clase, se realizan 3 ejercicios como repaso para el primer examen parcial del curso.

## Ejercicio 1: Evaluación de Rendimiento Académico

Solicita al usuario ingresar los nombres y notas de varios estudiantes.
Luego muestra:

- Lista de estudiantes con su nota
- Promedio general del grupo
- Cuántos estudiantes aprobaron (nota >= 70)
- Cuál fue el mejor y el peor estudiante

**Requisitos:**

- Usar dos listas: una para nombres y otra para notas
- Usar `zip()` para emparejar nombre y nota al mostrar resultados

**Ejemplo esperado de ejecución:**
```
¿Cuántos estudiantes desea registrar?: 3
Nombre del estudiante 1: Ana
Nota del estudiante 1: 80
Nombre del estudiante 2: Luis
Nota del estudiante 2: 65
Nombre del estudiante 3: Marta
Nota del estudiante 3: 92

Notas ingresadas:
Ana - 80
Luis - 65
Marta - 92
Promedio: 79.0
Aprobados: 2
Mejor estudiante: Marta (92)
Peor estudiante: Luis (65)
```

---

## Ejercicio 2: Clasificador de Palabras

Solicita al usuario una lista de palabras (separadas por coma).
Luego:

- Crea una lista con palabras que empiezan con vocal
- Otra con palabras que empiezan con consonante
- Muestra la cantidad de palabras en cada categoría y sus listas respectivas

**Ejemplo esperado de ejecución:**
```
Ingrese una lista de palabras separadas por coma: árbol, sol, elefante, casa, iglú, nube

Palabras que empiezan con vocal: ['árbol', 'elefante', 'iglú']
Cantidad con vocal: 3
Palabras que empiezan con consonante: ['sol', 'casa', 'nube']
Cantidad con consonante: 3
```

---

## Ejercicio 3: Análisis de Precios
Pide al usuario que ingrese una lista de precios de productos. Luego:

- Calcula el total de la compra
- Muestra cuántos productos son mayores a 1000 colones
- Muestra el precio más caro y más barato
- Aplica un 10% de descuento si el total supera los 5000 colones

**Requisitos:**

- Validar que los precios sean positivos
- Usar listas y funciones como `sum()`, `max()`, `min()`

**Ejemplo esperado de ejecución:**
```
Ingrese los precios de los productos separados por coma: 1200, 300, 5200, 1500

Total antes de descuento: 8200
Productos mayores a 1000 colones: 3
Precio más caro: 5200
Precio más barato: 300
Total con descuento:

