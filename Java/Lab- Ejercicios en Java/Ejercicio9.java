/* Ejercicio 9 Crear una matriz “marco” de tamaño 5x5: todos sus elementos deben ser 0,
salvo los de los bordes que deben ser 1. Mostrarla.
 */

public class Ejercicio9 {
    public static void main(String[] args) {
        int[][] matriz = new int[5][5];

        // Crear la matriz "marco"
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                // Asignar 1 a los elementos del borde y 0 al resto
                if (i == 0 || i == 4 || j == 0 || j == 4) {
                    matriz[i][j] = 1;
                } else {
                    matriz[i][j] = 0;
                }
            }
        }

        // Mostrar la matriz "marco"
        System.out.println("Matriz marco de 5x5:");
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
