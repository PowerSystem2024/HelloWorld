
class Cubo:
    
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

    
ancho = int(input(f'ingrese el ancho del Cubo: '))
alto = int(input(f'ingrese el alto del Cubo: '))
profundidad = int(input(f'ingrese el volumen del Cubo: '))
    
obj_Cubo = Cubo(ancho, alto, profundidad)
    
print(f'el objeto tiene como atributos: ')
print(f'ancho: {obj_Cubo.ancho}')
print(f'alto: {obj_Cubo.alto}')
print(f'profundidad: {obj_Cubo.profundidad}')
print(f'volumen: {obj_Cubo.calcular_volumen()}')