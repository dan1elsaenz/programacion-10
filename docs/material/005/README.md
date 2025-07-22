# Clase 5: Ejercicios de `for` loops <!-- omit from toc -->

<details>
    <summary>Tabla de contenidos</summary>

- [1. Ejercicios de `for` loop](#1-ejercicios-de-for-loop)
  - [Ejercicio 1: Contar vocales en una palabra](#ejercicio-1-contar-vocales-en-una-palabra)
  - [Ejercicio 2: Filtrar palabras cortas](#ejercicio-2-filtrar-palabras-cortas)
  - [Ejercicio 3: Encontrar la palabra más larga en una lista](#ejercicio-3-encontrar-la-palabra-más-larga-en-una-lista)
  - [Ejercicio 4: Contar palabras que contienen una letra específica](#ejercicio-4-contar-palabras-que-contienen-una-letra-específica)
  - [Ejercicio 5: Convertir palabras a mayúsculas si tienen más de 5 letras](#ejercicio-5-convertir-palabras-a-mayúsculas-si-tienen-más-de-5-letras)
  - [Ejercicio 6: Reemplazar vocales en una palabra](#ejercicio-6-reemplazar-vocales-en-una-palabra)
  - [Ejercicio 7: Eliminar palabras repetidas de una lista](#ejercicio-7-eliminar-palabras-repetidas-de-una-lista)
  - [Ejercicio 8: Determinar si una lista está ordenada](#ejercicio-8-determinar-si-una-lista-está-ordenada)
  - [Ejercicio 9: Concatenar todas las palabras de una lista](#ejercicio-9-concatenar-todas-las-palabras-de-una-lista)
  - [Ejercicio 10: Contar números pares e impares en una lista](#ejercicio-10-contar-números-pares-e-impares-en-una-lista)
  - [Ejercicio 11: Contar letras en una lista de palabras](#ejercicio-11-contar-letras-en-una-lista-de-palabras)
  - [Ejercicio 12: Palabras que terminan con una letra específica](#ejercicio-12-palabras-que-terminan-con-una-letra-específica)
  - [Ejercicio 13: Contar cuántas veces aparece una letra en cada palabra](#ejercicio-13-contar-cuántas-veces-aparece-una-letra-en-cada-palabra)
  - [Ejercicio 14: Buscar palabras con letras repetidas (for anidado)](#ejercicio-14-buscar-palabras-con-letras-repetidas-for-anidado)
  - [Ejercicio 15: Contar letras vocales en cada palabra (for anidado)](#ejercicio-15-contar-letras-vocales-en-cada-palabra-for-anidado)
  - [Ejercicio 16: Mostrar letras comunes entre pares de palabras (for anidado)](#ejercicio-16-mostrar-letras-comunes-entre-pares-de-palabras-for-anidado)
  - [Ejercicio 17: Contar cuántas palabras contienen al menos una vocal](#ejercicio-17-contar-cuántas-palabras-contienen-al-menos-una-vocal)

</details>

## 1. Ejercicios de `for` loop

### Ejercicio 1: Contar vocales en una palabra

Escribe un programa que reciba una palabra y cuente cuántas vocales (`a, e, i, o, u`) tiene.  

**Ejemplo:**  
```plaintext
Entrada: "elefante"  
Salida: 4

Entrada: "python"  
Salida: 1
```

### Ejercicio 2: Filtrar palabras cortas  

Dada una lista de palabras, devuelve una nueva lista que contenga solo aquellas palabras con más de 4 letras.  

**Ejemplo:**  
```plaintext
Entrada: ["sol", "estrella", "luz", "universo"]  
Salida: ["estrella", "universo"]
```

### Ejercicio 3: Encontrar la palabra más larga en una lista  

Dada una lista de palabras, devuelve la palabra con más caracteres. Si hay más de una con la misma longitud, devuelve la primera que aparece.  

**Ejemplo:**  
```plaintext
Entrada: ["perro", "elefante", "ratón"]  
Salida: "elefante"
```

### Ejercicio 4: Contar palabras que contienen una letra específica  

Dada una lista de palabras y una letra, cuenta cuántas palabras contienen esa letra.  

**Ejemplo:**  
```plaintext
Entrada: ["casa", "carro", "perro", "gato"], "r"  
Salida: 2
```

### Ejercicio 5: Convertir palabras a mayúsculas si tienen más de 5 letras  

Dada una lista de palabras, devuelve una nueva lista donde las palabras con más de 5 letras estén en mayúsculas y las demás queden igual.  

**Ejemplo:**  
```plaintext
Entrada: ["hola", "elefante", "mundo", "estrella"]  
Salida: ["hola", "ELEFANTE", "mundo", "ESTRELLA"]
```

### Ejercicio 6: Reemplazar vocales en una palabra  

Escribe un programa que reemplace todas las vocales de una palabra por un asterisco `*`.  

**Ejemplo:**  
```plaintext
Entrada: "programación"  
Salida: "pr*gr*m*c**n"
```

### Ejercicio 7: Eliminar palabras repetidas de una lista  

Dada una lista de palabras, devuelve una nueva lista con las palabras sin repetir, conservando el orden original.  

**Ejemplo:**  
```plaintext
Entrada: ["manzana", "pera", "manzana", "uva", "pera"]  
Salida: ["manzana", "pera", "uva"]
```

### Ejercicio 8: Determinar si una lista está ordenada  

Escribe un programa que reciba una lista de números y determine si está ordenada de menor a mayor.  

**Ejemplo:**  
```plaintext
Entrada: [1, 2, 3, 4, 5]  
Salida: True

Entrada: [3, 1, 4, 2, 5]  
Salida: False
```

### Ejercicio 9: Concatenar todas las palabras de una lista  

Dada una lista de palabras, devuelve un solo string donde todas las palabras estén separadas por un espacio (sin utilizar el método `join()`)

**Ejemplo:**  
```plaintext
Entrada: ["Hola", "mundo", "esto", "es", "Python"]  
Salida: "Hola mundo esto es Python"
```

### Ejercicio 10: Contar números pares e impares en una lista  

Dada una lista de números enteros, cuenta cuántos son pares y cuántos son impares.  

**Ejemplo:**  
```plaintext
Entrada: [1, 2, 3, 4, 5, 6]  
Salida: "Pares: 3, Impares: 3"
```

### Ejercicio 11: Contar letras en una lista de palabras  

Dada una lista de palabras, devuelve una nueva lista con la cantidad de letras que tiene cada palabra.  

**Ejemplo:**  
```plaintext
Entrada: ["hola", "elefante", "sol"]  
Salida: [4, 8, 3]
```

### Ejercicio 12: Palabras que terminan con una letra específica  

Dada una lista de palabras y una letra, devuelve una lista con las palabras que terminan con esa letra.  

**Ejemplo:**  
```plaintext
Entrada: ["luz", "sol", "coral", "animal"], "l"  
Salida: ["coral", "animal"]
```

### Ejercicio 13: Contar cuántas veces aparece una letra en cada palabra  

Dada una lista de palabras y una letra, crea una nueva lista con la cantidad de veces que esa letra aparece en cada palabra.  

**Ejemplo:**  
```plaintext
Entrada: ["banana", "manzana", "pera"], "a"  
Salida: [3, 3, 1]
```

### Ejercicio 14: Buscar palabras con letras repetidas (for anidado)  

Dada una lista de palabras, devuelve una lista con las palabras que tienen alguna letra repetida.  

**Ejemplo:**  
```plaintext
Entrada: ["sol", "gato", "taza", "luz", "elefante"]  
Salida: ["taza", "elefante"]
```

### Ejercicio 15: Contar letras vocales en cada palabra (for anidado)  

Dada una lista de palabras, devuelve una lista con la cantidad de vocales que tiene cada una.  

**Ejemplo:**  
```plaintext
Entrada: ["hola", "python", "elefante"]  
Salida: [2, 1, 4]
```

### Ejercicio 16: Mostrar letras comunes entre pares de palabras (for anidado)  

Dada una lista de dos palabras, muestra las letras que tienen en común (sin repetir letras).  

**Ejemplo:**  
```plaintext
Entrada: ["python", "elefante"]  
Salida: ['e', 'n']
```

### Ejercicio 17: Contar cuántas palabras contienen al menos una vocal  

Dada una lista de palabras, cuenta cuántas contienen al menos una vocal.  

**Ejemplo:**  
```plaintext
Entrada: ["sky", "agua", "sol", "fly"]  
Salida: 2
```

