class MiClase:
    
    variableDeClase = 'esta es una variable de clase'
    
    def __init__(self, variablesInstancia):
        self.variablesInstancia = variablesInstancia
    
    @staticmethod # un metodo estatico es un metodo que se relaciona con la clase, no con una instancia de la misma, es decir, no necesita una instancia para funcionar
    def metodo_estatico():
        print(MiClase.variableDeClase)
    
    @classmethod # el metodo de clase hace referencia a la clase, por eso no recibe self (que es la instancia de la clase), sino cls (que es la clase misma)
    def metodo_clase(cls):
        print(cls.variableDeClase)
    
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variableDeClase)
        print(self.variablesInstancia)
    
print(MiClase.variableDeClase)

miClase1 = MiClase('esta es una variable de instancia')
print(miClase1.variablesInstancia)

miClase1.variable_clase2 = 'valor de la variables de clase 2'

print(miClase1.variableDeClase)
print(miClase1.variable_clase2)

MiClase.metodo_estatico()
MiClase.metodo_clase()

miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodo_clase()

miObjeto1.metodo_instancia()