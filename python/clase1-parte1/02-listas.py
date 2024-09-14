nombres = ['naty', 'osvaldo', 'lil', 'ariel']

print(nombres)
print(nombres[0:2]) # muestra desde el indice 0 al 2
print(nombres[:3]) # muestra desde el indice 0 al 3
print(nombres[1:]) # muestra desde el indice indicado al final

nombres[2] = 'liliana' # modificar un valor
print(nombres)

# iterar una lista

for nombre in nombres:
    print(nombre)
else:
    print('se acabaron los elementos de la lista')