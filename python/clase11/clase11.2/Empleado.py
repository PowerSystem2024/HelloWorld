class Empleado:
    
    def __init__(self, nombre, sueldo):
        
        self.nomre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        
        return f'Empleado {self.nomre} con sueldo de {self.sueldo}'