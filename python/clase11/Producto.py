class Producto:
    
    contador_productos = 0
    
    def __init__(self, nombre, precio):
        
        Producto.contador_productos += 1
        
        self._id_producto = Producto.contador_productos
        
        self._nombre = nombre
        self._precio = precio
    
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    
    def __str__(self):
        return f"Producto {self._id_producto}: {self._nombre} - {self._precio}"

if __name__ == "__main__":
    
    producto1 = Producto('camiseta', 100.00)
    print(producto1)
    
    producto2 = Producto('pantalon', 150.00)
    print(producto2)
