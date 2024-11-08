/*
Ejercicio 15: Leer 10 enteros ordenados crecientemente. Leer N y buscarlo en la 
tabla. Se debe mostrar la posición en que se encuentra. Si no está, indicarlo con
 un mensaje.
 */
package arreglos_ejercicio_15;

import java.util.Scanner;

public class Arreglos_Ejercicio_15 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        boolean creciente = true;
        int numero, numero2 = 0;
        
        
        System.out.println("Se llena primer arreglo: ");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.print((i+1)+") Ingresar un número: ");
                arreglo[i] = entrada.nextInt();
            }
            
            for (int i = 0; i < 9; i++) {
                if(arreglo[i] <= arreglo[i+1]){
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
        
        System.out.print("Ingresar número para buscar en el arreglo: ");
        numero = entrada.nextInt();
        
        boolean isFound = false;
        
        for (int i = 0; i < 10; i++) {
            if(arreglo[i] == numero){
                System.out.println("El número ingresado se encuentra en la posición: " + i);
                isFound = true;
            }
            else if(i == 9 && !isFound){
                System.out.println("El número ingresado no se encuentra en el arreglo.");
            }
        }
        
        System.out.println();
        
    }
}
