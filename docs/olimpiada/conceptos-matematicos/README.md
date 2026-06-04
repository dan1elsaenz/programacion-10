---
icon: material/calculator-variant
---

<!-- Colocar formato matemático -->
<script id="MathJax-script" async src="https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
  window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
</script>

# :material-calculator-variant: Conceptos Matemáticos

Esta sección cubre los conceptos matemáticos que aparecen con mayor frecuencia en la OCI.

## Lógica

La **lógica proposicional** estudia proposiciones (afirmaciones que son verdaderas o falsas) y la forma en que se combinan mediante operadores.

### Operadores lógicos

Un **operador lógico** transforma o combina proposiciones. Los más importantes son:

| Símbolo | Nombre       | Descripción                                      |
|---------|--------------|--------------------------------------------------|
| \(\lnot A\) | Negación | Verdadero cuando \(A\) es falso, y viceversa. |
| \(A \land B\) | Conjunción (Y) | Verdadero solo cuando ambas son verdaderas. |
| \(A \lor B\) | Disyunción (O) | Verdadero cuando al menos una es verdadera. |
| \(A \oplus B\) | Disyunción exclusiva (XOR) | Verdadero cuando exactamente una es verdadera. |
| \(A \Rightarrow B\) | Implicación | Falso solo cuando \(A\) es verdadero y \(B\) es falso. |
| \(A \Leftrightarrow B\) | Bicondicional | Verdadero cuando \(A\) y \(B\) tienen el mismo valor. |

La tabla de verdad completa para dos proposiciones \(A\) y \(B\):

| \(A\) | \(B\) | \(\lnot A\) | \(\lnot B\) | \(A \land B\) | \(A \lor B\) | \(A \Rightarrow B\) | \(A \Leftrightarrow B\) |
|-------|-------|------------|------------|--------------|-------------|-------------------|----------------------|
| 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |

!!! note "La implicación y su falsedad"
    \(A \Rightarrow B\) es falso **únicamente** cuando la premisa \(A\) es verdadera y la conclusión \(B\) es falsa. En todos los demás casos (incluyendo \(A\) falso) la implicación es verdadera.

### Leyes de De Morgan

Las leyes de De Morgan permiten distribuir la negación sobre una conjunción o disyunción:

\(
\lnot(A \land B) \equiv \lnot A \lor \lnot B
\)

\(
\lnot(A \lor B) \equiv \lnot A \land \lnot B
\)

Son fundamentales para reescribir expresiones lógicas en formas equivalentes.

### Cuantificadores

Los **cuantificadores** conectan una expresión lógica con los elementos de un conjunto.

- \(\forall x \; P(x)\): "Para todo \(x\), \(P(x)\) es verdadero."
- \(\exists x \; P(x)\): "Existe al menos un \(x\) tal que \(P(x)\) es verdadero."

La negación de un cuantificador invierte tanto el cuantificador como la proposición interna:

\(
\lnot(\forall x \; P(x)) \equiv \exists x \; \lnot P(x)
\)

\(
\lnot(\exists x \; P(x)) \equiv \forall x \; \lnot P(x)
\)

!!! example "Ejemplo"
    La proposición "Todos los gatos tienen cola" se escribe \(\forall x (\text{Gato}(x) \Rightarrow \text{TieneCola}(x))\). Su negación es "Existe al menos un gato que no tiene cola": \(\exists x (\text{Gato}(x) \land \lnot \text{TieneCola}(x))\).

### Implicación y contrapositiva

Dada la implicación \(A \Rightarrow B\), se definen tres proposiciones relacionadas:

| Nombre | Forma | Equivalente a la original |
|--------|-------|--------------------------|
| Implicación original | \(A \Rightarrow B\) | Sí |
| Contrapositiva | \(\lnot B \Rightarrow \lnot A\) | **Sí** (siempre equivalente) |
| Inversa | \(\lnot A \Rightarrow \lnot B\) | No |
| Recíproca | \(B \Rightarrow A\) | No |

!!! warning "Error frecuente"
    Que \(A \Rightarrow B\) sea verdadero **no implica** que \(B \Rightarrow A\) lo sea. Pero sí implica que \(\lnot B \Rightarrow \lnot A\) (la contrapositiva) es verdadera.

### Ejercicios de la OCI — Lógica

!!! question "OCI 2023 — Pregunta 10"
    ¿Cuál de las siguientes afirmaciones es la negación correcta de la proposición "Todos los gatos tienen cola"?

    A. Algunos gatos no tienen cola  
    B. Ningún gato tiene cola  
    C. Todos los gatos tienen cola  
    D. Algunos gatos tienen cola  
    E. Todos los gatos no tienen cola

    **Respuesta:** A. La negación de \(\forall x \; P(x)\) es \(\exists x \; \lnot P(x)\): existe al menos un gato que no tiene cola.

!!! question "OCI 2023 — Pregunta 11"
    Considere la expresión lógica \(p \Leftrightarrow q\), equivalente a \((p \Rightarrow q) \land (q \Rightarrow p)\). ¿Cuál de las siguientes opciones representa una expresión equivalente a la **negación** de \(p \Leftrightarrow q\)?

    A. \(p \Leftrightarrow (\lnot q)\)  
    B. \((\lnot p) \Leftrightarrow (\lnot q)\)  
    C. \(\lnot((\lnot p) \Leftrightarrow q)\)  
    D. \(\lnot(p \Leftrightarrow (\lnot q))\)  
    E. \(p \Leftrightarrow q\)

    **Respuesta:** A. Se puede verificar con tabla de verdad que \(p \Leftrightarrow (\lnot q)\) tiene exactamente los valores opuestos a \(p \Leftrightarrow q\), por lo que es su negación.

