import java.lang.Math;

import javax.swing.JOptionPane;
public class Ejercicio1JOptionPane {
    public static void main(String[] args) {
        int condition = 1;
        double numero, cuadrado;

        while (condition ==1) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));

            if (numero >= 0) {
                cuadrado = Math.pow(numero, 2);
                System.out.println("El cuadrado de " + numero + " es: " + cuadrado);
            } else {
                System.out.println("El ciclo a finalizado por numeros negativos");
                condition = 0;
                break;
            }    
        }
    }    
    
}
