/* Ejercicio 6 Leer dos series de 10 numeros enteros, que estaran ordenados crecientemente. Copiar (fusionar)
las dos tablas en una tercera, de forma que sigan ordenados.
 */

import java.util.Scanner;
import java.util.Arrays;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] serie1 = new int[10]; // Primera serie de números
        int[] serie2 = new int[10]; // Segunda serie de números
        int[] fusionada = new int[20]; // Tabla para almacenar la fusión
        boolean creciente = true;

        // Leer los 10 números de la primera serie
        System.out.println("Ingresa 10 números de la primera serie (ordenados crecientemente):");
        do {
            creciente = true; // Asumimos que la serie está en orden creciente
            for (int i = 0; i < 10; i++) {
                System.out.print("Número " + (i + 1) + ": ");
                serie1[i] = scanner.nextInt();
            }
            // Verificar si la serie1 está ordenada de forma creciente
            for (int i = 0; i < 9; i++) {
                if (serie1[i] > serie1[i + 1]) {
                    creciente = false;
                    break;
                }
            }

            if (!creciente) {
                System.out.println("La serie 1 no está ordenada de forma creciente. Intenta de nuevo.");
            }
        } while (!creciente);

        // Leer los 10 números de la segunda serie
        System.out.println("Ingresa 10 números de la segunda serie (ordenados crecientemente):");
        do {
            creciente = true; // Asumimos que la serie está en orden creciente
            for (int i = 0; i < 10; i++) {
                System.out.print("Número " + (i + 1) + ": ");
                serie2[i] = scanner.nextInt();
            }
            // Verificar si la serie2 está ordenada de forma creciente
            for (int i = 0; i < 9; i++) {
                if (serie2[i] > serie2[i + 1]) {
                    creciente = false;
                    break;
                }
            }

            if (!creciente) {
                System.out.println("La serie 2 no está ordenada de forma creciente. Intenta de nuevo.");
            }
        } while (!creciente);

        // Fusionar las dos series de forma ordenada
        int i = 0, j = 0, k = 0;
        while (i < 10 && j < 10) {
            if (serie1[i] <= serie2[j]) {
                fusionada[k] = serie1[i]; // Agregar elemento de serie1
                i++; // Mover el índice de serie1
            } else {
                fusionada[k] = serie2[j]; // Agregar elemento de serie2
                j++; // Mover el índice de serie2
            }
            k++; // Mover al siguiente índice de la tabla fusionada
        }

        // Si hay elementos restantes en serie1, agregarlos
        while (i < 10) {
            fusionada[k] = serie1[i];
            i++;
            k++;
        }

        // Si hay elementos restantes en serie2, agregarlos
        while (j < 10) {
            fusionada[k] = serie2[j];
            j++;
            k++;
        }

        // Ordenar la tabla fusionada (en caso de que algo se haya desordenado)
        Arrays.sort(fusionada);

        // Mostrar la tabla fusionada
        System.out.println("\nTabla fusionada (ordenada):");
        for (int num : fusionada) {
            System.out.print(num + " ");
        }

        scanner.close();
    }
}