!!! question "OCI 2023 — Pregunta 13"
    Juan es un estudiante de secundaria. Sabiendo que Juan no tiene elefantes en su casa, la expresión "Todos los elefantes que Juan tiene en su casa saben programar" podemos decir que:

    A. Es completamente falsa  
    B. Es completamente verdadera  
    C. No es ni verdadera ni falsa  
    D. Es una paradoja  
    E. Es imposible determinarlo

    **Respuesta:** B. Es una implicación vacuamente verdadera: como el conjunto "elefantes de Juan" está vacío, ningún contraejemplo puede falsificarla.

!!! question "OCI 2023 — Pregunta 14"
    Si se tiene la expresión "Si llueve, entonces me mojo", puedo afirmar con certeza:

    A. Si estoy mojado es porque llovió  
    B. Si llueve y hace sol, entonces no me mojo  
    C. Si no me mojo, entonces no llueve  
    D. Si llueve y me mojo es porque no porto paraguas  
    E. Ninguna otra opción es correcta

    **Respuesta:** C. La contrapositiva de \(P \Rightarrow Q\) es \(\lnot Q \Rightarrow \lnot P\), que siempre es equivalente a la original.

!!! question "OCI 2024 — Pregunta 2"
    Considere las siguientes proposiciones. Suponga que no existe vida en Marte.

    I. Todos los marcianos saben programar.  
    II. Si al menos un marciano sabe programar, entonces se hallará agua en Marte.  
    III. Existe un marciano que navega por redes sociales.

    ¿Cuáles de esas proposiciones son verdaderas?

    A. Sólo I y II  
    B. Sólo I  
    C. Sólo II  
    D. Todas  
    E. Ninguna

    **Respuesta:** A. I es vacuamente verdadera (no hay marcianos que la contradigan). II también es vacuamente verdadera (su premisa "al menos un marciano sabe programar" es falsa). III es existencial y requiere que exista un marciano, lo cual no ocurre.

!!! question "OCI 2025 — Pregunta 2"
    La proposición "Ningún participante (ni siquiera Conner) adivinó el número secreto" es falsa. Entonces, se puede concluir con certeza que:

    A. Conner adivinó el número secreto.  
    B. Al menos Tobías adivinó el número secreto.  
    C. Todos los participantes (incluso Conner) adivinaron el número secreto.  
    D. Todos los participantes adivinaron el número secreto.  
    E. Hubo al menos un participante que adivinó el número secreto.

    **Respuesta:** E. La negación de "ningún participante" es "al menos un participante". No se puede afirmar quién en particular lo fue.

!!! question "OCI 2025 — Pregunta 15"
    Suponga que la siguiente frase es verdadera y es toda la información que posee: "Todos los animales que son perros, también son mamíferos". De ella se puede inferir correctamente que:

    A. Si un animal no es mamífero, entonces tampoco es perro.  
    B. Los perros no ponen huevos.  
    C. Los animales mamíferos tienen varias cosas en común con los perros.  
    D. Todos los mamíferos son perros.  
    E. Existe un perro y por tanto existe un mamífero.

    **Respuesta:** A. Es la contrapositiva directa de la proposición original.

!!! question "OCI 2025 — Pregunta 16"
    Suponga que $P, Q, R, S$ y $T$ son proposiciones lógicas y se quiere construir la tabla de verdad para:
    \(
    (P \Rightarrow (Q \lor R)) \Rightarrow \lnot(S \land T)
    \)
    ¿Cuántas filas debería tener esta tabla?

    A. 10
    B. 128
    C. 15
    D. 25
    E. 32

    **Respuesta:** E. Con 5 proposiciones, la tabla tiene \(2^5 = 32\) filas.

---

## Números

### Conjuntos numéricos

Los números se organizan en conjuntos anidados:

- \(\mathbb{N}\): números naturales \(\{0, 1, 2, 3, \ldots\}\) (o \(\{1, 2, 3, \ldots\}\), según la convención.
- \(\mathbb{Z}\): enteros \(\{\ldots, -2, -1, 0, 1, 2, \ldots\}\).
- \(\mathbb{Q}\): racionales, de la forma \(\frac{p}{q}\) con \(p, q \in \mathbb{Z}\), \(q \neq 0\).
- \(\mathbb{R}\): reales, que incluyen tanto racionales como irracionales (\(\sqrt{2}\), \(\pi\), \(e\)).

La relación de contenencia es \(\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}\).

!!! note "Propiedad de cierre"
    Los racionales son **cerrados** bajo las operaciones \(+, -, \times, \div\) (excepto dividir por cero): el resultado de operar dos racionales siempre es racional.

### Funciones matemáticas útiles

La **función piso** \(\lfloor x \rfloor\) redondea hacia abajo al entero más cercano; la **función techo** \(\lceil x \rceil\) redondea hacia arriba.
Por ejemplo, \(\lfloor 3.7 \rfloor = 3\) y \(\lceil 3.2 \rceil = 4\).

El **factorial** se define como \(n! = 1 \cdot 2 \cdot 3 \cdots n\) con \(0! = 1\).

### Ejercicios de la OCI — Números

!!! question "OCI 2023 — Pregunta 24"
    Si se multiplican dos números racionales, se puede afirmar con certeza que el número que se obtiene es:

    A. Entero &nbsp; B. Natural &nbsp; C. Racional &nbsp; D. Irracional &nbsp; E. Positivo

    **Respuesta:** C. Los racionales son cerrados bajo la multiplicación.

