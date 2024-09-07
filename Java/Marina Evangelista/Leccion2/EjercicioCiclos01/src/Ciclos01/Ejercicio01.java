/*Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso 
hasta que se introduzca un numero negativo
*/
package Ciclos01;

import javax.swing.JOptionPane; //Otra opcion para el scanner- ventana emergente

public class Ejercicio01 {
    public static void main(String[] args) {
         int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >=0){ //Mientras el numero sea = 0 o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+ " elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        System.out.println("El programa ha finalizado por numero negativo");
    }
}
