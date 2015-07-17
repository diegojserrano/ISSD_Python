def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


v2 = [fibonacci(x) for x in range(10)]

for a in v2:
    print(a)

