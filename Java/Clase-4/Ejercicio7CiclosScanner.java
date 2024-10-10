/* Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo
y calcular la media
*/

import java.util.Scanner;
public class Ejercicio7CiclosScanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);

        int numero = 1;
        int contador = 0;
        int suma = 0;

        while (numero >= 0) {
            System.out.println("Ingresa un numero: ");
            numero = valor.nextInt();
            if (numero < 0) {
                System.out.println("El programa ha finalizado");
                break;
            } else {
                suma += numero;
                contador++;
            }
        }

        System.out.println("La media es: " + (suma / contador));
        valor.close();
    }
}
