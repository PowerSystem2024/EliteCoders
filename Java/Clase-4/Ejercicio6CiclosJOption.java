/* Ejercicio 6: Pedir numeros hasta que se teclee un 0, mostrar
la suma de todos los numeros introducidos.
 */

import javax.swing.JOptionPane;

public class Ejercicio6CiclosJOption {
     public static void main(String[] args) {

         int total = 0;
         int num = 1;
 
         while (num != 0) {
             num = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: "));
             total += num;
         }
 
         JOptionPane.showMessageDialog(null, "La suma de todos los numeros es: " + total);
     }
 }