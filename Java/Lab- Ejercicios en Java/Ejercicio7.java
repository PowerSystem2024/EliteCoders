/* Ejercicio 7 Leer 10 numeros enteros ordenados crecientemente. Leer N y buscarlo en la tabla.
Se debe mostrar la posicion en que se encuentra. Si no esta, indicarlo con un mensaje.
 */

import java.util.Scanner;

public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[10];

        // Leer 10 números enteros en orden creciente
        System.out.println("Ingrese 10 números enteros en orden creciente:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();

            // Validar que los números estén en orden creciente
            if (i > 0 && numeros[i] < numeros[i - 1]) {
                System.out.println("Los números deben estar en orden creciente. Inténtelo de nuevo.");
                i--; // Repetir la entrada de este número
            }
        }

        // Leer el número N a buscar
        System.out.print("Ingrese el número a buscar (N): ");
        int N = scanner.nextInt();

        // Buscar N en el arreglo
        int posicion = -1;
        for (int i = 0; i < 10; i++) {
            if (numeros[i] == N) {
                posicion = i;
                break;
            }
        }

        // Mostrar el resultado
        if (posicion != -1) {
            System.out.println("El número " + N + " se encuentra en la posición: " + posicion);
        } else {
            System.out.println("El número " + N + " no se encuentra en la tabla.");
        }

        scanner.close();
    }
}



