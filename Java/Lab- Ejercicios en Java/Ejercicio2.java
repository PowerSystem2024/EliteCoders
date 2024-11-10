/* Ejercicio 2 Leer por teclado dos tablas de 10 numeros enteros y mezclarlas en una tercera de la forma: el 1o de A, el 1o de B, 2o de A, 2o de B, etc.
 */

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] A = new int[10];
        int[] B = new int[10];
        int[] C = new int[20]; // El arreglo C contendrá los números mezclados

        // Leer los 10 números para la tabla A
        System.out.println("Ingresa los 10 números para la tabla A:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            A[i] = scanner.nextInt();
        }

        // Leer los 10 números para la tabla B
        System.out.println("Ingresa los 10 números para la tabla B:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            B[i] = scanner.nextInt();
        }

        // Mezclar las tablas A y B en C
        for (int i = 0; i < 10; i++) {
            C[2 * i] = A[i];    // El elemento i de A se coloca en el índice par de C
            C[2 * i + 1] = B[i]; // El elemento i de B se coloca en el índice impar de C
        }

        // Mostrar la tabla C mezclada
        System.out.println("\nTabla C (mezclada):");
        for (int i = 0; i < 20; i++) {
            System.out.print(C[i] + " ");
        }

        scanner.close();
    }
}

