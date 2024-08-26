/*
Ejercicio 2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se ponga un cero 0
*/
package Ciclos01;
//Importo 
import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        //Pido al usuario que digite un numero
        var num=Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")) ;
         //Si es distinto de 0
        while (num != 0 ){
            
            JOptionPane.showInputDialog(null,"El numero es "+ num+ " por tanto sigue");
            System.out.println("El numero  "+ num+ " es positivo");
            System.out.println("Digite otro numero: ");
            
            num=Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        //si es igual a 0 imprimo esto
        JOptionPane.showConfirmDialog(null,"El programa a finalizado por el numero 0");
        
    }
}
