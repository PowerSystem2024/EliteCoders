
package Operaciones;

/**
 *
 * @author Matias
 */
public class PruebaAritmetica {
    public static void main(String[] args) {
        int a=10;//variable locar
        int b=7;//Memoria stack
        miMetodo();//llamamos al nuevo metodo
        Aritmrtica aritmetica1=new Aritmrtica();
        aritmetica1.a=3;
        aritmetica1.b=7;
        aritmetica1.sumarNumero();
        //Para almecenar un objeto o los atributos se utiliza la memoria heap
        int resultado= aritmetica1.sumarConRetorno();
        System.out.println("Resultado: "+resultado);
    
        resultado= aritmetica1.sumarArgumentos(11, 6);
        System.out.println("Resultado usando argumentos: "+resultado);
        
        System.out.println("Aritmetica1 a: "+aritmetica1.a);
        System.out.println("Aritmetica2 a: "+aritmetica1.b);
        
         Aritmrtica aritmetica2=new Aritmrtica(5,8);
         System.out.println("Aritmetica1 a: "+aritmetica1.a);
         System.out.println("Aritmetica2 a: "+aritmetica1.b);
         //nunca utilizar esto no se debe hacer
         aritmetica1=null;
         System.gc();//sirve para limpiar residuos, es pesado, no utilizar
         Persona persona = new Persona("Ariel", "Betancud");
         System.out.println("persona = " + persona);
         System.out.println("Persona nombre: "+persona.nombre);
         System.out.println("Persona apellido: "+persona.apellido);
    }

        //Modularidad creamos un nuevo metodo
    public static void miMetodo(){
        int a =10;
        System.out.println("Aqui hay ptrp metodo");
        
    }
}
//Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona (String nombre, String apellido){ //Constructor
        super(); //constructor de la clase padre Object- no necesita argumentos
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
        
    }
}

class Imprimir{
    public Imprimir(){
        super(); //el constructor de la clase padre, para resrvar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
}