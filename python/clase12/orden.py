from computadora import *

class Orden:
    
    contador_ordenes = 0
    
    def __init__(self, computadores):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadores = computadores
        
    def agregar_computadoras(self, computadora):
        self._computadores.append(computadora)
    
    def __str__(self):
        computadora_str = ""
        for computadora in self._computadores:
            computadora_str += computadora.__str__() + "\n"
            
        return f'''
                Orden: {self._id_orden}
                Computadoras:
                {computadora_str}
                '''

if __name__ == '__main__':
    computadora1 = Computadora('HP', 'HP', '20 pulgadas', 'USB', 'Bluetooth')
    computadora2 = Computadora('Acer', 'Acer', '20 pulgadas', 'USB', 'Bluetooth')
    
    orden1 = Orden([computadora1, computadora2])
    orden1.agregar_computadoras(computadora1)
    orden1.agregar_computadoras(computadora2)
    print(orden1)
