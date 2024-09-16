/*
EJercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar
cuantos numeros se han introducidos.
Lo hacemmos primero con la clese scanner 
luefo lo hacemos con la clase JOptionPane
|||||||||||AHORA CON JOPTIONPANE|||||||||||||||
*/
package Ciclos04;
import javax.swing.JOptionPane;

/**
 *
 * @author Matias
 */
public class Ciclos04JOptionPane {
    public static void main(String[] args) {
        //Defino variable
        var  cantida_num =0;
       
        //Pido al usuario que digite un numero
        var num=Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")) ;
      
        //SI es distinto de NEGATIVO entra al bucle
        while (num >= 0){
            
             //INCREMENTOO EL VALOR PARA REPRESENTAR LA ACANTIDAD DE VESES QUE TECLEA Y IMPRIMO
            cantida_num++;    
            JOptionPane.showConfirmDialog(null,"LA CANTIDAD DE NUMEROS INGRESADOS: "+cantida_num);
            
            //Pido nuevamente que digite
            num=Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        
        
       //si es NEGATIVO imprimo esto
        JOptionPane.showConfirmDialog(null,"El programa a finalizado por el numero NEGATIVO");
    }
}
