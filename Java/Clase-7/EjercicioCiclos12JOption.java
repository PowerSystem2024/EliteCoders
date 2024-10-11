//Ejercicio 12: Pedir un numero y calcular su factorial.

import javax.swing.JOptionPane;

public class EjercicioCiclos12JOption {
    public static void main(String[] args) {
     
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingresa un numero: "));

        int factorial = 1;
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }

        JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
    }
}