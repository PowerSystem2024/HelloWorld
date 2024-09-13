cocina = ('cuchara', 'cuchillo', 'tenedor')

print(len(cocina))

print(cocina[1])

print(cocina[-1])

print(cocina[0:1])

for cocinar in cocina:
    print(cocinar, end = " ")

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print(cocina)