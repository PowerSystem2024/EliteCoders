// Ejercicio 8: Pedir un numero N y mostrar todos del 1 al N.

import java.util.Scanner;

public class Ejercicio8CiclosScanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);
        
        System.out.println("Ingresa un numero: ");
        int numero = valor.nextInt();

        for (int i = 1; i <= numero; i++) {
            System.out.println(i);
        }
        valor.close();
    }
}