
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1 = "+ persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        // Modificar a través de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; // Ya no se puede utilizar
        //System.out.println("(Nombre es: " + persona1.nombre); //Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("person1 para obtener el booleano: "+persona1.isEliminado());
        
        // Tarea: Crear otro objeto tipo Persona, asignar valores de manera inicial
        // e imprimir, luego modificar sus valores y volver a imprimir
        Persona persona2 = new Persona("Sebastián", 100000, true);
        System.out.println("persona2 con su nombre: "+persona2.getNombre()+", sueldo: "+persona2.getSueldo()+", y su booleano: "+persona2.isEliminado());
        persona2.setNombre("Seba");
        persona2.setSueldo(500);
        persona2.setEliminado(false);        
        System.out.println("persona2 modificado con su nombre: "+persona2.getNombre()+", sueldo: "+persona2.getSueldo()+", y su booleano: "+persona2.isEliminado());
        
        System.out.println("persona1 = "+ persona1);
        
    }
}