!!! question "OCI 2025 — Pregunta 4"
    Se tienen las siguientes fracciones:
    \(
    P = \frac{2}{3}, \quad Q = \frac{5}{6}, \quad R = \frac{3}{5}
    \)
    Si se ordenan de mayor a menor, se obtiene:

    A. \([Q, R, P]\) &nbsp; B. \([Q, P, R]\) &nbsp; C. \([R, P, Q]\) &nbsp; D. \([P, Q, R]\) &nbsp; E. \([P, R, Q]\)

    **Respuesta:** B. Convirtiendo a decimales: \(P \approx 0.667\), \(Q \approx 0.833\), \(R = 0.6\). Orden: \(Q > P > R\).

!!! question "OCI 2025 — Pregunta 14"
    Considere las siguientes afirmaciones:

    I. El cero es un número entero par.  
    II. El cero es múltiplo de 3.  
    III. Un número primo se define como un número entero positivo mayor que 1 que es divisible por 1 y por sí mismo.

    De ellas, son verdaderas:

    A. I, II y III &nbsp; B. I y III &nbsp; C. Ninguna &nbsp; D. Solamente III &nbsp; E. I y II

    **Respuesta:** A. Las tres son verdaderas: \(0 = 2 \times 0\) (par), \(0 = 3 \times 0\) (múltiplo de 3), y la definición de primo es estándar.

!!! question "OCI 2025 — Pregunta 26"
    La expresión \(\sqrt{50} + \sqrt{32}\) es igual a:

    A. \(\sqrt{82}\) &nbsp; B. \(7\sqrt{2}\) &nbsp; C. \(3\sqrt{6}\) &nbsp; D. \(\sqrt{18}\) &nbsp; E. \(9\sqrt{2}\)

    **Respuesta:** E. \(\sqrt{50} = 5\sqrt{2}\) y \(\sqrt{32} = 4\sqrt{2}\), por lo que la suma es \(9\sqrt{2}\).

---

## Conjuntos
Un **conjunto** es una colección de elementos sin orden ni repetición.
Se usa la notación \(X = \{2, 4, 7\}\) y \(|X|\) para el tamaño (cardinalidad).

### Operaciones con conjuntos

| Operación | Notación | Descripción |
|-----------|----------|-------------|
| Intersección | \(A \cap B\) | Elementos en ambos conjuntos |
| Unión | \(A \cup B\) | Elementos en al menos uno |
| Complemento | \(\overline{A}\) | Elementos del universo que no están en \(A\) |
| Diferencia | \(A \setminus B\) | Elementos en \(A\) pero no en \(B\) |

!!! example "Ejemplo"
    Si \(A = \{1, 2, 5\}\) y \(B = \{2, 4\}\):

    - \(A \cap B = \{2\}\)
    - \(A \cup B = \{1, 2, 4, 5\}\)
    - \(A \setminus B = \{1, 5\}\)

### Subconjuntos y conjunto potencia

\(A\) es **subconjunto** de \(S\) (escrito \(A \subseteq S\)) si todo elemento de \(A\) también pertenece a \(S\).

El **conjunto potencia** \(\mathcal{P}(S)\) es el conjunto de todos los subconjuntos de \(S\), incluyendo \(\emptyset\) y el propio \(S\).
Si \(|S| = n\), entonces \(|\mathcal{P}(S)| = 2^n\).

!!! example "Ejemplo"
    Para \(S = \{2, 4, 7\}\) con \(|S| = 3\):
    \(\mathcal{P}(S) = \{\emptyset,\, \{2\},\, \{4\},\, \{7\},\, \{2,4\},\, \{2,7\},\, \{4,7\},\, \{2,4,7\}\}\)
    \(|\mathcal{P}(S)| = 2^3 = 8\).

### Ejercicios de la OCI — Conjuntos

!!! question "OCI 2023 — Pregunta 25"
    Sea \(X = \{3, 2, 5\}\) e \(Y = \{7, 3, 5\}\). ¿Cuál es la intersección entre el conjunto potencia de \(X\) y el conjunto potencia de \(Y\)?

    A. \(\emptyset\)  
    B. \(\{\emptyset, 3, 5\}\)  
    C. \(\{\emptyset, \{3\}, \{5\}, \{3,5\}\}\)  
    D. \(\{\{3\}, \{5\}, \{3,5\}\}\)  
    E. \(\{\emptyset, \{3\}, \{5\}\}\)

    **Respuesta:** C. Los subconjuntos comunes a ambos conjuntos potencia son los formados únicamente con elementos en \(X \cap Y = \{3, 5\}\): son \(\emptyset, \{3\}, \{5\}, \{3, 5\}\).

!!! question "OCI 2024 — Pregunta 22"
    Se tienen dos números naturales (con \(0 \in \mathbb{N}\)) \(a\) y \(b\), distintos entre sí, con \(a \neq 1\) y \(b \neq 1\). Sean \(A\) y \(B\) el conjunto de los divisores positivos de \(a\) y \(b\) respectivamente. Considere:

    I. La intersección de \(A\) y \(B\) puede ser vacía.  
    II. La unión de \(A\) y \(B\) siempre tiene más de dos elementos.  
    III. El conjunto de números que aparecen en \(A\) o en \(B\), pero no en ambos, tiene cardinalidad mayor o igual a 2.  
    IV. La cardinalidad de \(A\) puede ser infinita, si \(a\) es cero.

    De ellas, son verdaderas:

    A. Sólo I, II y III &nbsp; B. I, II, III, IV &nbsp; C. Sólo II y III &nbsp; D. Sólo II y IV &nbsp; E. Sólo II, III, IV

    **Respuesta:** D. **I es falsa**: \(1\) divide a cualquier número positivo, así que \(1 \in A \cap B\) siempre. **II es verdadera**: \(A \cup B\) contiene \(\{1, a, b\}\) con \(a \neq b\), por lo que tiene al menos 3 elementos. **III es falsa**: si \(a = 2\) y \(b = 4\), entonces \(A = \{1,2\}\), \(B = \{1,2,4\}\), y la diferencia simétrica \(A \triangle B = \{4\}\) tiene cardinalidad 1. **IV es verdadera**: todo entero no nulo divide a \(0\), así que \(A\) sería infinito.

