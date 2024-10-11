//Ejercicio 12: Pedir un numero y calcular su factorial.

import java.util.Scanner;

public class EjercicioCiclos12Scanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);

        System.out.println("Ingresa un numero: ");
        int numero = valor.nextInt();

        int factorial = 1;
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }

        System.out.println("El factorial de " + numero + " es: " + factorial);
        valor.close();
    }
}