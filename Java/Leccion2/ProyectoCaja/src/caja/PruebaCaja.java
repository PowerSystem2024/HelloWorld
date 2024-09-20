/*
Proyecto caja:
Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
La fórmula es: volumen = ancho * alto * profundidad
 */
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        int x = 7;
        int y = 15;
        int z = 20;
        
        Caja box1 = new Caja();
        box1.ancho = x;
        box1.alto = y;
        box1.profundidad = z;
        int volumen = box1.calcularVolumen();
        
        System.out.println("El volumen de box1 = " + volumen);
        
        Caja box2 = new Caja(5, 5, 4);
        System.out.println("El volumen de box2 = " + box2.calcularVolumen());
        
    }
}
