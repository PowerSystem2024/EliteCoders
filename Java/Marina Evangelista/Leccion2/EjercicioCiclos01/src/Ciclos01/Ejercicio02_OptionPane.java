/* Ejercicio 2: Leer un número e indicar si es positivo o negativo. 
El proceso se repetirá hasta que se introduzca un 0.
*/
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio02_OptionPane {
    
    public static void main(String[] args) {
        
        int numero;
        
        do {
            // Solicitar el número al usuario utilizando un cuadro de diálogo
            String input = JOptionPane.showInputDialog("Digite un número:");
            numero = Integer.parseInt(input); // Convertir la entrada en un número entero
            
            if (numero > 0) {
                JOptionPane.showInputDialog("El número " + numero + " es positivo");
            } 
            else if (numero < 0) {
                JOptionPane.showInputDialog("El número " + numero + " es negativo");
            }
            
        } while (numero != 0); // El bucle continúa hasta que el usuario ingrese 0
        
        // Mostrar un mensaje de finalización
        JOptionPane.showInputDialog("El número " + numero + " finaliza el programa");
    }
}
