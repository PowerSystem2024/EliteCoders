//Ejercicio 10: Pedir 10 numeros y escribir la suma total

import javax.swing.JOptionPane;

public class EjercicioCiclos10JOption {
    public static void main(String[] args) {

        int suma = 0;

        for (int i = 0; i < 10; i++) {
            int valor = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el valor " + (i + 1) + ": "));
            suma += valor;
        }

        JOptionPane.showMessageDialog(null, "La suma de todos los numeros es: " + suma);
    }
}
