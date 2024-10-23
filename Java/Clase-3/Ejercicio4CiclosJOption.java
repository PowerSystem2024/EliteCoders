/* Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
y mostrar cuantos numerops se han introducido.
 */

import javax.swing.JOptionPane;

public class Ejercicio4CiclosJOption {
    public static void main(String[] args) {
        

        int numero = 1;
        int contador = 0;

        while (numero >= 0) {
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: "));
            if (numero < 0) {
                JOptionPane.showMessageDialog(null, "El programa ha finalizado");
                break;
            }
            else {
                contador++;
            }
        }

        JOptionPane.showMessageDialog(null, "Se han introducido " + contador + " numeros");
    }
}