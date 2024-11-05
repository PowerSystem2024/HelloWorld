from computadora import *
from orden import *
from monitor import *
from teclado import *
from raton import *

teclado1 = Teclado('HP', 'USB')
teclado2 = Teclado('Acer', 'Bluetooth')

raton1 = Raton('HP', 'USB')
raton2 = Raton('Acer', 'Bluetooth')

monitor1 = Monitor('HP', '20 pulgadas')
monitor2 = Monitor('Acer', '20 pulgadas')

computadora1 = Computadora('HP', 'HP', monitor1, teclado1, raton1)
computadora2 = Computadora('Acer', 'Acer', monitor2, teclado2, raton2)

orden1 = Orden([computadora1, computadora2])
orden1.agregar_computadoras(computadora1)
orden1.agregar_computadoras(computadora2)
orden1.agregar_computadoras(computadora1)
orden1.agregar_computadoras(computadora2)

orden2 = Orden([computadora1, computadora2])
orden2.agregar_computadoras(computadora1)
orden2.agregar_computadoras(computadora2)
orden2.agregar_computadoras(computadora1)
orden2.agregar_computadoras(computadora2)

print(orden1)            
print(orden2)