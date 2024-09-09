/*Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso 
hasta que se introduzca un numero negativo

*/
package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine()); //convierte la entrada en intero
        while(numero >=0){ //Mientras el numero sea = 0 o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El número "+numero+ " elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro número:");
            numero = Integer.parseInt(entrada.nextLine()); 
        }
        System.out.println("El programa ha finalizado por numero negativo");
    }
    
    
    
}