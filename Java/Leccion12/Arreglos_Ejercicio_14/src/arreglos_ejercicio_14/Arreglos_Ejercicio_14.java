/*
Ejercicio 14: Leer dos series de 10 enteros, que estarán ordenados crecientemente.
Copiar (fusionar) las dos tablas en una tercera, de forma que sigan ordenados.
 */
package arreglos_ejercicio_14;

import java.util.Scanner;

public class Arreglos_Ejercicio_14 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int a[] = new int[10];
        int b[] = new int[10];
        int c[] = new int[20];
        boolean creciente = true;
        
        System.out.println("Se llena primer arreglo: ");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.print((i+1)+") Ingresar un número: ");
                a[i] = entrada.nextInt();
            }
            
            for (int i = 0; i < 9; i++) {
                if(a[i] <= a[i+1]){
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
        
        System.out.println("Se llena segundo arreglo: ");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.print((i+1)+") Ingresar un número: ");
                b[i] = entrada.nextInt();
            }
            
            for (int i = 0; i < 9; i++) {
                if(b[i] <= b[i+1]){
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
        
        int i = 0;
        int j = 0;
        int k = 0;
        while(i < 10 && j < 10){
            if(a[i] < b[j]){
                c[k] = a[i];
                i++;
            }
            else{
                c[k] = b[j];
                j++;
            }
            k++;
        }
        
        if(i == 10){
            while(j < 10){
                c[k] = b[j];
                j++;
                k++;
            }
        }
        else{
            while(i < 10){
                c[k] = a[i];
                i++;
                k++;
            }
        }
        
        System.out.print("Arreglo Final: ");
        for (int l = 0; l < 20; l++) {
            System.out.print(c[l] + " ");
        }
        
        System.out.println();
        
    }
}
