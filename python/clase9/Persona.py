
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        def __str__(self):
            return f'persona: {self.nombre} \n edad: {self.edad}'
        

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

empleado1 = Empleado("Juan", 30, 1000)

print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)