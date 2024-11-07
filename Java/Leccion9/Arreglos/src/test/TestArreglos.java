
package test;

public class TestArreglos {
    public static void main(String[] args) { // lado derec. instanciamos un bojeto de tipo object
        int edades[] = new int [3]; // el lado izq. declaramos la variable
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades[0]);
        edades[1] = 19;
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 23;
        System.out.println("edades 2 = " + edades[2]);
        
        //edades[3] = 7; // Fuera de rango, error en tiempo de ejecución
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos "+i+": "+edades[i]);
            
        }
        
    }
}