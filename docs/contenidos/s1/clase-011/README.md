---
icon: material/dumbbell
---

# :material-dumbbell: Clase 11

En esta clase, se plantean algunos ejercicios de práctica para refrescar conceptos vistos anteriormente.

## Recursión

!!! tip "Patrón para diseñar funciones recursivas"

    Toda función recursiva tiene dos partes:

    1. **Caso base**: condición que detiene la recursión y retorna un valor directamente.
    2. **Caso recursivo**: llamada a la misma función con un problema más pequeño.

    Si no hay caso base, la función se llama a sí misma infinitamente hasta causar un error.

### 1. Torres de Hanói

=== "Enunciado"

    El puzzle de las Torres de Hanói consiste en mover N discos desde la torre **A** hacia la torre **C**, usando la torre **B** como auxiliar.
    Las reglas son:

    1. Solo se puede mover un disco a la vez.
    2. Un disco más grande nunca puede colocarse sobre uno más pequeño.

    Escriba una función `hanoi(n, origen, destino, auxiliar)` que imprima la secuencia de movimientos necesarios para resolver el puzzle con `n` discos.

    ```
    Mover disco de A a C
    Mover disco de A a B
    Mover disco de C a B
    Mover disco de A a C
    Mover disco de B a A
    Mover disco de B a C
    Mover disco de A a C
    ```

=== "Solución"

    ```python
    def hanoi(n, origen, destino, auxiliar):
        if n == 1:                                          # (1)!
            print(f"Mover disco de {origen} a {destino}")
            return
        hanoi(n - 1, origen, auxiliar, destino)            # (2)!
        print(f"Mover disco de {origen} a {destino}")      # (3)!
        hanoi(n - 1, auxiliar, destino, origen)            # (4)!

    n = int(input("Número de discos: "))
    hanoi(n, "A", "C", "B")
    ```

    1. Caso base: con un solo disco, el movimiento es directo.
    2. Mueve los n-1 discos superiores de origen a auxiliar (usando destino como apoyo).
    3. Mueve el disco más grande directamente a su destino.
    4. Mueve los n-1 discos desde auxiliar hasta destino (usando origen como apoyo).

    !!! example "Ejemplos de ejecución"

        === "2 discos"
            ```
            Número de discos: 2
            Mover disco de A a B
            Mover disco de A a C
            Mover disco de B a C
            ```
        === "3 discos"
            ```
            Número de discos: 3
            Mover disco de A a C
            Mover disco de A a B
            Mover disco de C a B
            Mover disco de A a C
            Mover disco de B a A
            Mover disco de B a C
            Mover disco de A a C
            ```

---

### 2. Decimal a binario

=== "Enunciado"

    Escriba una función recursiva `a_binario(n)` que convierta un entero positivo a su representación binaria y la retorne como string.

    - `a_binario(1)` → `"1"`
    - `a_binario(5)` → `"101"`
    - `a_binario(42)` → `"101010"`

    **Restricción:** no usar `bin()`, `format()` ni ninguna función de conversión incorporada.

=== "Solución"

    ```python
    def a_binario(n):
        if n == 0:                                  # (1)!
            return "0"
        if n == 1:                                  # (2)!
            return "1"
        return a_binario(n // 2) + str(n % 2)      # (3)!

    n = int(input("Ingrese un entero positivo: "))
    print(f"{n} en binario es: {a_binario(n)}")
    ```

    1. Caso base especial: el cero en binario es `"0"`.
    2. Caso base: el uno en binario es `"1"`.
    3. Caso recursivo: el bit menos significativo es `n % 2`; los bits anteriores son la conversión de `n // 2`.

    !!! example "Ejemplos de ejecución"

        === "n = 8"
            ```
            Ingrese un entero positivo: 8
            8 en binario es: 1000
            ```
        === "n = 13"
            ```
            Ingrese un entero positivo: 13
            13 en binario es: 1101
            ```

