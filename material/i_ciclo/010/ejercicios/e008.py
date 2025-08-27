"""
Implementación de una pila

push() to insert an element into the stack
pop() to remove an element from the stack
top() Returns the top element of the stack.
isEmpty() returns true if stack is empty else false.
"""

def push(pila, valor):
    pila.append(valor)

def pop(pila):
    if isEmpty(pila):
        return None
    ultimo = pila.pop()
    return ultimo

def top(pila):
    if isEmpty(pila):
        return None
    return pila[-1]

def isEmpty(pila):
    if len(pila) == 0:
        return True
    return False

# Declaración de pila
pila = []

print(top(pila))
push(pila, 10)
push(pila, 8)
push(pila, 3)
push(pila, 4)
push(pila, 7)
print(pop(pila))
print(top(pila))
print(isEmpty(pila))

