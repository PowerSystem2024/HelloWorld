/*
Ejercicio 2: Leer 5 números, guardarlos en un arreglo y 
mostrarlos en el orden inverso al introducirlos.
 */
package arreglos_ejercicios_2;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        
        System.out.println("Guardando los datos del arreglo.");
        for (int i = 0; i < 5; i++) {
            System.out.print((i+1)+". Digite un número: ");
            numeros[i] = entrada.nextFloat();
        }
        
        System.out.println("\nImprimimos los elementos del arreglo.");
        for (int i = 4; i >= 0; i--) {
            System.out.print(numeros[i]+" ");
        }

        System.out.println("\n");
    }
}
