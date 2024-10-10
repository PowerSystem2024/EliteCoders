/* Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
y mostrar cuantos numerops se han introducido.
 */

import java.util.Scanner;

public class Ejercicio4CiclosScanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);

        int numero = 1;
        int contador = 0;

        while (numero >= 0) {
            System.out.println("Ingresa un numero: ");
            numero = valor.nextInt();
            if (numero < 0) {
                System.out.println("El programa ha finalizado");
                break;
            }
            else {
                contador++;
            }
        }

        System.out.println("Se han introducido " + contador + " numeros");
        valor.close();
    }
}