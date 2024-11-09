/* Ejercicio 4 Leer por teclado una tabla de 10 elementos numericos enteros y una posicion (entre 0 y 9).
Eliminar el elemento situado en la posicion dada sin dejar huecos.
 */

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] tabla = new int[10]; // Tabla de tamaño 10
        int posicion; // Posición del elemento a eliminar

        // Leer los 10 elementos de la tabla
        System.out.println("Ingresa 10 números enteros:");
        for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            tabla[i] = scanner.nextInt();
        }

        // Leer la posición que se quiere eliminar
        System.out.print("Ingresa la posición (entre 0 y 9) del elemento a eliminar: ");
        posicion = scanner.nextInt();

        // Verificar que la posición esté en el rango válido
        if (posicion < 0 || posicion > 9) {
            System.out.println("Posición inválida.");
        } else {
            // Mover los elementos posteriores para eliminar el elemento en la posición dada
            for (int i = posicion; i < 9; i++) {
                tabla[i] = tabla[i + 1]; // Desplazar el siguiente elemento hacia la izquierda
            }

            // Establecer el último elemento como 0 (ya no es válido después de desplazar)
            tabla[9] = 0;

            // Mostrar la tabla después de eliminar el elemento
            System.out.println("\nTabla después de eliminar el elemento:");
            for (int i = 0; i < 10; i++) {
                System.out.print(tabla[i] + " ");
            }
        }

        scanner.close();
    }
}
