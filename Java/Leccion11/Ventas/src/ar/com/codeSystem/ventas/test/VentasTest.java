
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        
        Orden orden1 = new Orden();
        // Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        // Tarea:
        // Crear más objetos de tipo Producto = 10
        Producto producto3 = new Producto("Pulsera", 900.00);
        Producto producto4 = new Producto("Remera", 7900.00);
        Producto producto5 = new Producto("Zapatillas", 34900.00);
        Producto producto6 = new Producto("Gorra", 3900.00);
        Producto producto7 = new Producto("Buzo", 17900.00);
        Producto producto8 = new Producto("Camisa", 12900.00);
        Producto producto9 = new Producto("Cinturón", 2500.00);
        Producto producto10 = new Producto("Chaleco", 21900.00);
        Producto producto11 = new Producto("Bufanda", 4500.00);
        Producto producto12 = new Producto("Guantes", 3200.00);
        
        // Crear más objetos de tipo Orden = 2
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto1);
        orden2.agregarProducto(producto2);
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto12);
        orden3.mostrarOrden();
        
    }
}
