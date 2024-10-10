/*Ejercicio 3: Leer numeros hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
*/
import javax.swing.JOptionPane;
public class Ejercicio3CiclosJOption {
    public static void main(String[] args) {

        int numero = 1;

        while (numero > 0) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: "));
            if (numero % 2 == 0 && numero != 0) {
                JOptionPane.showMessageDialog(null, "El numero es par");
            } else {
                if (numero != 0) {
                JOptionPane.showMessageDialog(null, "El numero es impar");
                }
            }
        }
        JOptionPane.showMessageDialog(null, "El programa ha finalizado");

    }
}