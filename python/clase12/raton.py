from dispositivo_entrada import *

class Raton(DispositivoEntrada):
    
    contador_ratones = 0
    
    def __init__(self, marca, tipo_entrada):
        
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones 
        
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        
        return f'id : {self._id_raton}\nmarca : {self._marca}\ntipo entrada : {self._tipo_entrada}'

if __name__ == '__main__':
    
    raton1 = Raton('HP', 'USB')
    print(raton1)
    
    raton2 = Raton('Acer', 'Bluetooth')
    print(raton2)