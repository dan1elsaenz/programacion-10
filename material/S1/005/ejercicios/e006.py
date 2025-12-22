"""
Ejercicio 6: Reemplazar vocales en una palabra  

Escribe un programa que reemplace todas las vocales de una palabra por un asterisco `*`.  

```
Entrada: "programación"  
Salida: "pr*gr*m*c**n"
```
"""

# Lista inicial
lista = ["hola", "elefante", "mundo", "estrella"] 
nueva_lista = []

# Alternativa si quieren utilizar input()
# lista = input("Ingrese las palabras separadas por un espacio: ").split()

# Método 1: como iterador
# Recorrer lista
for palabra in lista:
    # Largo de la palabra mayor que 0
    if len(palabra) > 5:
        # Convertir a mayúscula
        nueva_lista.append(palabra.upper())
    else:
        # Agregar la palabra normal
        nueva_lista.append(palabra)

# Mostrar lista resultante
print(nueva_lista)

# Método 2: por índice
for i in range(len(lista)):
    # Modificar el índice de la lista
    if len(lista[i]) > 5:
        lista[i] = lista[i].upper()

# Imprimir el resultado
print(lista)



