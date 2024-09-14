diccionarioNuevo = {
    'azul': 'blue',
    'rojo': 'red',
    'verde': 'green', 
    'amarillo': 'yellow'
}

print(diccionarioNuevo)

del (diccionarioNuevo['azul'])  # eliminar un valor
print(diccionarioNuevo)

diccionario2 = {   # los diccionarios pueden almacenar diferentes tipos de datos
    'joaquin': {
        'edad': 19,
        'altura': 170
    },
    'pepe': [
        29, 180
        ],
    'roberto': [
        39, 190
        ],
    }

print(diccionario2)