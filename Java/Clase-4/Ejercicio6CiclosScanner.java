/* Ejercicio 6: Pedir numeros hasta que se teclee un 0, mostrar
la suma de todos los numeros introducidos.
 */

import java.util.Scanner;

public class Ejercicio6CiclosScanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);
        int total = 0;
        int num = 1;

        while (num != 0) {
            System.out.println("Ingresa un numero: ");
            num = valor.nextInt();
            total += num;
        }

        System.out.println("La suma de todos los numeros es: " + total);
        valor.close();
    }
}