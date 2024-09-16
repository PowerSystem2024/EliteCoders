//Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir
//el proceso hasta que se intrudusca un numero negativo

package Ciclos01;

//importamos la libreria 
import javax.swing.JOptionPane;


public class Ejercicio01 {
    
    public static void main(String[] args) {
   
        //definimos
        int numero,cuadrado;
       //Nos ofresera una ventena emergernte
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")) ;
        //Cuantdo sea mayor o igual a 0
        while (numero >= 0 ){
            //elevar el numero al cuadrado
            cuadrado=(int)Math.pow(numero, 2);
            //resultado
            System.out.println("El numero "+ numero+" elevado al cuadrado es: "+cuadrado);
            //pedir nuevamente
            numero=Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: " ));
       
        }
        //si es numero negativo entonces imprime esto
        System.out.println("El programa a finalizado por un numero negativo");    
        
        
        
        
    
    }
    
}