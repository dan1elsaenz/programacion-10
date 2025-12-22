# Tarea 1: Validaciones de Datos y Verificación de Patrón ABBA

## Descripción

Esta tarea consiste en **dos ejercicios independientes** en los que se utilizarán **métodos de strings y la estructura de control `if-elif-else`**.
Ambos ejercicios se centran en la manipulación de texto y la validación de datos.

Recuerde añadir comentarios descriptivos a su solución, así como asignar nombres de variables claros.

---

## Ejercicio 1: Registro de Usuario y Validaciones de Datos

Se requiere un programa en Python que solicite información personal al usuario y valide que cada dato cumpla con ciertas condiciones antes de mostrar un resumen con la información ingresada.

El programa debe solicitar y validar los siguientes datos:

1. **Nombre completo**: Debe contener únicamente letras y espacios.
    - _Sugerencia_: `string.replace(" ", "").isalpha()` se encarga de reemplazar de reemplazar los espacios en un string por caracteres vacíos (similar a quitar los espacios) y luego verifica que el string posea únicamente letras. Esto se realiza porque `isalpha()` no reconoce a los espacios como letras.
2. **Edad**: Debe ser un número entero positivo.
3. **Correo electrónico**: Debe contener el carácter `@`.
    - _Sugerencia_: Busque en el string ingresado si contiene el caracter `@`.
4. **Número de teléfono**: Debe contener solo dígitos y tener al menos 8 caracteres.  
    - _Sugerencia_: Verifique que el string ingresado tenga únicamente dígitos y que su largo sea mayor que 8.
5. **País de residencia**: No puede estar vacío.
    - _Sugerencia_: Verifique que el string al quitarle los espacios alrededor sea distinto de `""` (un string vacío).

Si un dato ingresado es inválido, se debe mostrar un mensaje de error explicando la razón.
Finalmente, si todos los datos son válidos, el programa debe mostrar un resumen con la información ingresada.

### **Ejemplo de Ejecución**

```
Ingrese su nombre completo: Juan Pérez
Ingrese su edad: 25
Ingrese su correo electrónico: juanperez@gmail.com
Ingrese su número de teléfono: 87654321
Ingrese su país de residencia: Costa Rica

Registro exitoso. Información ingresada:
Nombre: Juan Pérez
Edad: 25
Correo: juanperez@gmail.com
Teléfono: 87654321
País: Costa Rica
```

Si el usuario ingresa datos inválidos, el programa debe mostrar un mensaje de error:

```
Ingrese su nombre completo: Juan123
Error: El nombre solo debe contener letras y espacios.

Ingrese su edad: -5
Error: La edad debe ser un número entero positivo.

Ingrese su correo electrónico: juanperezgmail.com
Error: El correo debe contener '@' y un dominio válido.

Ingrese su número de teléfono: 12345
Error: El número de teléfono debe contener al menos 8 dígitos.

No se pudo realizar el registro del usuario.
```

### Criterios de Evaluación
- **Validación de Nombre (10%)**: Se debe comprobar que el nombre solo contenga letras y espacios.
- **Validación de Edad (10%)**: Debe asegurarse que sea un número entero positivo.
- **Validación de Correo Electrónico (10%)**: Se debe verificar que tenga una estructura válida con `@`.
- **Validación de Número de Teléfono (10%)**: Debe contener solo dígitos y al menos 8 caracteres.
- **Presentación del Resumen (10%)**: Si todos los datos son válidos, debe mostrarse un resumen claro con la información ingresada.

---

## **Ejercicio 2: Verificación de un Patrón ABBA**
Escriba un código en Python que valide si un string cumple con la estructura **ABBA** (dos palabras que se repiten en orden reflejado).

### **Requisitos**
- Solicitar al usuario dos palabras distintas.
- Solicitar un string compuesto por esas palabras en **algún orden** (siempre será un string de cuatro palabras, sin necesidad de validación).
- Comparar si las palabras ingresadas siguen el **orden ABBA**.
- Mostrar un mensaje indicando si el string cumple o no con el patrón.

### **Ejemplo de Ejecución**

```
Escriba el string #1: mundo
Escriba el string #2: hola
Escriba un string que contenga las palabras anteriores en algún orden: hola mundo mundo hola
El string SÍ cumple con el orden ABBA.
```

Otro ejemplo:
```
Escriba el string #1: mundo
Escriba el string #2: hola
Escriba un string que contenga las palabras anteriores en algún orden: hola hola mundo mundo
El string NO cumple con el orden ABBA.
```

### **Pistas para la Implementación**
- Utilizar `split()` para dividir el string con las palabras repetidas en una lista de palabras.
- Acceder a los elementos de la lista por sus índices: `palabras[0]`, `palabras[1]`, y así sucesivamente.
- Comparar los valores de la lista para verificar si siguen el orden ABBA.
- Se puede usar `if-elif-else` para realizar la comparación.

### Criterios de Evaluación
- **Recepción de Palabras (10%)**: Se debe solicitar ambas palabras y el string principal.
- **Separación del String (10%)**: Se debe dividir correctamente el string en palabras utilizando `split()`.
- **Verificación de Patrón ABBA (20%)**: Comparar las palabras ingresadas y determinar si siguen el patrón ABBA.
- **Mensaje al Usuario (10%)**: Se deben mostrar mensajes adecuados indicando si el patrón se cumple o no.

## **Entrega**
- El código de cada ejercicio debe estar en **archivos separados** (`ejercicio1.py` y `ejercicio2.py`).
- Subir los archivos `.py` al entorno de **Google Classroom** designado para el curso.

