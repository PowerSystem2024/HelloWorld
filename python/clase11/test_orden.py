from Producto import Producto
from Orden import Orden

producto1 = Producto('camiseta', 100.00)
producto2 = Producto('pantalon', 150.00)
producto3 = Producto('remera', 150.00)
producto4 = Producto('zapatillas', 150.00)
producto5 = Producto('campera', 150.00)
producto6 = Producto('sweater', 150.00)
producto7 = Producto('mochila', 150.00)

productos1 = [producto1, producto2]

orden1 = Orden(productos1)
print(f'total de la primera orden: {orden1.calcular_total()}')
print(orden1)

productos2 = [producto3, producto4, producto5, producto6, producto7]

orden2 = Orden(productos2)
print(f'total de la segunda orden: {orden2.calcular_total()}')
print(orden2)