---

### 3. ¿La lista está ordenada?

=== "Enunciado"

    Escriba una función recursiva `esta_ordenada(lista)` que verifique si una lista de enteros está en orden ascendente (de menor a mayor).

    - `esta_ordenada([1, 3, 5, 9])` → `True`
    - `esta_ordenada([1, 3, 2, 9])` → `False`
    - `esta_ordenada([7])` → `True`

    **Restricción:** no usar ciclos ni la función `sorted()`.

=== "Solución"

    ```python
    def esta_ordenada(lista):
        if len(lista) <= 1:                                         # (1)!
            return True
        if lista[0] > lista[1]:                                     # (2)!
            return False
        return esta_ordenada(lista[1:])                             # (3)!

    numeros = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
    if esta_ordenada(numeros):
        print("La lista está ordenada.")
    else:
        print("La lista NO está ordenada.")
    ```

    1. Caso base: listas de 0 o 1 elemento siempre están ordenadas.
    2. Si el primer elemento es mayor que el segundo, ya no puede estar ordenada.
    3. Caso recursivo: verificar el resto de la lista (desde el segundo elemento en adelante).

    !!! example "Ejemplos de ejecución"

        === "Ordenada"
            ```
            Ingrese números separados por espacio: 2 5 8 11 15
            La lista está ordenada.
            ```
        === "Desordenada"
            ```
            Ingrese números separados por espacio: 3 7 4 10
            La lista NO está ordenada.
            ```

---

### 4. Secuencia de Collatz

=== "Enunciado"

    La conjetura de Collatz dice que cualquier entero positivo eventualmente llega a 1 si se aplica repetidamente esta regla:

    - Si `n` es **par** → `n / 2`
    - Si `n` es **impar** → `3 * n + 1`

    Escriba una función recursiva `collatz(n)` que retorne la cantidad de pasos que tarda en llegar a 1.

    - `collatz(1)` → `0`
    - `collatz(6)` → `8`  (6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1)

=== "Solución"

    ```python
    def collatz(n):
        if n == 1:                          # (1)!
            return 0
        if n % 2 == 0:                      # (2)!
            return 1 + collatz(n // 2)
        return 1 + collatz(3 * n + 1)       # (3)!

    n = int(input("Ingrese un entero positivo: "))
    print(f"Pasos para llegar a 1 desde {n}: {collatz(n)}")
    ```

    1. Caso base: ya llegamos a 1, no se necesitan más pasos.
    2. Si es par, dividir entre 2 y sumar 1 paso.
    3. Si es impar, aplicar `3n + 1` y sumar 1 paso.

    !!! example "Ejemplos de ejecución"

        === "n = 6"
            ```
            Ingrese un entero positivo: 6
            Pasos para llegar a 1 desde 6: 8
            ```
        === "n = 27"
            ```
            Ingrese un entero positivo: 27
            Pasos para llegar a 1 desde 27: 111
            ```

---

## Strings, listas y diccionarios

!!! tip "Herramientas para estos ejercicios"

    - `ord(c)` retorna el código numérico de un carácter; `chr(n)` hace lo contrario.
    - Un diccionario puede usarse como tabla de búsqueda para evitar cadenas largas de `if-elif`.
    - Una lista puede comportarse como una **pila** (stack): `append()` empuja, `pop()` saca el último.

### 5. Cifrado César

=== "Enunciado"

    El cifrado César desplaza cada letra del alfabeto k posiciones.
    Con k = 3: `a` → `d`, `b` → `e`, … `z` → `c` (la rotación es circular).

    Escriba dos funciones: `cifrar(mensaje, k)` y `descifrar(mensaje, k)`.
    Ambas deben respetar mayúsculas y minúsculas, y dejar sin cambio cualquier carácter que no sea letra (espacios, signos, dígitos).

    - `cifrar("Hola Mundo", 3)` → `"Krod Pxqgr"`
    - `descifrar("Krod Pxqgr", 3)` → `"Hola Mundo"`

