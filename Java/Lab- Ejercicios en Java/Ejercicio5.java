/* Ejercicio 5 Leer 10 enteros en una tabla. Guardar en otra tabla los elementos pares de la primera,
y a continuacion los elementos impares.
 */

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] tabla = new int[10]; // Tabla de tamaño 10
        int[] resultado = new int[10]; // Tabla para almacenar los números pares seguidos de los impares

        // Leer los 10 elementos de la tabla
        System.out.println("Ingresa 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            tabla[i] = scanner.nextInt();
        }

        // Contadores para los números pares e impares
        int contadorPares = 0;
        int contadorImpares = 0;

        // Clasificar los números pares y impares en la tabla de resultado
        for (int i = 0; i < 10; i++) {
            if (tabla[i] % 2 == 0) {
                resultado[contadorPares] = tabla[i];  // Guardar los pares
                contadorPares++;
            } else {
                resultado[10 - 1 - contadorImpares] = tabla[i];  // Guardar los impares
                contadorImpares++;
            }
        }

        // Mostrar la tabla resultante
        System.out.println("\nTabla con los elementos pares seguidos de los impares:");
        for (int i = 0; i < 10; i++) {
            System.out.print(resultado[i] + " ");
        }

        scanner.close();
    }
}

