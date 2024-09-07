/* Ejercicio 2: Leer un número e indicar si es positivo o negativo. 
El proceso se repetirá hasta que se introduzca un 0.
*/
package Ciclos01;

import java.util.Scanner;

public class Ejercicio02 {
    
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int numero;
        
        do {
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(entrada.nextLine()); // Conversión y guardar la entrada
            
            if (numero > 0){
                System.out.println("El número "+numero+ " es positivo");
            }
            else if (numero < 0) {
                System.out.println("El número "+numero+ " es negativo");
            }
        } while(numero != 0);
        
        System.out.println("El número "+numero+ " finaliza el programa");
    }
}

