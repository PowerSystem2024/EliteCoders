package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;

    //El constructor de una clase especial
    public Aritmetica(){//Constructor 1
        System.out.println("Se esta ejecutando este constructor numero 1");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){//Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero 2");
    }

    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    }

    public int sumaConArgumentos(int a, int b){
        this.a = a;
        this.b = b;
        //return a + b;
        return this.sumarConRetorno();
    }
}