!!! question "OCI 2025 — Pregunta 6"
    Considere el conjunto \(A = \{1, 2, 3, \ldots, 15\}\). ¿Cuántos subconjuntos de \(A\) contienen al menos un número impar?

    A. \(128 \times 255\) &nbsp; B. \(256\) &nbsp; C. \(2^{14}\) &nbsp; D. \(2^{14} - 1\) &nbsp; E. \(256 \times 127\)

    **Respuesta:** A. Los números pares en \(A\) son 7 (\(\{2,4,6,8,10,12,14\}\)), y los impares son 8. Subconjuntos sin ningún impar \(= 2^7 = 128\). Subconjuntos con al menos un impar \(= 2^{15} - 2^7 = 2^7(2^8 - 1) = 128 \times 255\).

!!! question "OCI 2025 — Pregunta 27"
    Se definen los conjuntos \(A=\{1,2,3,4\}\), \(B=\{3,4,5,6\}\), \(C=\{5,6,7,8\}\) y el conjunto inicial \(S=\{1,2,3,4,5,6,7,8\}\). En cada paso se puede reemplazar \(S\) por \(S \cup X\) o por \(S \cap X\) (con \(X \in \{A,B,C\}\)), siempre que la intersección no sea vacía. ¿Cuál es el menor número de elementos que puede tener \(S\) al final del proceso, y cuántas operaciones son necesarias?

    A. 2 elementos con 2 operaciones.  
    B. 2 elementos con 3 operaciones.  
    C. No se puede determinar con la información dada.  
    D. 4 elementos con 1 operación.  
    E. 8 elementos sin operaciones.

    **Respuesta:** A. Aplicando primero \(S \cap B = \{3,4,5,6\}\) y luego \(\{3,4,5,6\} \cap C = \{5,6\}\), se obtiene un conjunto de 2 elementos en 2 operaciones.

---

## Teoría de Números

La teoría de números estudia las propiedades de los enteros, especialmente la divisibilidad y la estructura multiplicativa.

> Para las implementaciones algorítmicas de estos conceptos (MCD con el algoritmo de Euclides, Criba de Eratóstenes, test de primalidad), ver la sección [Algoritmos](../algoritmos/).

### Divisibilidad

Dados enteros \(a\) y \(b\) con \(b \neq 0\), se dice que \(b\) **divide** a \(a\) (escrito \(b \mid a\)) si existe un entero \(k\) tal que \(a = k \cdot b\).

- Si \(b \mid a\) y \(b \mid c\), entonces \(b \mid (a + c)\).
- Si \(b \mid a\), entonces \(b \mid (a \cdot k)\) para cualquier entero \(k\).

### Aritmética modular

Se escribe \(a \equiv b \pmod{m}\) y se lee "\(a\) es congruente con \(b\) módulo \(m\)" cuando \(m \mid (a - b)\), equivalentemente, cuando \(a\) y \(b\) tienen el mismo residuo al dividirse por \(m\).

Las propiedades fundamentales son:

\((a + b) \bmod m = \bigl((a \bmod m) + (b \bmod m)\bigr) \bmod m\)

\((a \cdot b) \bmod m = \bigl((a \bmod m) \cdot (b \bmod m)\bigr) \bmod m\)


### Máximo Común Divisor y Mínimo Común Múltiplo

- El **MCD** de dos enteros es el mayor divisor común a ambos.
- El **MCM** es el menor múltiplo común.

Existe la propiedad:

\(\text{MCD}(a, b) \cdot \text{MCM}(a, b) = a \cdot b\)

### Ejercicios de la OCI — Teoría de Números

!!! question "OCI 2023 — Pregunta 6"
    Se sabe que la factorización de un número es \(2^n \times 5^n\). Por tanto, ese número en base 10 tiene:

    A. \(n-1\) dígitos &nbsp; B. \(n\) dígitos &nbsp; C. \(n+1\) dígitos &nbsp; D. \(2n\) dígitos &nbsp; E. Es imposible determinarlo

    **Respuesta:** C. \(2^n \times 5^n = 10^n\), que es el número 1 seguido de \(n\) ceros, es decir, \(n+1\) dígitos.

!!! question "OCI 2023 — Pregunta 15"
    Sean dos enteros \(a\) y \(b\) tales que \((a^2 + b^2) \bmod 4 = 3\). Se puede afirmar que:

    A. Esos enteros son menores que 100.  
    B. Es imposible encontrar dichos enteros.  
    C. Esos enteros poseen al menos 10 dígitos.  
    D. Esos enteros son impares.  
    E. Esos enteros son pares.

    **Respuesta:** B. Para cualquier entero \(n\): si \(n\) es par, \(n^2 \equiv 0 \pmod{4}\); si \(n\) es impar, \(n^2 \equiv 1 \pmod{4}\). Entonces \(a^2 + b^2 \pmod{4}\) solo puede ser \(0, 1\) o \(2\), nunca 3.

!!! question "OCI 2023 — Pregunta 28"
    Se tienen dos enteros positivos \(a\) y \(b\) tales que:
    - La factorización de \(a\) consiste en el producto de exactamente dos factores primos.
    - La factorización de \(b\) consiste en el producto de exactamente dos factores primos.
    - El máximo común divisor de \(a\) y \(b\) es igual a 7.

    ¿Cuál es el valor mínimo posible para \(a \cdot b\)?

    A. 49 &nbsp; B. 98 &nbsp; C. 196 &nbsp; D. 294 &nbsp; E. 784

    **Respuesta:** C. Como \(\text{MCD}(a,b) = 7\), el primo 7 divide a ambos. Con exactamente dos factores primos: \(a = 7p\) y \(b = 7q\) para primos \(p, q\). Entonces \(a \cdot b = 49pq\). Para minimizar, se toma \(p = q = 2\), lo que da \(a = b = 14\) y \(a \cdot b = 196\).

