/* Ejercicio 1  Leer 10 numeros enteros, guardarlos en un arreglo. Debemos mostrarlos
en el siguiente orden: el primero, el ultimo, el segundo, el penultimo, el tercero, etc.
 */

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] numeros = new int[10];

        // Leer los 10 números y almacenarlos en el arreglo
        System.out.println("Ingresa 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        // Mostrar los números en el orden solicitado
        System.out.println("\nNúmeros en el orden solicitado:");
        for (int i = 0; i < 5; i++) {
            System.out.print(numeros[i] + " ");        // Mostrar el i-ésimo elemento desde el inicio
            System.out.print(numeros[9 - i] + " ");    // Mostrar el i-ésimo elemento desde el final
        }

        scanner.close();
    }
}

