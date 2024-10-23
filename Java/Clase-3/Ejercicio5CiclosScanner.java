/* Ejercicio 5: Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0-100, y
luego ir pidiendo numeros indicando si es mayor o menor.
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos.
 */

import java.util.Scanner;
public class Ejercicio5CiclosScanner {
    public static void main(String[] args) {
        Scanner valor = new Scanner(System.in);
        int numero = (int) (Math.random() * 100);
        int intentos = 0; 
        int num = 0;

        while (numero != num) {
            System.out.println("Ingresa un numero: ");
            num = valor.nextInt();
            intentos++;
            if (num > numero) {
                System.out.println("El numero es menor\n");
            } else if (num < numero) {
                System.out.println("El numero es mayor\n");
            } else {
                System.out.println("Felicidades, adivinaste el numero en " + intentos + " intentos");
            }
        }
        valor.close();
    }
    
}
