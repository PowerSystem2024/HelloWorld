diccionario = {
    'IDE': 'Integrated Development Environmet',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}

print(diccionario)
print(len(diccionario))
print(diccionario['IDE'])

diccionario['IDE'] = 'entorno de desarrollo integrado'

print(diccionario)

for termino in diccionario:
    print(termino)

for termino, valor in diccionario.items():
    print(termino + ": " + valor)

for termino in diccionario.keys():
    print(termino)

for termino in diccionario.values():
    print(termino)

print('IDE' in diccionario)

diccionario.pop('SABD')

print(diccionario)

diccionario.clear()
print(diccionario)

del diccionario
print(diccionario)
