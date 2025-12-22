def f1(a, b):
    return f2(a, b) * f2(b, a)
def f2(a, b):
    return 7 * a + 5 * b
def f3(a, b):
    return f1(a + 2, b + 2) * 2 + 4 * a + b

print(f3(11,17))

