# Examen Parcial I

## Indicaciones generales

- El examen tiene una duración total de 2 horas y 15 minutos.
- Subir al Google Classroom las soluciones en el espacio denominado _Examen Parcial I_.
- Entregue un documento para cada ejercicio: `ejercicio1.py` y `ejercicio2.py`.
- Esta es una prueba de carácter individual y está prohibido el acceso a información en internet.
- Los estudiantes pueden llevar una hoja como formulario escrita a mano.

---

## Ejercicio 1: Control de acceso a una zona restringida

### Descripción

Un laboratorio escolar desea automatizar el control de acceso a una zona restringida.
Sólo se permite el ingreso a estudiantes con edades entre **15 y 18 años inclusive**.
Se debe registrar la información de varias personas y procesarla para determinar quiénes pueden ingresar y quiénes no.

### Requerimientos

1. Solicitar al usuario cuántas personas se van a registrar.
2. Por cada persona, solicitar el **nombre** y la **edad**.
3. Al finalizar, mostrar:
   - Una lista con los nombres de las personas permitidas (edades entre 15 y 18 inclusive).
   - La cantidad de personas **menores de 15 años rechazadas**.
   - La cantidad de personas **mayores de 18 años rechazadas**.
   - El nombre de la **persona permitida con mayor edad**.
4. Se recomienda clasificar cada uno de los grupos (menores, mayores y permitidos) en listas separadas.
5. Documentar el programa con comentarios descriptivos.

!!! info "Aclaración"

      Para este ejercicio no es necesario realizar la validación de las entradas numéricas del usuario, se supone que son entradas válidas.

### Criterios de Evaluación

| Criterio                                                                | Puntaje    |
| ----------------------------------------------------------------------- | ---------- |
| Lectura de la cantidad total de personas                                | 2.5 pts    |
| Solicitud y almacenamiento correcto de nombre y edad en listas          | 7.5 pts    |
| Filtrado correcto de personas dentro del rango permitido (15 a 18 años) | 5 pts      |
| Impresión clara de los nombres permitidos                               | 5 pts      |
| Conteo correcto de personas menores de 15                               | 5 pts      |
| Conteo correcto de personas mayores de 18                               | 5 pts      |
| Identificación de la persona permitida con mayor edad                   | 15 pts     |
| Documentación clara mediante comentarios                                | 5 pts      |
| **Total**                                                               | **60 pts** |

---

### Ejemplo esperado de ejecución

```
Cantidad de personas para el registro: 4
Nombre de la persona 1: Ana
Edad: 17
Nombre de la persona 2: Pablo
Edad: 19
Nombre de la persona 3: Carla
Edad: 14
Nombre de la persona 4: Luis
Edad: 18

Personas permitidas: ['Ana', 'Luis']
Rechazados menores de edad: 1
Rechazados mayores de edad: 1
Persona permitida con mayor edad: Luis
```

---

## Ejercicio 2: Juego de palabras ocultas en una frase

### Descripción

Un estudiante recibe una frase con palabras ocultas.
El objetivo es procesar esa frase para encontrar ciertos patrones y trabajar con cada palabra de forma individual.
Además, se quiere formar una palabra oculta tomando la **última letra de cada palabra**.

### Requerimientos

1. Solicitar al usuario que ingrese una frase (suponga que únicamente hay espacios entre las palabras).
2. Procesar la frase para:
   - Contar cuántas palabras **terminan con la letra `a`**.
   - Mostrar cuál es la **palabra más larga** junto con su longitud.
   - Construir y mostrar la **palabra oculta** formada por la última letra de cada palabra.
   - **Extra:** Indicar cuántas palabras tienen exactamente **5 letras**.
   - **Extra:** Crear y mostrar una nueva lista con todas las **palabras invertidas**.
3. Documentar correctamente el programa.

!!! info "Pistas sobre para el ejercicio"

      - Recorrer todas las palabras de la lista y guardar la información en variables fuera del loop.
      - Forme un string inicialmente vacío y vaya concatenando los caracteres extraídos de cada palabra.

### Criterios de Evaluación

| Criterio                                                | Puntaje      |
| ------------------------------------------------------- | ------------ |
| Lectura de la frase original                            | 2.5 pts      |
| División de la frase en palabras                        | 2.5 pts      |
| Conteo correcto de palabras que terminan con `a`        | 10 pts       |
| Cálculo de longitud y detección de la palabra más larga | 10 pts       |
| Palabra oculta generada a partir de las últimas letras  | 10 pts       |
| Comentarios claros en el código                         | 5 pts        |
| **Extra:** Lista con las palabras invertidas            | 5 pts        |
| **Extra:** Conteo de palabras con exactamente 5 letras  | 7.5 pts      |
| **Total**                                               | **52.5 pts** |

### Ejemplo esperado de ejecución

```
Ingrese una frase: hola mundo casa roja

Palabras que terminan con 'a': 3
Palabra mas larga: mundo
Palabra oculta: aaoa
Palabras con exactamente 5 letras: 1
Palabras invertidas: ['aloh', 'odnum', 'asac', 'ajor']
```
