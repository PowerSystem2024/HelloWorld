
class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

for i in range(3):
    
    i += 1
    
    base = int(input(f'ingrese la base del rectangulo numero {i}: '))
    altura = int(input(f'ingrese la altura del rectangulonumero {i}: '))
    
    obj_rectangulo = Rectangulo(base, altura)
    
    print(f'el objeto numero {i} tiene como atributos: ')
    print(f'base: {obj_rectangulo.base}')
    print(f'altura: {obj_rectangulo.altura}')
    print(f'area: {obj_rectangulo.calcular_area()}')