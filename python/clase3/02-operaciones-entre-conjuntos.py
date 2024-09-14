# repaso de set o conjunto
# para definir un conjunto

conjunto2 = set()
conjunto1 = {"bye", }

conjunto2.add(7)
conjunto2.add("hola")

print(conjunto2)

conjunto1.add("hola")

print(conjunto1)

print(3 not in conjunto1) # preguntar si el numero 3 NO esta en el conjunto1

print(conjunto2 == conjunto1) # igualdad entre conjuntos, respuesta booleana

# operaciones entre conjuntos

conjunto3 = conjunto1 | conjunto2 # suma de conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # elementos en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1 # asigna el valor que esta en el conjunto2 y no en el conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # asigna el valor que esta en el conjunto y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # preguntar si un conjunto es sub-conjunto de otro
print(conjunto1.issubset(conjunto3)) # preguntar si un conjunto es sub-conjunto de otro
print(conjunto3.issubset(conjunto1)) # preguntar si un conjunto es sub-conjunto de otro
print(conjunto3.issubset(conjunto2)) # preguntar si un conjunto es sub-conjunto de otro

print(conjunto3.issuperset(conjunto1)) # preguntar si los elementos de un conjunto estan dentro de otro conjunto
print(conjunto3.issuperset(conjunto2)) # preguntar si los elementos de un conjunto estan dentro de otro conjunto
print(conjunto2.issuperset(conjunto3)) # preguntar si los elementos de un conjunto estan dentro de otro conjunto

print(conjunto1.isdisjoint(conjunto2)) # saber si dos conjuntos son disconexos (que no comparten elementos en comun)

conjunto1 = frozenset # hacer que un conjunto sea inmutable