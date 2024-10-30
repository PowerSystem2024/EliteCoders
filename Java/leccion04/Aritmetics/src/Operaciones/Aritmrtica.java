
package Operaciones;

/**
 *
 * @author Matias
 */
public class Aritmrtica {
    int a ;
    int b ;
    
    //El constructor es un metodo especial
    public Aritmrtica(){//Constructor 1
        System.out.println("Se está ejecutando ete constructor número uno");
    }
    
    //Estamos viendo lo que se llama sobrecarga de cosntructores
    public Aritmrtica(int a, int b){//Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando ete constructor número dos");
        
    }
    
    //Metodo
    public  void  sumarNumero(){
        int resultado= a + b ;
        System.out.println("Resultado: "+resultado);
    
    
    }
    
        // Método sin argumentos, retorna un valor fijo.
    public int sumarConRetorno() {
        int a = 5;
        int b = 3;
        return a + b;
    }

    // Método con argumentos.
    public int sumarArgumentos(int a, int b) {
        return a + b;
    }
}
    
    

