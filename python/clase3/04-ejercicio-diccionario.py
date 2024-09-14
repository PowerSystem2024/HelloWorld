seleccionArgentina = {
    10: {'nombre': 'Lionel Messi', 
        'edad': 35,
        'altura': 1.70,
        'precio': '50 millones',
        'posicion': 'extremo derecho'},
    11: {'nombre': 'Angel Di Maria',
        'edad': 34,
        'altura': 1.80,
        'precio': '12 millones',
        'posicion': 'extremo derecho'},
    24: {'nombre': 'Paulo Dybala',
        'edad': 28,
        'altura': 1.77,
        'precio': '35 millones',
        'posicion': 'media punta'},
    19: {'nombre': 'Nicolas Otamendi',
        'edad': 34,
        'altura': 1.83,
        'precio': '3.5 millones',
        'posicion': 'defensa central'},
    1: {'nombre': 'Franco Armani',
        'edad': 35,
        'altura': 1.89,
        'precio': '3.5 millones',
        'posicion': 'portero'},
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# agregar 4 jugadores mas

print('tenemos cargados en el diccionario la cantidad dejugadores: ', end = " ")
print(len(seleccionArgentina))