=== "Solución"

    ```python
    def desplazar(caracter, k):
        if caracter.islower():
            return chr((ord(caracter) - ord('a') + k) % 26 + ord('a'))  # (1)!
        if caracter.isupper():
            return chr((ord(caracter) - ord('A') + k) % 26 + ord('A'))  # (2)!
        return caracter                                                   # (3)!

    def cifrar(mensaje, k):
        resultado = ""
        for c in mensaje:
            resultado += desplazar(c, k)
        return resultado

    def descifrar(mensaje, k):
        return cifrar(mensaje, -k)                                       # (4)!

    mensaje = input("Mensaje: ")
    k = int(input("Desplazamiento: "))
    cifrado = cifrar(mensaje, k)
    print(f"Cifrado:    {cifrado}")
    print(f"Descifrado: {descifrar(cifrado, k)}")
    ```

    1. Para minúsculas: normaliza al rango 0 a 25, aplica el desplazamiento con módulo, vuelve al código ASCII.
    2. El mismo proceso para mayúsculas, usando `ord('A')` como base.
    3. Si no es letra, se devuelve sin cambios.
    4. Descifrar es cifrar con desplazamiento negativo.

    !!! example "Ejemplos de ejecución"

        === "k = 3"
            ```
            Mensaje: Hola Mundo
            Desplazamiento: 3
            Cifrado:    Krod Pxqgr
            Descifrado: Hola Mundo
            ```
        === "k = 13 (ROT13)"
            ```
            Mensaje: Python
            Desplazamiento: 13
            Cifrado:    Clguba
            Descifrado: Python
            ```

---

### 6. Histograma de caracteres

=== "Enunciado"

    Dado un texto, contar la frecuencia de cada letra que aparezca (sin distinguir mayúsculas, ignorar espacios, signos y dígitos).
    Luego mostrar un histograma donde cada fila tiene el formato:

    ```
    a | ****
    e | **
    o | *
    ```

    El histograma debe estar ordenado por frecuencia de mayor a menor.

=== "Solución"

    ```python
    def contar_letras(texto):
        frecuencia = {}
        for c in texto.lower():
            if c.isalpha():                                 # (1)!
                frecuencia[c] = frecuencia.get(c, 0) + 1
        return frecuencia

    def mostrar_histograma(frecuencia):
        # Ordenar de mayor a menor frecuencia
        ordenado = sorted(frecuencia.items(), key=lambda par: par[1], reverse=True)
        for letra, cantidad in ordenado:
            print(f"{letra} | {'*' * cantidad}")

    texto = input("Ingrese un texto: ")
    frecuencia = contar_letras(texto)
    mostrar_histograma(frecuencia)
    ```

    1. `isalpha()` retorna `True` solo si el carácter es una letra, descartando espacios, signos y dígitos.

    !!! example "Ejemplos de ejecución"

        === "Frase corta"
            ```
            Ingrese un texto: hola mundo
            o | ***
            l | **
            h | *
            a | *
            m | *
            u | *
            n | *
            d | *
            ```
        === "Texto más largo"
            ```
            Ingrese un texto: la programacion es divertida
            a | *****
            i | ***
            o | ***
            r | ***
            e | **
            g | **
            m | **
            c | *
            l | *
            p | *
            s | *
            d | *
            v | *
            t | *
            n | *
            ```

---

### 7. Tabla de posiciones de torneo

=== "Enunciado"

    Se tienen N equipos numerados del 0 al N-1.
    Los resultados entre ellos se almacenan en una matriz NxN, donde `M[i][j]` indica el resultado del equipo `i` contra el equipo `j`:

    - `1` → victoria del equipo `i`
    - `0` → empate
    - `-1` → derrota del equipo `i`

    La diagonal (`M[i][i]`) no aplica (un equipo no juega contra sí mismo).

    Dado una lista de nombres de equipos y la matriz de resultados, calcular los puntos de cada equipo (victoria = 3, empate = 1, derrota = 0) y mostrar la tabla ordenada de mayor a menor.

