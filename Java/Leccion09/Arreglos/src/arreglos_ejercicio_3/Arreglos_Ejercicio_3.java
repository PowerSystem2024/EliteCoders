import java.util.Scanner;

public class Arreglos_Ejercicio_3 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int[] arreglo = new int[5];
        int sumaPositivo = 0;
        int sumaNegativo = 0;
        int cantidadPositivo = 0;
        int cantidadNegativo = 0;
        int ceros = 0;
        
        // Leer los números y almacenarlos en el arreglo
        for (int i = 0; i < 5; i++) {
            System.out.print((i + 1) + ". Digite un número: ");
            arreglo[i] = entrada.nextInt();
            
            if (arreglo[i] > 0) {
                sumaPositivo += arreglo[i];
                cantidadPositivo++;
            } else if (arreglo[i] < 0) {
                sumaNegativo += arreglo[i];
                cantidadNegativo++;
            } else {
                ceros++;
            }
        }
        
        // Mostrar los números en el mismo orden
        System.out.println("\nImprimir los elementos del arreglo:");
        for (int i = 0; i < 5; i++) {
            System.out.println(arreglo[i]);
        }
        
        // Calculando la media de positivos
        if (cantidadPositivo > 0) {
            System.out.println("La media de los números positivos es: " + (sumaPositivo / cantidadPositivo));
        } else {
            System.out.println("No hay números positivos.");
        }
        
        // Calculando la media de negativos
        if (cantidadNegativo > 0) {
            System.out.println("La media de los números negativos es: " + (sumaNegativo / cantidadNegativo));
        } else {
            System.out.println("No hay números negativos.");
        }
        
        // Mostrar la cantidad de ceros
        System.out.println("La cantidad de ceros es: " + ceros);
    }
}
