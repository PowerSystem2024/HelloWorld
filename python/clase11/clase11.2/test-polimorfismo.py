from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objecto):
    print(objecto)

empleado = Empleado('joaquin', 1000)
imprimir_detalles(empleado)

gerente = Gerente('claudio', 2000, 'sistemas')
imprimir_detalles(gerente)