!!! question "OCI 2024 — Pregunta 19"
    Beto tiene \(394\,526\) chocolates y decide separarlos en bolsitas de 7. ¿Cuántos chocolates le sobran?

    A. Ninguno &nbsp; B. 1 &nbsp; C. 2 &nbsp; D. 4 &nbsp; E. 6

    **Respuesta:** E. \(394\,526 = 7 \times 56\,360 + 6\), ya que \(7 \times 56\,360 = 394\,520\) y \(394\,526 - 394\,520 = 6\).

!!! question "OCI 2024 — Pregunta 27"
    Se tiene un número \(n\) cuya factorización es \(2^{20} \cdot 3^9 \cdot 5^{18}\). ¿Cuántos factores propios (menores que \(n\)) tiene este número?

    A. 3240 &nbsp; B. 3239 &nbsp; C. 2584 &nbsp; D. 2583 &nbsp; E. 3989

    **Respuesta:** E. El número total de divisores es \((20+1)(9+1)(18+1) = 21 \times 10 \times 19 = 3990\). Los factores propios excluyen al propio \(n\), así que son \(3990 - 1 = 3989\).

!!! question "OCI 2025 — Pregunta 7"
    Luis se pregunta si existen números primos \(p\) tales que \(p + 9\) sea un cuadrado perfecto. Al trabajar con la ecuación, llega a que \(p = (n+3)(n-3)\) donde \(n\) es un entero. ¿Cuántos números primos cumplen esta condición?

    A. Exactamente dos diferentes.  
    B. Solo los positivos de \(n\), exactamente tres soluciones.  
    C. Ninguno, porque todo producto de dos factores no puede ser primo.  
    D. Exactamente uno.  
    E. Infinitos.

    **Respuesta:** D. Para que \(p = (n+3)(n-3)\) sea primo, uno de los factores debe ser 1 y el otro debe ser \(p\). La solución \(n - 3 = 1 \Rightarrow n = 4\) da \(p = 7\). Verificación: \(7 + 9 = 16 = 4^2\). ✓ Es el único primo que cumple la condición.

!!! question "OCI 2025 — Pregunta 20"
    Sean \(a\), \(b\) y \(m\) enteros positivos con \(a \equiv b \pmod{m}\). Considere:

    I. \(a + m \equiv b + m \pmod{m}\)  
    II. \(a - b\) es divisible por \(m\)  
    III. \(\dfrac{a}{m} \equiv \dfrac{b}{m} \pmod{m}\)  
    IV. \(m \bmod a = m \bmod b\)

    De ellas, son verdaderas:

    A. Solo I &nbsp; B. Todas &nbsp; C. Ninguna &nbsp; D. I, II y IV &nbsp; E. I y II

    **Respuesta:** E. **I**: \((a+m) \bmod m = a \bmod m\) y \((b+m) \bmod m = b \bmod m\), que son iguales. ✓ **II**: la definición de congruencia equivale a que \(m \mid (a-b)\). ✓ **III y IV** no se sostienen en general.

---

## Combinatoria

La combinatoria cuenta la cantidad de configuraciones posibles bajo ciertas restricciones.

### Regla de la suma y regla del producto

- **Regla de la suma**: si una tarea puede realizarse de \(m\) maneras **o** de \(n\) maneras (mutuamente excluyentes), entonces hay \(m + n\) maneras en total.
- **Regla del producto**: si una tarea se compone de una decisión de \(m\) maneras **y** luego una de \(n\) maneras (independientes), hay \(m \times n\) maneras en total.

### Permutaciones

Una **permutación** es un arreglo ordenado.
El número de formas de ordenar \(n\) objetos distintos es \(n!\).
Para elegir y ordenar \(k\) de \(n\) objetos:

\(P(n, k) = \dfrac{n!}{(n-k)!}\)

Si hay objetos repetidos (por ejemplo, \(r_1\) de un tipo, \(r_2\) de otro, etc.), el número de permutaciones distintas es:

\(\dfrac{n!}{r_1!\, r_2!\, \cdots}\)

### Combinaciones

Una **combinación** es una selección sin importar el orden.
El número de formas de elegir \(k\) de \(n\) objetos distintos es el **coeficiente binomial**:

\(\dbinom{n}{k} = \dfrac{n!}{k!\,(n-k)!}\)

El total de subconjuntos de un conjunto de \(n\) elementos es \(\displaystyle\sum_{k=0}^{n}\binom{n}{k} = 2^n\).

### Principio de inclusión-exclusión

Para dos conjuntos:
\(
|A \cup B| = |A| + |B| - |A \cap B|
\)

Para tres conjuntos:
\(
|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|
\)

### Principio del palomar

Si se distribuyen \(n\) objetos en \(k\) contenedores y \(n > k\), entonces al menos un contenedor contiene más de un objeto.
Equivalentemente, si \(n > k \cdot m\), algún contenedor contiene al menos \(m + 1\) objetos.

### Probabilidad

La **probabilidad** de un evento \(A\) en un espacio equiprobable es:
\(
P(A) = \frac{\text{casos favorables}}{\text{casos totales}}
\)

Para eventos no mutuamente excluyentes:
\(
P(A \cup B) = P(A) + P(B) - P(A \cap B)
\)

### Fórmulas de suma

\(
\sum_{k=1}^{n} k = \frac{n(n+1)}{2} \qquad \sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
\)

### Ejercicios de la OCI — Combinatoria

