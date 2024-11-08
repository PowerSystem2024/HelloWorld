/*
Ejercicio 5: Leer por teclado dos tablas de 10 números
enteros y mezclarlas en una tercera de la forma: 1° de A,
1° de B, 2° de A, 2 de B, etc. 
 */
package arreglos_ejercicio_5;

import java.util.Scanner;


public class Arreglos_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros1[] = new int[10];
        int numeros2[] = new int[10];
        int numeros3[] = new int[20];
        
        System.out.println("Se llena el primer arreglo: ");
        for (int i = 0; i < 10; i++) {
            System.out.print((i+1)+") Ingresar un número: ");
            numeros1[i] = entrada.nextInt();
        }
        
        System.out.println("Se llena el segundo arreglo: ");
        for (int i = 0; i < 10; i++) {
            System.out.print((i+1)+") Ingresar un número: ");
            numeros2[i] = entrada.nextInt();
        }
        
        int j = 0;
        for (int i = 0; i < 10; i++) {
            numeros3[j] = numeros1[i];
            j++;
            numeros3[j] = numeros2[i];
            j++;
        }
        
        System.out.print("El tercer arreglo: ");
        for (int i = 0; i < 20; i++) {
            System.out.print(numeros3[i] + " ");
        }
        System.out.println();
    }
}
