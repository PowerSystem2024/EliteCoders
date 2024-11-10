/* Ejercicio 8 Utilizando dos matrices de tamaño 5x9 y 9x5,
cargar la primera y transponerla en la segunda
 */

import java.util.Scanner;

public class Ejercicio8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] matrizA = new int[5][9];
        int[][] matrizB = new int[9][5];

        // Cargar la primera matriz (5x9)
        System.out.println("Ingrese los elementos de la matriz de tamaño 5x9:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                System.out.print("Elemento [" + i + "][" + j + "]: ");
                matrizA[i][j] = scanner.nextInt();
            }
        }

        // Transponer la matrizA en matrizB
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 9; j++) {
                matrizB[j][i] = matrizA[i][j];
            }
        }

        // Mostrar la matriz transpuesta (9x5)
        System.out.println("\nMatriz transpuesta (9x5):");
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matrizB[i][j] + "\t");
            }
            System.out.println();
        }

        scanner.close();
    }
}
