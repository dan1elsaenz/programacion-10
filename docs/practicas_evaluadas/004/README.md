# Práctica Evaluada 4

## Enunciado

Se solicita implementar una función recursiva en Python que reciba una cadena de texto y devuelva el número total de vocales que contiene.

La función **no debe utilizar estructuras de repetición** como `for` o `while`, ni métodos como `.count()`.

La función debe contar tanto vocales minúsculas como mayúsculas (`a, e, i, o, u, A, E, I, O, U`).

---

## Archivo requerido

Se debe crear un archivo llamado `recursividad.py` con el siguiente contenido base:

```python
def contar_vocales(cadena):
    # Implementación recursiva
    pass

texto = input("Ingrese una cadena: ")
print("Cantidad de vocales:", contar_vocales(texto))
```

---

## Pista

Se recomienda revisar el primer carácter de la cadena y verificar si es una vocal.
En caso afirmativo, se debe sumar uno y llamar nuevamente a la función con el resto de la cadena.
Si no es vocal, simplemente se continúa con la llamada recursiva sin incrementar el contador.

---

## Ejemplos de ejecución

```
Ingrese una cadena: Python es util
Cantidad de vocales: 4
```

---

## Restricciones

- No se permite el uso de ciclos (`for`, `while`).
- No se permite el uso de métodos como `.count()` ni expresiones regulares.
- Se debe utilizar exclusivamente recursión y funciones propias.

---

## Criterios de evaluación

| Criterio                                                   | Puntos |
|------------------------------------------------------------|--------|
| Implementación recursiva funcional de `contar_vocales`     | 50     |
| Manejo correcto de mayúsculas y minúsculas                 | 20     |
| Estructura clara, código indentado                         | 10     |
| Entrada y salida definida               | 10     |
| Documentación y uso de comentarios relevantes              | 10     |
| **Total**                                                  | **100** |