!!! question "OCI 2023 — Pregunta 2"
    En Imagilonia, en lugar de utilizar bits tradicionales con dos estados, se emplean los 3-bits con tres estados: 0, 1 y 2. ¿Cuántos estados tiene en total un 3-byte (secuencia de ocho 3-bits)?

    A. 24 &nbsp; B. 256 &nbsp; C. 6561 &nbsp; D. 1024 &nbsp; E. Es imposible determinarlo

    **Respuesta:** C. Por la regla del producto, cada posición tiene 3 opciones: \(3^8 = 6561\).

!!! question "OCI 2023 — Pregunta 4"
    En un restaurante, un casado se configura eligiendo exactamente una opción de carne, dos opciones de guarnición y una opción de ensalada. Las alternativas son: 3 carnes, 4 guarniciones y 3 ensaladas. ¿De cuántas maneras se puede armar un casado?

    A. 54 &nbsp; B. 108 &nbsp; C. 36 &nbsp; D. 10 &nbsp; E. Ninguna opción tiene la respuesta correcta

    **Respuesta:** A. Se elige 1 de 3 carnes, luego 2 de 4 guarniciones (sin orden): \(\binom{4}{2} = 6\), luego 1 de 3 ensaladas. Total: \(3 \times 6 \times 3 = 54\).

!!! question "OCI 2023 — Pregunta 21"
    Se tienen dos dados con caras numeradas del 1 al 6. ¿Cuál es la probabilidad de que al lanzarlos, los números obtenidos (una vez ordenados) resulten ser consecutivos?

    A. \(\dfrac{1}{2}\) &nbsp; B. \(\dfrac{1}{3}\) &nbsp; C. \(\dfrac{1}{6}\) &nbsp; D. \(\dfrac{5}{18}\) &nbsp; E. \(\dfrac{5}{36}\)

    **Respuesta:** D. Los pares consecutivos posibles son \((1,2),(2,1),(2,3),(3,2),(3,4),(4,3),(4,5),(5,4),(5,6),(6,5)\): 10 pares favorables de 36 totales. \(P = \dfrac{10}{36} = \dfrac{5}{18}\).

!!! question "OCI 2023 — Pregunta 22"
    En un grupo de 150 personas, 35 hablan inglés, 70 hablan español y 15 hablan ambos idiomas. ¿Cuántas personas no hablan ni inglés ni español?

    A. 30 &nbsp; B. 45 &nbsp; C. 60 &nbsp; D. 90 &nbsp; E. 135

    **Respuesta:** C. Por inclusión-exclusión: \(|I \cup E| = 35 + 70 - 15 = 90\). Los que no hablan ninguno: \(150 - 90 = 60\).

!!! question "OCI 2023 — Pregunta 31"
    ¿Cuántos anagramas distintos tiene la palabra PREPARAR?

    A. 40320 &nbsp; B. 6720 &nbsp; C. 3360 &nbsp; D. 1680 &nbsp; E. 560

    **Respuesta:** D. PREPARAR tiene 8 letras: P(2), R(3), E(1), A(2). Número de permutaciones distintas: \(\dfrac{8!}{2!\cdot 3!\cdot 1!\cdot 2!} = \dfrac{40320}{24} = 1680\).

!!! question "OCI 2024 — Pregunta 6"
    Paula y Josué generan cada uno un número aleatorio de 4 dígitos (del 0000 al 9999) con igual probabilidad. En un turno, se dieron cuenta de que sus números coincidían en la primera, segunda y cuarta posición. ¿Cuál es la probabilidad de que esto ocurra en un turno?

    A. 1 en 100 &nbsp; B. 1 en 1.000 &nbsp; C. 1 en 10.000 &nbsp; D. 1 en 1.000.000 &nbsp; E. 1 en 100.000.000

    **Respuesta:** B. Fijado el número de Paula, los números de Josué que coinciden en las posiciones 1, 2 y 4 son 10 (la posición 3 puede ser cualquier dígito). Probabilidad: \(10 / 10000 = 1/1000\).

!!! question "OCI 2024 — Pregunta 11"
    ¿Cuántos anagramas distintos tiene la palabra ENTRETENER?

    A. 453600 &nbsp; B. 113400 &nbsp; C. 75600 &nbsp; D. 37800 &nbsp; E. 18900

    **Respuesta:** E. ENTRETENER tiene 10 letras: E(4), N(2), T(2), R(2). Permutaciones: \(\dfrac{10!}{4!\cdot 2!\cdot 2!\cdot 2!} = \dfrac{3628800}{192} = 18900\).

!!! question "OCI 2024 — Pregunta 23"
    En un bus viajan personas a un congreso. De ellas, 28 saben programar en Python, 35 en C++ y 20 en Java. Además, 5 saben solo Java, 10 saben Java y Python, 17 saben solo C++ y 30 saben solo un lenguaje. Todas saben al menos uno. ¿Cuántas saben los tres lenguajes?

    A. 3 &nbsp; B. 5 &nbsp; C. 8 &nbsp; D. 9 &nbsp; E. 10

    **Respuesta:** A. Denotando \(x = |P \cap C \cap J|\) y resolviendo el sistema: solo Python \(= 8\), solo C++ \(= 17\), solo Java \(= 5\) (suman 30 ✓). De \(|P| = 28\): \(|P \cap C \setminus J| = 10\). De \(|C| = 35\): \(|C \cap J \setminus P| = 5\). De \(|J| = 20\): \(5 + 7 + 5 + x = 20 \Rightarrow x = 3\).

