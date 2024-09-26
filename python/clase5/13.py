def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

res = factorial(5)

print(f"el factorial de 5 es {res}")