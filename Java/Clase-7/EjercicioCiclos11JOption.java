//Ejercicio 11: Diseñar un programa que muestre el producto de los 10 primero numeros impares.

import javax.swing.JOptionPane;

public class EjercicioCiclos11JOption {
    public static void main(String[] args) {
        
        int producto = 1;
        for (int i = 0; i < 20; i++) {
            if (i % 2 != 0) {
                producto *= i;
            }
        }
        JOptionPane.showMessageDialog(null, "El producto de los 10 primero numeros impares es: " + producto);
                
    }
}