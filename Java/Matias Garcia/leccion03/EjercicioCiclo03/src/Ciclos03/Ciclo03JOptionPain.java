/*
Ejercicio 3:Leer numeros hasta que se introduzca un cero 
Para cada uno indicar si es par o impar
Primero lo haremos con la clase Scanner
|||||AHORA con la clase JOPtionPane|||
*/

package Ciclos03;

import javax.swing.JOptionPane;

public class Ciclo03JOptionPain {
    
    public static void main(String[] args) {
        
        //Pido al usuario que digite un numero
        var num=Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")) ;
        //SI es distinto de 0 entra al bucle
        while (num !=0){
            if (num %2 ==0){
             //si es PAR imprimo esto
                JOptionPane.showConfirmDialog(null,"EL NUMERO ES PAR: "+num);
               
            }
            else {
                 //si es IMPAR imprimo esto
                JOptionPane.showConfirmDialog(null,"EL NUMERO ES IMPAR: " +num);
            }
                
            num=Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        
        
       //si es igual a 0 imprimo esto
     
        JOptionPane.showConfirmDialog(null,"El programa a finalizado por el numero 0");
    }
}
