/* Ejercicio 3 Leer 5 elementos numericos que se introduciran ordenadosde forma creciente.
Estos los guardaremos en una tabla de tamaño 10. Leer un numero N, e insertarlo en el lugar adecuado
para que la tabla continue ordenada
 */

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] tabla = new int[10]; // Tabla de tamaño 10
        int N; // El número que vamos a insertar

        // Leer los 5 elementos ordenados de forma creciente
        System.out.println("Ingresa 5 números ordenados de forma creciente:");
        for (int i = 0; i < 5; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            tabla[i] = scanner.nextInt();
        }

        // Leer el número N que se quiere insertar
        System.out.print("Ingresa el número N que deseas insertar: ");
        N = scanner.nextInt();

        // Insertar N en el lugar adecuado para mantener el orden creciente
        int i = 4; // El último índice con valor válido en la tabla
        while (i >= 0 && tabla[i] > N) {
            tabla[i + 1] = tabla[i]; // Mover el valor hacia la derecha
            i--;
        }
        tabla[i + 1] = N; // Insertar N en la posición correcta

        // Mostrar la tabla después de insertar N
        System.out.println("\nTabla después de insertar el número N:");
        for (int j = 0; j < 10; j++) {
            System.out.print(tabla[j] + " ");
        }

        scanner.close();
    }
}


