//Ejercicio1Ciclos
import java.util.Scanner;
import java.lang.Math;
public class Ejercicio1Ciclos {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        int condition = 1;
        double numero, cuadrado;

        while (condition ==1) {
            System.out.println("Ingrese un numero: ");
            numero = teclado.nextDouble();

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