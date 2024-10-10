/* Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo
y calcular la media
*/

import javax.swing.JOptionPane;

public class Ejercicio7CiclosJOption {
    public static void main(String[] args) {

        int numero = 1;
        int contador = 0;
        int suma = 0;

        while (numero >= 0) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: "));
            if (numero < 0) {
                JOptionPane.showMessageDialog(null, "El programa ha finalizado");
                break;
            } else {
                suma += numero;
                contador++;
            }
        }

        JOptionPane.showMessageDialog(null, "La media es: " + (suma / contador));
    }
}
