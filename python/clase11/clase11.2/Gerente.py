from Empleado import Empleado

class Gerente(Empleado):    
    
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        
        self.departamento = departamento
    
    def __str__(self):
        
        return f'Gerente {self.nomre} con sueldo de {self.sueldo} y departamento {self.departamento}'
        