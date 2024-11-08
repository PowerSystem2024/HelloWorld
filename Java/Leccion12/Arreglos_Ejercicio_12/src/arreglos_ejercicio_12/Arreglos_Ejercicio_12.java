/*
Ejercicio 12: Leer por teclado una tabla de 10 elementos numéricos enteros y
una posición (entre 0 y 9). Eliminar el elemento situado en la posición dada
sin dejar huecos
 */
package arreglos_ejercicio_12;

import java.util.Scanner;

public class Arreglos_Ejercicio_12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        int posicion, j = 0;
        
        System.out.println("Se llena arreglo: ");
        for (int i = 0; i < 10; i++) {
            System.out.print((i+1)+") Ingresar un número: ");
            arreglo[i] = entrada.nextInt();
        }
        
        System.out.println();
        
        do{
            System.out.print("Ingresar posición a eliminar entre 0 y 9: ");
            posicion = entrada.nextInt();
        }while (posicion < 0 || posicion > 9);
        
        for (int i = posicion; i < 9; i++) {
            arreglo[i] = arreglo[i+1];
        }
        
        System.out.print("\nArreglo Final: ");
        for (int i = 0; i < 9; i++) {
            System.out.print(arreglo[i] + " ");
        }
        
        System.out.println();
        
    }
}
