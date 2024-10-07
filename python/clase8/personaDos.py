class Persona2:
    
    def __init__(self, nombre, apellido, edad):
    
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    def mostrar_detalles(self):
        print(f'el nombre de la persona es {self._nombre} {self._apellido} y tiene {self._edad} años')

    @property
    def nombre(self):
        print('metodo getter')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('metodo setter')
        self._nombre = nombre
    
    @property
    def apellido(self):
        print('metodo getter')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('metodo setter')
        self._apellido = apellido
        
    @property
    def edad(self):
        print('metodo getter')
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('metodo setter')
        self._edad = edad
    
    def __del__(self):
        print(f'persona: {self._nombre}, {self._apellido}, {self._edad}')

persona1 = Persona2('joaquin', 'peralta', 19)
persona1.mostrar_detalles()

# tarea: crear tres objetos mas, utilizando los metodos getters y setters para modificar y mostrar los cambios con el metodo mostrar detalles

persona1.nombre = 'juan'
persona1.apellido = 'rodrigues'
persona1.edad = 23

persona1.mostrar_detalles()

persona1.nombre = 'pepe'
persona1.apellido = 'perez'
persona1.edad = 32

persona1.mostrar_detalles()

persona1.nombre = 'maria'
persona1.apellido = 'rosas'
persona1.edad = 89

persona1.mostrar_detalles()

print(__name__)

print('eliminar los objetos'.center(100, '-'))
