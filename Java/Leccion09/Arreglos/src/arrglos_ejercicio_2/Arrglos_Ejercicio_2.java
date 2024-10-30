/*
 Ejercicio 2: Leer 5 números, guardarlos en 
    un arreglo y mostrarlos en el orden inveerso
 */
package arrglos_ejercicio_2;

import java.util.Scanner;

/**
 * @author matis
 */
public class Arrglos_Ejercicio_2 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int[] arreglo = new int[5];
        
        // Leer los números y almacenarlos en el arreglo
        for (int i = 0; i < 5; i++) {
            System.out.print((i + 1) + ". Digite un número: ");
            arreglo[i] = entrada.nextInt();
        }
        
        // Mostrar los números en el mismo orden
        System.out.println("\nImprimir los elementos del arreglo:");
        for (int i = 4; i >= 0; i--) {
            System.out.println(arreglo[i]);
        }
    }
}
