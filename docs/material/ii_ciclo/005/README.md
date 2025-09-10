# Clase 5: Polimorfismo, decoradores y sobrecarga de operadores

En esta clase, se van a estudiar los conceptos de polimorfismo en la OOP, el uso de decoradores `@staticmethod` y `@classmethod` en la definición de métodos y finalmente, la sobrecarga de operadores.

## Polimorfismo y redefinición de métodos

La **programación orientada a objetos (POO)** permite que diferentes clases puedan **compartir el mismo nombre de método**, pero con un comportamiento adaptado a cada una.
A esto se le conoce como **polimorfismo**.

!!! info "Definición"

    El **polimorfismo** es la capacidad que tienen los objetos de diferentes clases de responder de manera distinta a la **misma llamada de método**.

### Redefinición de Métodos

Cuando una clase hija **hereda** de una clase padre, puede **redefinir (sobrescribir)** un método para adaptarlo a su propio comportamiento.  
Esto se logra simplemente **volviendo a declarar el método** en la subclase, como se ha visto anteriormente.

=== "Ejemplo"

    ```python
    class Animal:
        def hacer_sonido(self):
            return "Sonido genérico"

    class Perro(Animal):
        def hacer_sonido(self):   # (1)!
            return "Guau"

    class Gato(Animal):
        def hacer_sonido(self):   # (2)!
            return "Miau"

    # Demostración de polimorfismo
    animales = [Perro(), Gato(), Animal()]
    for animal in animales:
        print(animal.hacer_sonido())
    ```

    1. Redefinición del método.
    2. Redefinición del método.

=== "Salida esperada"

    ```text
    Guau             # (1)!
    Miau             # (2)!
    Sonido genérico  # (3)!
    ```

    1. Para la instancia de `Perro`.
    2. Para la instancia de `Gato`.
    3. Para la instancia de `Animal`.

1. `Animal` define un método genérico `hacer_sonido()`.
2. `Perro` y `Gato` heredan de `Animal`, pero redefinen (`override`) el método.
3. Cuando recorremos la lista `animales`, **cada objeto ejecuta su propia versión del método**.

!!! tip "Ventaja del polimorfismo"

    Permite **escribir código genérico** que funciona con múltiples tipos de objetos, sin necesidad de conocer de antemano la clase exacta.

### Ejemplo: Polimorfismo en una jerarquía de figuras

=== "Ejemplo"

    ```python
    class Figura:
        def area(self):  # (1)!
            raise NotImplementedError("Este método debe ser redefinido en la subclase")

    class Rectangulo(Figura):
        def __init__(self, base, altura):
            self.base = base
            self.altura = altura

        def area(self):   # (2)!
            return self.base * self.altura

    class Circulo(Figura):
        def __init__(self, radio):
            self.radio = radio

        def area(self):   # (3)!
            return 3.14 * self.radio ** 2

    figuras = [Rectangulo(4, 5), Circulo(3)] # (4)!
    for f in figuras:
        print(f"Área: {f.area()}")
    ```

    1. Clase abstracta: No se va a cubrir específicamente.
    2. Redefinición del área para un rectángulo.
    3. Redefinición del área para un círculo.
    4. Se aplica el método a las instancias de la lista.

=== "Salida esperada"

    ```text
    Área: 20
    Área: 28.26
    ```

!!! note "Observación"

    Cada subclase (`Rectangulo`, `Circulo`) redefine el método `.area()` de forma diferente.
    Gracias al polimorfismo, se recorre una lista heterogénea de figuras y **se tratan a todas por igual**.

---

## Decoradores en clases: `@staticmethod` y `@classmethod`

En Python, los **decoradores en clases** permiten cambiar la forma en que se comportan los métodos.  
Ya se cubrieron `@property` y `@setter`, ahora se va a enfocar en:

- `@staticmethod`
- `@classmethod`

### `@staticmethod`

Un **método estático** es aquel que **no recibe ni `self` ni `cls`** como primer argumento.  
Es útil cuando se necesita una función **relacionada con la clase**, pero que **no depende de la instancia ni de la clase** en sí.

```python title="Ejemplo de método estático"
class Calculadora:
    @staticmethod  # (1)!
    def suma(a, b):
        return a + b

# Se puede llamar sin crear un objeto
print(Calculara.suma(5, 3))  # (2)!

# También funciona desde una instancia
m = Matematica()
print(m.suma(10, 7))  # (3)!
```

1. Método estático asociado a la clase.
2. `8`
3. `17`

!!! tip "Uso típico"

    Se emplea para **métodos utilitarios** o **funciones auxiliares** que tienen sentido en la clase, pero que **no dependen de sus atributos**.

### `@classmethod`