=== "Solución"

    ```python
    def calcular_puntos(matriz, i):
        puntos = 0
        for j in range(len(matriz)):
            if i == j:                  # (1)!
                continue
            if matriz[i][j] == 1:
                puntos += 3
            elif matriz[i][j] == 0:
                puntos += 1
        return puntos

    def mostrar_tabla(equipos, matriz):
        resultados = []
        for i in range(len(equipos)):
            pts = calcular_puntos(matriz, i)
            resultados.append((equipos[i], pts))

        resultados.sort(key=lambda par: par[1], reverse=True)

        print(f"\n{'Equipo':<15} {'Puntos':>6}")
        print("-" * 22)
        for nombre, pts in resultados:
            print(f"{nombre:<15} {pts:>6}")

    equipos = ["Tigres", "Halcones", "Lobos", "Águilas"]

    # Resultados: fila i vs columna j (1=gana i, 0=empate, -1=pierde i)
    matriz = [
        [ 0,  1,  1, -1],   # Tigres
        [-1,  0,  0,  1],   # Halcones
        [-1,  0,  0,  1],   # Lobos
        [ 1, -1, -1,  0],   # Águilas
    ]

    mostrar_tabla(equipos, matriz)
    ```

    1. Se salta la diagonal porque un equipo no juega contra sí mismo.

    !!! example "Ejemplo de ejecución"

        ```
        Equipo          Puntos
        ----------------------
        Tigres               6
        Halcones             4
        Lobos                4
        Águilas              3
        ```

## Ejercicio integrador

### Campeonato relámpago

#### Enunciado

Desarrolle un programa que administre los resultados de un campeonato de fútbol de salón.

El programa funciona con un menú principal y mantiene las estadísticas de cada equipo en un diccionario.

**Datos de cada equipo:**

| Campo | Descripción                              |
| ----- | ---------------------------------------- |
| `PJ`  | Partidos jugados                         |
| `PG`  | Partidos ganados                         |
| `PE`  | Partidos empatados                       |
| `PP`  | Partidos perdidos                        |
| `GF`  | Goles a favor                            |
| `GC`  | Goles en contra                          |
| `Pts` | Puntos (victoria=3, empate=1, derrota=0) |

**Menú principal:**

```
=== CAMPEONATO RELÁMPAGO ===
1. Registrar equipo
2. Ingresar resultado de partido
3. Ver tabla de posiciones
4. Ver equipo con más goles a favor
5. Salir
```

**Requisitos:**

1. La opción 1 registra un nuevo equipo con todas las estadísticas en cero. No se puede registrar el mismo nombre dos veces.
2. La opción 2 pide los nombres de los dos equipos y el marcador (ej. `2-1`). Actualiza las estadísticas de ambos equipos. Si algún equipo no existe, mostrar un error.
3. La opción 3 muestra todos los equipos ordenados por puntos de mayor a menor. En caso de empate de puntos, ordena por diferencia de goles (GF - GC).
4. La opción 4 muestra el equipo con mayor cantidad de goles a favor.
5. Validar el marcador con `try-except` para manejar formatos incorrectos.

#### Solución

