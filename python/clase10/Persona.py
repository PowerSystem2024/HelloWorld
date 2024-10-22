class Persona:
    
    contador_personas = 0 # variable de clase
    
    @classmethod
    def generar_siguiente_valor (cls):
        cls.contador_personas += 1
        return cls.contador_personas
    
    def __init__(self, nombre, edad):
        
        Persona.contador_personas += 1
        
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad
        
        # de esta manera, cada que se cree una instancia de Persona, es instancia tendra el numero del contador asociado
        
    def __str__(self):
        return f'Persona {self.id_persona}\n nombre: {self.nombre}\n edad: {self.edad}'  

persona1 = Persona('Juan', 25)
print(persona1)

persona2 = Persona('Pedro', 30)
print(persona2)

persona3 = Persona('Maria', 35)
print(persona3)

print(f'cantidad de personas {Persona.contador_personas}')

persona4 = Persona('Juan', 25)
print(persona4)