Un **método de clase** recibe la clase como primer parámetro (en lugar de `self`), normalmente llamado `cls`.  
Se usa cuando el método necesita **acceder o modificar atributos compartidos por todas las instancias**.

=== "Ejemplo"

    ```python
    class Persona:
        cantidad = 0  # (1)!

        def __init__(self, nombre): # (2)!
            self.nombre = nombre
            Persona.cantidad += 1   # (3)!

        @classmethod
        def contar_personas(cls):   # (4)!
            return f"Se han creado {cls.cantidad} personas."  # (5)!

    # Crear instancias
    p1 = Persona("Ana")
    p2 = Persona("Luis")

    # Llamar al método de clase
    print(Persona.contar_personas())
    ```

    1. Atributo de clase: fuera del `__init__`.
    2. Definición de atributos de instancia.
    3. Se incrementa `cantidad` (atributo de clase).
    4. Método de clase recibe `cls` como primer parámetro.
    5. Imprime el atributo de clase.

=== "Salida esperada"

    ```text
    Se han creado 2 personas.
    ```

!!! note "Diferencia con métodos estáticos"

    - Método de instancia: recibe `self` y puede acceder a los atributos de instancia.
    - `@staticmethod`: **no recibe** ni `self` ni `cls`, está agrupado con la clase pero no puede acceder a atributos.
    - `@classmethod`: recibe **la clase (`cls`)** como primer parámetro, puede acceder/modificar los atributos de clase.

### Ejemplo de `@staticmethod` y `@classmethod`

```python title="Implementación de métodos de estáticos y de clase en Producto"
class Producto:
    tasa_impuesto = 0.13                  # (1)!

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @staticmethod
    def es_valido(precio):                # (2)!
        """Un precio es válido si es positivo"""
        return precio > 0

    @classmethod
    def cambiar_impuesto(cls, nuevo):     # (3)!
        cls.tasa_impuesto = nuevo

    def precio_final(self):
        return self.precio * (1 + Producto.tasa_impuesto)

# Uso
print(Producto.es_valido(50))     # (4)!
print(Producto.es_valido(-20))    # (5)!

p1 = Producto("Camisa", 10000)
print(p1.precio_final())          # (6)!

Producto.cambiar_impuesto(0.2)
print(p1.precio_final())          # (7)!
```

1. Atributo de clase: Compartido por todas las instancias de la clase.
2. No recibe ni `self` ni `cls`.
3. Modifica el atributo de clase. Puede llamarse sin necesidad de existir una instancia (con la clase propiamente).
4. True
5. False
6. `11300.0`
7. `12000.0`

---

## Sobrecarga de Operadores en Clases Personalizadas

En Python, las clases pueden **definir cómo deben comportarse los operadores** (`+`, `-`, `==`, entre otros) cuando se aplican a sus objetos.
Esto se logra implementando **métodos especiales**.

!!! info "Definición"

    La **sobrecarga de operadores** consiste en redefinir los operadores para que funcionen con **objetos creados por el usuario**, haciendo el código más natural y legible.

### Métodos comunes

| Operador | Método especial | Uso                             |
| -------- | --------------- | ------------------------------- |
| `+`      | `__add__`       | Suma de objetos                 |
| `-`      | `__sub__`       | Resta de objetos                |
| `==`     | `__eq__`        | Comparación de igualdad         |
| `str()`  | `__str__`       | Representación en texto legible |
| `len()`  | `__len__`       | Longitud de un objeto           |

### Ejemplo: Clase `Vector`

```python title="Sobrecarga de operadores en clase Vector"
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Uso de la clase
v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2     # (1)!
print(v3)        # (2)!
print(v1 == v2)  # (3)!
```

1. Llama a `__add__`
2. Llama a `__str__`: `(7, 10)`
3. Llama a `__eq__`: `False`

!!! tip "Ventaja"

    Gracias a la sobrecarga de operadores, podemos trabajar con objetos de manera **intuitiva y expresiva**, en lugar de definir métodos como `sumar(v1, v2)`.

### Ejemplo: Clase `Fraccion`

```python title="Sobrecarga de operadores en clase Fraccion"
from math import gcd

class Fraccion:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("El denominador no puede ser cero")
        self.num = num
        self.den = den
        self.simplificar()

    def simplificar(self):
        divisor = gcd(self.num, self.den) # Máximo común divisor
        self.num //= divisor
        self.den //= divisor

    def __add__(self, other):
        nuevo_num = self.num * other.den + other.num * self.den
        nuevo_den = self.den * other.den
        return Fraccion(nuevo_num, nuevo_den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __str__(self):
        return f"{self.num}/{self.den}"

# Uso
f1 = Fraccion(1, 2)
f2 = Fraccion(1, 3)
print(f1 + f2)     # (1)!
print(f1 == f2)    # (2)!
```

1. `5/6`
2. `False`

---
