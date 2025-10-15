"""
f(n) = f(n-1) + 2*f(n-2)
f(0) = 1
f(1) = 2
"""

def f(n):
    # Casos base
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return f(n-1) + 2 * f(n-2)

print(f(10))

