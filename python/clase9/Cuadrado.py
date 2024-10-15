from color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, color):
        FiguraGeometrica.__init__(self, alto, alto)
        Color.__init__(self, color)
    
    def clacular_area(self):   
        return self.alto * self.alto