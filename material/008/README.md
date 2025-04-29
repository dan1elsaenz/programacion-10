# Clase 8: Estructuras de Datos en Python (Tuplas, Diccionarios y Sets) <!-- omit from toc -->

<details> 
  <summary>Tabla de contenidos</summary>

- [Tuplas](#tuplas)
  - [¿Qué es una tupla?](#qué-es-una-tupla)
  - [¿Cómo crear una tupla?](#cómo-crear-una-tupla)
  - [Propiedades de las tuplas](#propiedades-de-las-tuplas)
  - [Obtener el largo de una tupla](#obtener-el-largo-de-una-tupla)
  - [Acceder a elementos](#acceder-a-elementos)
  - [Modificar una tupla (usando _type-casting_)](#modificar-una-tupla-usando-type-casting)
  - [Eliminar una tupla](#eliminar-una-tupla)
  - [Unir tuplas](#unir-tuplas)
  - [Métodos de tuplas](#métodos-de-tuplas)
- [Diccionarios](#diccionarios)
  - [¿Qué es un diccionario?](#qué-es-un-diccionario)
  - [Cómo definir un diccionario](#cómo-definir-un-diccionario)
  - [Propiedades de los diccionarios](#propiedades-de-los-diccionarios)
  - [Acceder y modificar elementos](#acceder-y-modificar-elementos)
  - [Métodos útiles](#métodos-útiles)
  - [Agregar elementos](#agregar-elementos)
  - [Eliminar elementos](#eliminar-elementos)
  - [Recorrer diccionarios](#recorrer-diccionarios)
  - [Copiar un diccionario](#copiar-un-diccionario)
  - [Diccionarios anidados](#diccionarios-anidados)
  - [Resumen de métodos de diccionarios](#resumen-de-métodos-de-diccionarios)
- [Sets (Conjuntos)](#sets-conjuntos)
  - [¿Qué es un set?](#qué-es-un-set)
  - [Crear un set](#crear-un-set)
  - [Propiedades de los sets](#propiedades-de-los-sets)
  - [Verificar pertenencia](#verificar-pertenencia)
  - [Agregar elementos](#agregar-elementos-1)
  - [Eliminar elementos](#eliminar-elementos-1)
  - [Operaciones entre sets](#operaciones-entre-sets)
  - [Tabla resumen de métodos de sets](#tabla-resumen-de-métodos-de-sets)

</details> 

Esta clase cubre tres estructuras de datos fundamentales restantes en Python: **tuplas**, **diccionarios** y **sets**.
Cada una tiene propiedades particulares, ventajas específicas y una variedad de métodos útiles para resolver distintos tipos de problemas.

---

## Tuplas

### ¿Qué es una tupla?
# Clave = Llave
# Valor = Contenido detrás de la puerta

Una tupla es una colección ordenada de elementos que no puede ser modificada después de su creación.
Son útiles cuando se desea almacenar datos que no deben cambiar, como coordenadas, fechas o información de configuración.

### ¿Cómo crear una tupla?

Las tuplas pueden crearse utilizando paréntesis o el constructor `tuple()`.

```python
tupla1 = ("manzana", "banana", "cereza")
tupla2 = tuple([1, 2, 3])
```

### Propiedades de las tuplas

- Son ordenadas: mantienen el orden en el que fueron creadas.
- Son inmutables: no se pueden modificar después de creadas.
- Permiten elementos duplicados.
- Son iterables: se pueden recorrer con un bucle `for`.

### Obtener el largo de una tupla

Se utiliza la función `len()` para conocer la cantidad de elementos en una tupla.

```python
print(len(tupla1)) # 3
```

### Acceder a elementos

Se puede acceder a los elementos por su índice, como en una lista.

```python
print(tupla1[1])  # banana
```

### Modificar una tupla (usando _type-casting_)

Aunque no se pueden modificar directamente, se puede convertir a lista, modificar y volver a convertir a tupla.

```python
t = ("a", "b", "c")
lista = list(t)
lista[1] = "x"
t = tuple(lista)
print(t)  # ('a', 'x', 'c')
```

> [!NOTE]
> Esto se realiza en casos específicos donde el uso de una tupla es preferible sobre una lista y la modificación es poco frecuente.

### Eliminar una tupla

Para eliminar una tupla completamente, se utiliza la palabra reservada `del`.

```python
del tupla1
```

> [!IMPORTANT]
> `del` también funciona con listas, diccionarios y variables.

### Unir tuplas

Las tuplas pueden unirse utilizando el operador `+`.

```python
tupla3 = tupla1 + tupla2
```

### Métodos de tuplas

- `count()`: cuenta cuántas veces aparece un elemento específico.
- `index()`: devuelve el índice de la primera aparición de un elemento.

```python
t = ("a", "b", "a")
print(t.count("a"))  # 2
print(t.index("b"))  # 1
```

---

## Diccionarios

### ¿Qué es un diccionario?

Un diccionario es una colección de elementos que almacena datos en pares clave-valor.
Es útil cuando se desea relacionar una clave con un valor de forma eficiente.

```
diccionario = {clave1:valor1, clave2:valor2, ...}
```

### Cómo definir un diccionario

Los diccionarios pueden definirse utilizando claves `{}` o con el constructor `dict()`.

```python
d = {"nombre": "Ana", "edad": 25, "activo": True}
d2 = dict(nombre="Ana", edad=25)
```

> [!IMPORTANT]
> Observe que al utilizar el constructor, las claves no van entre comillas ("").

### Propiedades de los diccionarios

- No permiten claves duplicadas.
- Son mutables (se pueden modificar).
- Pueden almacenar datos de diferentes tipos.
- Se accede a los valores mediante las claves.

### Acceder y modificar elementos

Se accede mediante la clave y se pueden modificar los valores directamente.

```python
# Respecto al diccionario anterior
print(d["nombre"])
d["edad"] = 26
```

### Métodos útiles

- `keys()`: devuelve todas las claves del diccionario.
- `values()`: devuelve todos los valores.
- `items()`: devuelve pares clave-valor.

```python
print(d.keys())
print(d.values())
print(d.items())
```

### Agregar elementos

Se puede usar asignación o el método `update()`.

```python
d["curso"] = "Python" # Forma similar al acceder a un valor a partir de la clave "curso"
d.update({"pais": "Costa Rica"})
```

> [!NOTE]
> Observe que el método `.update()` y el acceso a partir de la clave con `[]` funciona tanto para agregar elementos como para modificar pares existentes.

### Eliminar elementos

Se pueden eliminar con `pop()`, `popitem()`, `del`, o vaciar el diccionario con `clear()`.

```python
d.pop("edad")
d.popitem()
del d["nombre"]
d.clear()
```

### Recorrer diccionarios

```python
# Los dos primeros tienen el mismo comportamiento
for clave in d:
    print(clave)

for clave in d.keys():
    print(clave)

# Imprimir valores
for valor in d.values():
    print(valor)

# Separar clave y valor con .items()
for clave, valor in d.items():
    print(clave, valor)
```

### Copiar un diccionario

Se utiliza el método `.copy()` para copiar los contenidos de un diccionario (similar a como se realiza en listas).

```python
copia = d.copy()
```

### Diccionarios anidados

Los diccionarios pueden contener otros diccionarios como valores.

```python
alumnos = {
    "Juan": {"edad": 15, "nota": 90},
    "Ana": {"edad": 16, "nota": 95}
}

print(alumnos["Juan"]["nota"]) # 90
```

### Resumen de métodos de diccionarios

| Método       | Descripción                                  |
|--------------|----------------------------------------------|
| `.keys()`    | Devuelve todas las claves                    |
| `.values()`  | Devuelve todos los valores                   |
| `.items()`   | Devuelve pares (clave, valor)                |
| `.get()`     | Devuelve el valor asociado a una clave       |
| `.update()`  | Agrega o actualiza elementos                 |
| `.pop()`     | Elimina un elemento con su clave             |
| `.popitem()` | Elimina el último par añadido                |
| `.clear()`   | Elimina todos los elementos                  |
| `.copy()`    | Devuelve una copia del diccionario           |

---

## Sets (Conjuntos)

### ¿Qué es un set?

Un set es una colección de elementos únicos, sin orden específico.
Es útil cuando se necesita asegurarse de que no haya duplicados en una colección de datos.

### Crear un set

Puede crearse con llaves `{}` o el constructor `set()`.

```python
s1 = {"a", "b", "c"}
s2 = set([1, 2, 3]) # A partir de una lista, por ejemplo.
```

### Propiedades de los sets

- No tienen orden: no se puede acceder a elementos por índice.
- No permiten elementos duplicados.
- Son mutables: se pueden agregar y eliminar elementos.
- True y 1 se consideran iguales. Igual para False y 0.

### Verificar pertenencia

Se puede usar el operador `in`, similar a listas y otros tipos de estructuras de datos.

```python
"a" in s1  # True
```

### Agregar elementos

Existen los siguientes métodos para agregar elementos a un set:
- `.add()`: Agregar un elemento único.
- `.update()`: Agregar una estructura de datos al set (set, lista, tupla).

```python
s1.add("d")
s1.update(["e", "f"])
```

### Eliminar elementos

Python implementa los siguientes métodos para eliminar elementos de un set:
- `.discard()`: No lanza error si no existe un elemento.
- `.remove()`: Lanza error si no existe un elemento.
- `.pop()`: Elimina un elemento aleatorio del set (usualmente `.pop` elimina a partir de un índice, pero el set está desordenado).

```python
s1.discard("b")
s1.remove("a")
s1.pop()
```

### Operaciones entre sets

Los sets permiten operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.

- Union: Es una operación entre conjuntos que une los contenidos de todos los sets en cuestión.
- Intersección: Une los contenidos que comparten los sets de la operación.
- Diferencia: Elimina los contenidos compartidos entre el set comparado y el principal de la operación (guarda los que no comparten; es decir, la diferencia).
- Diferencia simétrica: Guarda los contenidos que no son compartidos entre todos los sets (la simetría viene porque se aplica la diferencia a todos los sets).

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))           # {1, 2, 3, 4, 5, 6}
print(A | B)

print(A.intersection(B))    # {3, 4}
print(A & B)

print(A.difference(B))      # {1, 2}
print(A - B)

print(A.symmetric_difference(B))  # {1, 2, 5, 6}
print(A ^ B)
```

La imagen a continuación sirve como una explicación visual de las operaciones anteriores:

<div align="center">
<p>
    <img src="images/operaciones_sets.jpg" width="500px" alt="Operaciones entre sets">
</p>
</div>

### Tabla resumen de métodos de sets

| Método                   | Descripción                                 |
|--------------------------|---------------------------------------------|
| `.add()`                 | Agrega un solo elemento                     |
| `.update()`              | Agrega múltiples elementos                  |
| `.discard()`             | Elimina un elemento si existe, sin error    |
| `.remove()`              | Elimina un elemento, lanza error si no existe |
| `.pop()`                 | Elimina un elemento aleatorio               |
| `.clear()`               | Elimina todos los elementos del set         |
| `.union()`               | Une dos sets                                |
| `.intersection()`        | Elementos comunes entre sets                |
| `.difference()`          | Elementos en uno pero no en el otro         |
| `.symmetric_difference()`| Elementos no comunes entre los sets         |

