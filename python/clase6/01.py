class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}')

print(type(Persona))
print(Persona)

persona1 = Persona("matias", 'aguilera', '18')
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


persona2 = Persona("claudio", 'alvarez', '23')
print(f'nombre: {persona2.nombre}, apellido: {persona2.apellido}, edad: {persona2.edad}')

persona3 = Persona("micaela", "gomila", 19)
persona3.mostrar_detalle()