```python
def crear_equipo():
    return {"PJ": 0, "PG": 0, "PE": 0, "PP": 0, "GF": 0, "GC": 0, "Pts": 0}

def registrar_equipo(campeonato):
    nombre = input("Nombre del equipo: ").strip()
    if nombre in campeonato:
        print(f"El equipo '{nombre}' ya está registrado.")
        return
    campeonato[nombre] = crear_equipo()
    print(f"Equipo '{nombre}' registrado.")

def actualizar_stats(campeonato, equipo, gf, gc):
    campeonato[equipo]["PJ"] += 1
    campeonato[equipo]["GF"] += gf
    campeonato[equipo]["GC"] += gc
    if gf > gc:
        campeonato[equipo]["PG"] += 1
        campeonato[equipo]["Pts"] += 3
    elif gf == gc:
        campeonato[equipo]["PE"] += 1
        campeonato[equipo]["Pts"] += 1
    else:
        campeonato[equipo]["PP"] += 1

def ingresar_resultado(campeonato):
    local = input("Equipo local: ").strip()
    visitante = input("Equipo visitante: ").strip()

    if local not in campeonato or visitante not in campeonato:
        print("Uno o ambos equipos no están registrados.")
        return

    try:
        marcador = input("Marcador (ej. 2-1): ")
        goles = marcador.split("-")
        gl = int(goles[0])
        gv = int(goles[1])
    except (ValueError, IndexError):
        print("Formato de marcador inválido. Use el formato: 2-1")
        return

    actualizar_stats(campeonato, local, gl, gv)
    actualizar_stats(campeonato, visitante, gv, gl)
    print("Resultado registrado.")

def ver_tabla(campeonato):
    if not campeonato:
        print("No hay equipos registrados.")
        return

    equipos = list(campeonato.items())
    equipos.sort(key=lambda e: (e[1]["Pts"], e[1]["GF"] - e[1]["GC"]), reverse=True)

    print(f"\n{'Equipo':<15} {'PJ':>3} {'PG':>3} {'PE':>3} {'PP':>3} {'GF':>3} {'GC':>3} {'Pts':>4}")
    print("-" * 46)
    for nombre, s in equipos:
        print(f"{nombre:<15} {s['PJ']:>3} {s['PG']:>3} {s['PE']:>3} {s['PP']:>3} {s['GF']:>3} {s['GC']:>3} {s['Pts']:>4}")

def ver_goleador(campeonato):
    if not campeonato:
        print("No hay equipos registrados.")
        return
    mejor = max(campeonato, key=lambda e: campeonato[e]["GF"])
    print(f"Equipo con más goles a favor: {mejor} ({campeonato[mejor]['GF']} goles)")

campeonato = {}

while True:
    print("\n=== CAMPEONATO RELÁMPAGO ===")
    print("1. Registrar equipo")
    print("2. Ingresar resultado de partido")
    print("3. Ver tabla de posiciones")
    print("4. Ver equipo con más goles a favor")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar_equipo(campeonato)
    elif opcion == "2":
        ingresar_resultado(campeonato)
    elif opcion == "3":
        ver_tabla(campeonato)
    elif opcion == "4":
        ver_goleador(campeonato)
    elif opcion == "5":
        print("¡Hasta la próxima!")
        break
    else:
        print("Opción inválida.")
```

!!! example "Ejemplo de ejecución"

    === "Registro y resultados"
        ```
        === CAMPEONATO RELÁMPAGO ===
        1. Registrar equipo
        ...
        Opción: 1
        Nombre del equipo: Tigres
        Equipo 'Tigres' registrado.

        Opción: 1
        Nombre del equipo: Halcones
        Equipo 'Halcones' registrado.

        Opción: 2
        Equipo local: Tigres
        Equipo visitante: Halcones
        Marcador (ej. 2-1): 3-1
        Resultado registrado.
        ```
    === "Tabla de posiciones"
        ```
        Opción: 3

        Equipo           PJ  PG  PE  PP  GF  GC  Pts
        ----------------------------------------------
        Tigres            1   1   0   0   3   1    3
        Halcones          1   0   0   1   1   3    0
        ```
    === "Marcador inválido"
        ```
        Opción: 2
        Equipo local: Tigres
        Equipo visitante: Halcones
        Marcador (ej. 2-1): tres a uno
        Formato de marcador inválido. Use el formato: 2-1
        ```
