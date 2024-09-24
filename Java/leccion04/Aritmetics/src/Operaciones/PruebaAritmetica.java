
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
         System.gc();//sirve para limpiar residuos, es peddo, no utilizar
    }

    public static void miMetodo(){
        int a =10;
        System.out.println("Aqui hay ptrp metodo");
        
    }
}
