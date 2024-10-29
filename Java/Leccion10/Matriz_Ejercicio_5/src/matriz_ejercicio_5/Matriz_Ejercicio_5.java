/*
Ejercicio 5: Crear y cargar una matriz de tamaño nxm, mostrar la suma de 
cada fila y de cada columna.
 */
package matriz_ejercicio_5;

import java.util.Scanner;

public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
                
        System.out.print("Ingresar número de filas: ");
        int n = entrada.nextInt();
        
        System.out.print("Ingresar número de columnas: ");
        int m = entrada.nextInt();
        
        int matriz [][] = new int [n][m];
        
        System.out.println();
        
        System.out.println("Rellenar la matriz: ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        
        System.out.println();
        
        System.out.println("Matriz Original: ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println();
        }
        
        System.out.println();
        
        // Calculo de la sumatoria de cada fila
        int sumFila = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sumFila += matriz[i][j];
                if (j == m - 1){
                    System.out.println("Sumatoria de fila["+i+"]: "+sumFila);
                    sumFila = 0;
                }
            }
        }
        
        System.out.println();

        // Calculo de la sumatoria de cada columna        
        int sumCol = 0;        
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++) {
                sumCol += matriz[i][j];
                if (i == n - 1){
                    System.out.println("Sumatoria de columna["+j+"]: "+sumCol);
                    sumCol = 0;
                }
            }
        }
        
        System.out.println();
        
    }
}
