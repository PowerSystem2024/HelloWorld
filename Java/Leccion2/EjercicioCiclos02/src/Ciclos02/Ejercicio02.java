/*
Ejercicio 2: Leer un número e indicar si es positivo o
negativo. El proceso se repetira hasta que se introduzca
un cero 0
Hacer este ejercicio con la clase Scanner,
luego hacerlo nuevamente con la clase JOptionPane
 */
package Ciclos02;

import java.util.Scanner;


public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite un número: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero > 0){
                System.out.println("El número "+ numero + " es POSITIVO");
            }
            else{
                System.out.println("El número "+ numero + " es NEGATIVO");
            }
            System.out.print("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El número " + numero + " finaliza el programa");
    }
}