!!! question "OCI 2024 — Pregunta 25"
    En una fiesta, los brazaletes cambian de color aleatoriamente entre 5 colores. Pablo y Jimena saltan al mismo tiempo y se detienen cuando obtienen una combinación de colores que ya tuvieron antes. ¿Cuál es el máximo número de saltos antes de detenerse?

    A. 25 &nbsp; B. 26 &nbsp; C. 24 &nbsp; D. 125 &nbsp; E. 6

    **Respuesta:** B. Hay \(5 \times 5 = 25\) combinaciones posibles. Tras 25 saltos, se han usado como máximo 25 combinaciones distintas; el salto 26 necesariamente repite una. Por el principio del palomar, el máximo es 26.

!!! question "OCI 2024 — Pregunta 38"
    ¿Cuál es el resultado de sumar los números naturales menores o iguales a 1000?

    A. 500500 &nbsp; B. 500000 &nbsp; C. 495000 &nbsp; D. 510000 &nbsp; E. 499500

    **Respuesta:** A. Usando la fórmula: \(\displaystyle\sum_{k=1}^{1000} k = \dfrac{1000 \times 1001}{2} = 500500\).

!!! question "OCI 2025 — Pregunta 5"
    Luis es profesor de 23 estudiantes (numerados del 1 al 23). Cada semana genera 10 números aleatorios entre 1 y 23 (con repetición) y hace una pregunta a cada persona seleccionada. Las preguntas se acumulan semana a semana. ¿Cuántas semanas deben transcurrir para garantizar que al menos alguien haya recibido 4 o más preguntas?

    A. 5 semanas &nbsp; B. No es posible &nbsp; C. 7 semanas &nbsp; D. 9 semanas &nbsp; E. 4 semanas

    **Respuesta:** C. Tras \(W\) semanas hay \(10W\) preguntas. Para garantizar que algún estudiante tenga \(\geq 4\), se necesita \(10W > 3 \times 23 = 69\), es decir, \(10W \geq 70\), lo que da \(W \geq 7\).

!!! question "OCI 2025 — Pregunta 9"
    Marco necesita seleccionar una entrada, una bebida, un postre, un plato principal y un acompañamiento. Tiene disponibles 3 tipos de entradas, 12 bebidas, 8 postres, 10 platos principales y 9 acompañamientos. ¿Cuántos menús distintos puede crear?

    A. \({}_{42}P_5\) &nbsp; B. \({}_{42}C_5\) &nbsp; C. \(3\cdot 8\cdot 9\cdot 10\cdot 12\) &nbsp; D. \(\dfrac{42!}{3!\cdot 8!\cdot 9!\cdot 10!\cdot 12!}\) &nbsp; E. \(3+8+9+10+12\)

    **Respuesta:** C. Por la regla del producto: \(3 \times 12 \times 8 \times 10 \times 9 = 25920\).

!!! question "OCI 2025 — Pregunta 10"
    Sofía tiene cuatro opciones de ropa: pantalón corto, pantalón largo, enagua o vestido. Tiene 10 pantalones cortos, 7 pantalones largos, 6 enaguas y 3 vestidos. ¿De cuántas maneras puede vestirse hoy?

    A. \(\dfrac{26!}{10!\cdot 7!\cdot 6!\cdot 3!}\) &nbsp; B. \({}_{26}C_4\) &nbsp; C. \(10\cdot 7\cdot 6\cdot 3\) &nbsp; D. \(10+7+6+3\) &nbsp; E. \({}_{26}P_4\)

    **Respuesta:** D. Elige una categoría y de ella una prenda. Por la regla de la suma: \(10 + 7 + 6 + 3 = 26\).

!!! question "OCI 2025 — Pregunta 24"
    Julián encontró una lista de 100 problemas de programación y ha decidido resolver 10 hoy. ¿De cuántas formas distintas puede elegir los 10 problemas?

    A. \({}_{10}C_{10} \cdot {}_{90}C_0\) &nbsp; B. \(\dbinom{100}{10}\) &nbsp; C. \(10!\) &nbsp; D. \(\dfrac{100!}{\dbinom{100}{10}}\) &nbsp; E. \({}_{100}P_{10}\)

    **Respuesta:** B. Se elige sin importar el orden: \(\dbinom{100}{10}\).

---

## Grafos

Un **grafo** \(G = (V, E)\) consiste en un conjunto de **vértices** (nodos) \(V\) y un conjunto de **aristas** \(E\) que conectan pares de vértices.
El **grado** de un vértice es el número de aristas que inciden en él.

### Lema del apretón de manos

En todo grafo no dirigido, la suma de los grados de todos los vértices es el doble del número de aristas:

\(\displaystyle\sum_{v \in V} \deg(v) = 2\,|E|\)

Esto se debe a que cada arista contribuye exactamente 1 al grado de cada uno de sus dos extremos.

!!! example "Ejemplo"
    En una red de 10 computadoras donde cada una está conectada directamente con las otras 9: cada vértice tiene grado 9, y la suma de grados es \(10 \times 9 = 90 = 2\,|E|\), por lo que \(|E| = 45\).

En un **grafo dirigido**, cada arista tiene una dirección, por lo que cada nodo tiene un **grado de entrada** y un **grado de salida**.
La suma de todos los grados de salida es igual a la suma de todos los grados de entrada (igual al número de aristas).

### Ejercicios de la OCI — Grafos

!!! question "OCI 2023 — Pregunta 5"
    En un laboratorio de 10 computadoras, se desea conectar directamente cada una con las otras 9. Cada cable conecta exactamente dos computadoras. ¿Cuántos cables se necesitan como mínimo para garantizar que todas estén conectadas entre sí?

    A. 90 &nbsp; B. 100 &nbsp; C. 45 &nbsp; D. 50 &nbsp; E. Es imposible determinarlo

    **Respuesta:** C. Por el lema del apretón de manos: suma de grados \(= 10 \times 9 = 90 = 2\,|E|\), por lo tanto \(|E| = 45\).

