class Monitor:
    
    contador_monitores   = 0
    
    def __init__(self, marca, tamaño):
        
        Monitor.contador_monitores += 1
        
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño
        
    def __str__(self):
        
        return f'id : {self._id_monitor}\nmarca: {self._marca}\ntamaño : {self._tamaño}\n' 

if __name__ == '__main__':
    
    monitor1 = Monitor('HP', '20 pulagadas')
    print(monitor1)

    
    monitor2 = Monitor('Acer', '20 pulagadas')            
    print(monitor2)
