/*
Ejercicio 11: Leer 5 elementos numéricos que se introducirán ordenados de forma
creciente. Estos los guardaremos en una tabla de tamaño 10. Leer un número N,
e insertarlo en el lugar adecuado para que la tabla continúe ordenada.
 */
package arreglos_ejercicio_11;

import java.util.Scanner;

public class Arreglos_Ejercicio_11 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        boolean creciente = true;
        int numero, sitio_num = 0, j = 0;
        
        System.out.println("Se llena el arreglo: ");
        do{
            for (int i = 0; i < 5; i++) {
                System.out.print((i+1)+") Ingresar un número: ");
                arreglo[i] = entrada.nextInt();
            }
            
            for (int i = 0; i < 4; i++) {
                if(arreglo[i] < arreglo[i+1]){
                    creciente = true;
                }
                else{
                    creciente = false;
                    break;
                }
            }
            
            if(!creciente){
                System.out.println("\nEl arreglo no está ordenado de forma creciente. Intente de nuevo.");
            }
            
        }while(!creciente);
        
        System.out.print("Ingresar número a insertar: ");
        numero = entrada.nextInt();
        
        while(arreglo[j] < numero && j < 5){
            sitio_num++;
            j++;
        }
        
        for (int i = 4; i >= sitio_num; i--) {
            arreglo[i+1] = arreglo[i];
        }
        
        arreglo[sitio_num] = numero;
        
        System.out.print("Arreglo Final: ");
        for (int i = 0; i < 6; i++) {
            System.out.print(arreglo[i] + " ");
        }
        
        System.out.println();
        
    }
}
