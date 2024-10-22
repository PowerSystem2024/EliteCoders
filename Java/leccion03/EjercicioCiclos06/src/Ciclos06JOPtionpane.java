/*
Ejercicio 6: Pedir nu,eros hasta que se teclee un 0,
mostrar la suma de todos los numeros introducisos
*/

import javax.swing.JOptionPane;
//AUTOR matias garcia
public class Ciclos06JOPtionpane {
    public static void main(String[] args) {
        
        //defino variables
        int num,suma = 0;
        
        //Que entre directamente al ciclo
        do {            
            //Pido al usuario que digite un numero y Convierto el valor a entero
            num=Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")) ;
             //Sumo la variable num y la guardo en suma
            suma+=num;
            //Imprimo la suma
            JOptionPane.showConfirmDialog(null,"La suma de los numeros son: "+suma);
            //Fin del ciclo
        } while (num!=0);
        //Imprimo la suma
        JOptionPane.showConfirmDialog(null,"La suma de los numeros son: "+suma);
    }
    
    
}
