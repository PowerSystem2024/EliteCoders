/*Ejercicio 3: Leer numeros hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
*/

import java.util.Scanner;

public class Ejercicio3CiclosScanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);

        int numero = 1;

        while (numero > 0) {
            System.out.println("Ingresa un numero: ");
            numero = Integer.parseInt(valor.nextLine());
            if (numero % 2 == 0 && numero != 0) {
                System.out.println("El numero es par");
            } else {
                if (numero != 0) {
                System.out.println("El numero es impar");
                }
            }
        }
        System.out.println("El programa ha finalizado");
        valor.close();
    }
}
