/*
Ejercicio 4: Leer 10 números enteros, guardarlos en un arreglo.
debemos mostrarlos en el siguiente orden: el primero, el último, 
el segundo, el penúltimo, el tercero, etc.
 */
package arreglos_ejercicio_4;

import java.util.Scanner;

public class Arreglos_Ejercicio_4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int[10];
        
        for (int i = 0; i < 10; i++) {
            System.out.print((i+1)+") Ingresar un número: ");
            numeros[i] = entrada.nextInt();
        }
        
        System.out.print("El resultado es: ");
        for (int i = 0; i < 5; i++) {
            System.out.print(numeros[i] + " ");
            System.out.print(numeros[9-i] + " ");
        }
        
        System.out.println();
    }
}
