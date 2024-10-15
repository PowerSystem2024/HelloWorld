'''
definir una clase padre llamada Vehiculo y dos clases hijas llamadas auto y bicicleta, las cuales heredan de la clase padre Vehiculo. la clase padre 
debe tener los siguientes atributos y metodos:

atributos: color, ruedas
metodos: __init__ y __str__

Auto(clase hija de Vehiculo):
atributos: velocidad en km/H
metodos: __init__ y __str__

Bicicleta(clase hija de Vehiculo):
atributos: tipo
metodos: __init__ y __str__

crear un objeto de cada clase   
'''

class Vehiculo:
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'color: {self.color} \n ruedas: {self.ruedas}'
    
class Auto(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f'color: {self.color} \n ruedas: {self.ruedas} \n velocidad: {self.velocidad}'

class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return f'color: {self.color} \n ruedas: {self.ruedas} \n tipo: {self.tipo}'

vehiculo1 = Vehiculo('rojo', 4)
print(vehiculo1)

auto1 = Auto('azul', 4, 100)
print(auto1)

bicicleta1 = Bicicleta('verde', 2, 'ciclista')
print(bicicleta1)   