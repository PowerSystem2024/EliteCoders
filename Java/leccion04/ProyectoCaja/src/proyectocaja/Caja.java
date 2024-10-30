
package proyectocaja;

/**
 *
 * @author Matias
 */
public class Caja {//Clase publica
    //Atributos (caracteristicas
    int ancho;
    int alto;
    int profundo;
    //Metodos y contructores (acciones)
    public Caja(){//contructor 1=vacio
        
    }
    //Contructor con parametros
    public  Caja(int ancho,int  alto,int profundo){//Contructor 2
        this.ancho=ancho;
        this.alto=alto;
        this.profundo=profundo;
        
    }
    public  int calcularVolumen(){//Metodo para calcualar
        return  alto*ancho*profundo;
    }
}
