// Ejercicio 8: Pedir un numero N y mostrar todos del 1 al N.
import javax.swing.JOptionPane;
public class Ejercicio8CiclosJOption {
    public static void main(String[] args) {
        
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: ")); 

        for (int i = 1; i <= numero; i++) {
            JOptionPane.showMessageDialog(null, i);
        }
    }
}