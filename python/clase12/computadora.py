class Computadora:
    
    contador_computadoras = 0
    
    def __init__(self, nombre, marca, monitor, teclado, raton):
        
        Computadora.contador_computadoras += 1
        
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._marca = marca
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    def __str__(self):
        
        return f'''
                id : {self._id_computadora}
                nombre : {self._nombre}
                marca : {self._marca}
                monitor : {self._monitor}
                teclado : {self._teclado}
                raton : {self._raton}
                '''

if __name__ == '__main__':
    
    computadora1 = Computadora('HP', 'HP', '20 pulagadas', 'USB', 'Bluetooth')
    print(computadora1)
    
    computadora2 = Computadora('Acer', 'Acer', '20 pulagadas', 'USB', 'Bluetooth')            
    print(computadora2)         