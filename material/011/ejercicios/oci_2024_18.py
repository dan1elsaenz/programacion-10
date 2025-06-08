
def foo(n):
    if n <= 2:
        return 1
    return foo(n - 1) + foo(n - 3) + 1

result = foo(12)
print(result)

