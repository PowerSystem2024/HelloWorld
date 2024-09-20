
package caja;

public class Caja {
    // Atributos de la clase
    int ancho;
    int alto;
    int profundidad;
    
    // Constructores
   public Caja(){  
   }
    
   public Caja(int ancho, int alto, int profundidad){
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

   // Métodos
   public int calcularVolumen(){
        return ancho*alto*profundidad;
   }  
}
