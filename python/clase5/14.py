# imprimir una lista de numeros de forma descendente de forma recursiva

def recursivaDescendiente(n):
    if n == 1:
        print(1)
    else:
        print(n)
        recursivaDescendiente(n - 1)

recursivaDescendiente(5)