!!! question "OCI 2023 — Pregunta 27"
    Se tiene un grafo dirigido donde cada arista conecta dos nodos distintos. Si la suma de los grados de salida de cada nodo es igual a 35, se puede afirmar con certeza que la suma de los grados de entrada de cada nodo es:

    A. Estrictamente menor que 35  
    B. Exactamente igual a 35  
    C. Estrictamente mayor que 35 y menor que 70  
    D. Exactamente igual a 70  
    E. Estrictamente mayor que 70

    **Respuesta:** B. Cada arista contribuye exactamente 1 al grado de salida de un nodo y 1 al grado de entrada de otro. Por tanto, la suma de grados de entrada siempre es igual a la suma de grados de salida.

!!! question "OCI 2024 — Pregunta 10"
    Se tiene un grafo simple no dirigido donde los grados de cada uno de sus \(n\) nodos son iguales a \(k\). ¿Cuántas aristas tiene?

    A. 64 &nbsp; B. 128 &nbsp; C. \(\dfrac{nk}{2}\) &nbsp; D. 320 &nbsp; E. 640

    **Respuesta:** C. Por el lema del apretón de manos: \(\displaystyle\sum_v \deg(v) = n \cdot k = 2\,|E|\), por lo tanto \(|E| = \dfrac{nk}{2}\).

!!! question "OCI 2025 — Pregunta 18"
    ¿Cuál de las siguientes afirmaciones tiene que ser **falsa** sobre un grafo simple no dirigido?

    A. Tiene la misma cantidad de vértices de grado par que de grado impar.  
    B. Tiene exactamente 3 vértices de grado par.  
    C. Tiene exactamente 5 vértices de grado impar.  
    D. Tiene exactamente 4 vértices de grado par.  
    E. Tiene exactamente 8 vértices de grado impar.

    **Respuesta:** C. El corolario del lema del apretón de manos garantiza que el número de vértices con grado impar es siempre par. Tener exactamente 5 (un número impar) es imposible.

---

## Geometría

### Distancia euclidiana

La **distancia euclidiana** entre dos puntos \(P_1 = (x_1, y_1)\) y \(P_2 = (x_2, y_2)\) en el plano es:

\(d(P_1, P_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\)

Esto es una aplicación directa del teorema de Pitágoras: la distancia es la hipotenusa del triángulo rectángulo cuyos catetos son las diferencias en \(x\) e \(y\).

En tres dimensiones, para \(P_1 = (x_1, y_1, z_1)\) y \(P_2 = (x_2, y_2, z_2)\):

\(d(P_1, P_2) = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}\)

### Ejercicios de la OCI — Geometría

!!! question "OCI 2023 — Pregunta 23"
    La distancia euclidiana en el plano cartesiano entre los puntos \((3, 13)\) y \((7, 10)\) es:

    A. 4 &nbsp; B. 5 &nbsp; C. 10 &nbsp; D. 16 &nbsp; E. 25

    **Respuesta:** B. \(d = \sqrt{(7-3)^2 + (10-13)^2} = \sqrt{16 + 9} = \sqrt{25} = 5\).

!!! question "OCI 2024 — Pregunta 26"
    Ramón y Jazmín viven en edificios frente a frente. El punto de conexión del cable en el apartamento de Ramón está a 22,5 m sobre el suelo, y en el de Jazmín a 17,5 m. La distancia horizontal entre edificios es de 15 m. ¿Cuál es la distancia exacta entre los puntos de conexión?

    A. 12,81 m &nbsp; B. 15,21 m &nbsp; C. 15,81 m &nbsp; D. 16,15 m &nbsp; E. 11,34 m

    **Respuesta:** C. \(d = \sqrt{15^2 + (22.5 - 17.5)^2} = \sqrt{225 + 25} = \sqrt{250} \approx 15{,}81\) m.

!!! question "OCI 2025 — Pregunta 8"
    ¿Cuál es el área de un triángulo isósceles donde un lado mide 10 m y otro 20 m?

    A. \(25\sqrt{15}\) m² &nbsp; B. \(100\) m² &nbsp; C. \(50\sqrt{5}\) m² &nbsp; D. \(50\sqrt{3}\) m² &nbsp; E. \(25\sqrt{10}\) m²

    **Respuesta:** A. El triángulo con lados 10, 10, 20 viola la desigualdad triangular, así que el triángulo válido es 10, 20, 20. Base \(= 10\), lados iguales \(= 20\). La altura es \(h = \sqrt{20^2 - 5^2} = \sqrt{400 - 25} = \sqrt{375} = 5\sqrt{15}\). Área \(= \frac{1}{2} \times 10 \times 5\sqrt{15} = 25\sqrt{15}\) m².

!!! question "OCI 2025 — Pregunta 19"
    Considere las siguientes afirmaciones sobre figuras geométricas:

    I. Todo rectángulo es un paralelogramo.  
    II. Todo trapecio es un paralelogramo.  
    III. Todo rombo es un paralelogramo.  
    IV. Dado un rectángulo, siempre se puede construir un trapecio que tenga la misma área.

    De ellas, son verdaderas:

    A. Solo III y IV &nbsp; B. I, II, III y IV &nbsp; C. Solo I, III y IV &nbsp; D. Solo I y II &nbsp; E. Solo I y III

    **Respuesta:** C. Un rectángulo tiene dos pares de lados paralelos (paralelogramo ✓). Un trapecio tiene solo un par de lados paralelos, por lo tanto **no** es un paralelogramo (II es falsa). Un rombo tiene dos pares de lados paralelos (paralelogramo ✓). Para IV, dado un rectángulo de base \(b\) y altura \(h\) (área \(= bh\)), se construye un trapecio con bases \(a\) y \(b\) y altura \(h'\) tal que \(\frac{(a+b)}{2} \cdot h' = bh\), lo cual siempre es posible ✓.
