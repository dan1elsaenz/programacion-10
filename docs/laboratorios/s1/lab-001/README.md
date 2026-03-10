---
icon: material/account-check
---

# :material-account-check: Laboratorio 1

Desarrolle un programa que simule un sistema de registro para un evento estudiantil.

Se desea construir un programa que cumpla con lo siguiente:

1. Solicite el nombre de la persona.
2. Solicite la edad.
3. Solicite si posee permiso especial (responder `si` o `no`).
4. Determine si puede ingresar al evento.
5. Muestre un mensaje final personalizado.

## Reglas del sistema

Una persona puede ingresar si:

- Tiene 18 años o más.
- O tiene permiso especial.

Además:

- El nombre no puede estar vacío.
- La edad debe ser un número válido.
- La edad no puede ser negativa.
- La respuesta de permiso debe analizarse sin importar mayúsculas o espacios.

## Requisitos técnicos

- Utilizar `input()` para recibir datos.
- Convertir correctamente la edad a entero.
- Utilizar al menos una estructura `if-elif-else`.
- Utilizar métodos para validar texto.
- Mostrar el mensaje final usando `f-strings`.
- Manejar un posible `ValueError` si la edad no es numérica.

## Casos de ejemplo

!!! example "Casos de ejecución"

    === "Caso válido 1"

        ```
        Nombre: Ana
        Edad: 20
        Permiso: no

        Bienvenido/a Ana.
        Puede ingresar al evento.
        ```

    === "Caso válido 2"

        ```
        Nombre: Luis
        Edad: 16
        Permiso: si

        Bienvenido/a Luis.
        Puede ingresar al evento.
        ```

    === "Caso no válido"

        ```
        Nombre: Carla
        Edad: 15
        Permiso: no

        Lo sentimos Carla.
        No puede ingresar al evento.
        ```

    === "Caso con error"

        ```
        Nombre: Pedro
        Edad: abc

        Error: la edad debe ser un número válido.
        ```

## Rúbrica de evaluación

### 1. Entrada de datos (15 puntos)

#### Nombre (5 pts)

- 5 pts: Usa `input()` y almacena correctamente el nombre.
- 3 pts: Lo solicita pero lo usa mal.
- 0 pts: No lo solicita.

#### Edad (5 pts)

- 5 pts: Usa `input()` y lo convierte correctamente con `int()`.
- 3 pts: Lo solicita pero no convierte correctamente.
- 0 pts: No lo solicita.

#### Permiso (5 pts)

- 5 pts: Solicita correctamente el permiso.
- 3 pts: Lo solicita pero no lo usa bien.
- 0 pts: No lo solicita.

### 2. Manejo de errores (15 puntos)

#### Uso de `try-except` (10 pts)

- 10 pts: Captura correctamente `ValueError`.
- 5 pts: Uso incompleto o incorrecto.
- 0 pts: No maneja errores.

#### Mensaje de error claro (5 pts)

- 5 pts: Mensaje comprensible.
- 3 pts: Mensaje poco claro.
- 0 pts: No informa error.

### 3. Validación de datos (15 puntos)

#### Nombre no vacío (5 pts)

- 5 pts: Verifica correctamente.
- 3 pts: Intento parcial.
- 0 pts: No verifica.

#### Edad no negativa (5 pts)

- 5 pts: Verifica correctamente.
- 3 pts: Intento parcial.
- 0 pts: No valida.

#### Normalización del permiso (5 pts)

- 5 pts: Usa correctamente `strip()` y `lower()`.
- 3 pts: Uso parcial.
- 0 pts: No normaliza.

### 4. Uso de estructuras condicionales (25 puntos)

#### Uso correcto de `if-elif-else` (20 pts)

- 20 pts: Correctamente implementado.
- 10 pts: Incompleto.
- 0 pts: Incorrecto.

#### Lógica correcta (5 pts)

- 5 pts: Cumple completamente las reglas.
- 3 pts: Parcial.
- 0 pts: Incorrecta.

### 5. Uso de strings (10 puntos)

#### Uso de `f-strings` (10 pts)

- 10 pts: Mensaje final usa correctamente `f""`.
- 5 pts: Usa concatenación en lugar de `f-string`.
- 0 pts: No personaliza el mensaje.

### 6. Salida del programa (10 puntos)

#### Mensaje personalizado (5 pts)

- 5 pts: Incluye correctamente el nombre.
- 3 pts: Parcial.
- 0 pts: No lo incluye.

#### Claridad del mensaje (5 pts)

- 5 pts: Resultado correcto según el caso.
- 3 pts: Parcial.
- 0 pts: Incorrecto.

### 7. Calidad del código (10 puntos)

#### Indentación correcta (5 pts)

- 5 pts: Consistente.
- 3 pts: Errores menores.
- 0 pts: Incorrecta.

#### Claridad y orden (5 pts)

- 5 pts: Código limpio y organizado.
- 3 pts: Algo desordenado.
- 0 pts: Difícil de leer.

## Solución

```python title="solucion.py"
nombre = input("Nombre: ").strip()

if nombre == "":
    print("Error: el nombre no puede estar vacío.")
else:
    try:
        edad = int(input("Edad: "))

        if edad < 0:
            print("Error: la edad no puede ser negativa.")
        else:
            permiso = input("Permiso: ").strip().lower()

            if edad >= 18 or permiso == "si":
                print(f"Bienvenido/a {nombre}.")
                print("Puede ingresar al evento.")
            else:
                print(f"Lo sentimos {nombre}.")
                print("No puede ingresar al evento.")

    except ValueError:
        print("Error: la edad debe ser un número válido.")
```
