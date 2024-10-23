//Ejercicio 10: Pedir 10 numeros y escribir la suma total

import java.util.Scanner;

public class EjercicioCiclos10Scanner {
    public static void main(String[] args) {

        Scanner valor = new Scanner(System.in);
        int suma = 0;

        for (int i = 0; i < 10; i++) {
            System.out.println("Ingresa el valor " + (i + 1) + ": ");
            suma += valor.nextInt();
        }

        System.out.println("La suma de todos los numeros es: " + suma);
        valor.close();
    }
}

