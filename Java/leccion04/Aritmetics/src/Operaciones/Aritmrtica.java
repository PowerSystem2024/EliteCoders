
package Operaciones;

/**
 *
 * @author Matias
 */
public class Aritmrtica {
    int a ;
    int b ;
    
     //El contrucctor es un metodo especial
    public  Aritmrtica(){//contructor vacio
        System.out.println("Se esta ejecutano el constructor 1");
    }
    //Sobre carga de contructores
    public Aritmrtica(int a,int b){//contructor 2
            this.a=a;
            this.b=b;
            System.out.println("Se esta ejecutano el constructor 2");
    }
    //Metodo
    public void sumarNumero(){
        int resultado= a + b ;
        System.out.println("Resultado: "+resultado);
    
    
    }
    
    public int sumarConRetorno(){
        //int resultado= a + b;
        return a + b;
    }
    public int sumarArgumentos(int arg1, int arg2){
        this.a = arg1;
        this.b = arg2;
       return  a + b;
       
        
   }
}
